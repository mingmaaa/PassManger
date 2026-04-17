import json
import os
import sys

from cli import parse_args
from storage import load_file, save_file
from crypto import derive_key, encrypt, decrypt
from models import Vault
from utils import get_master_password

def main():
    args = parse_args()

    if not args.command:
        print("No command provided. Use --help.")
        sys.exit(1)

    password = get_master_password()
    raw = load_file()

    #load vault
    if raw is None:
        salt = os.urandom(16)
        vault = Vault()
    else:
        try:
            salt = raw[:16]
            encrypted = raw[16:]
            key = derive_key(password, salt)
            decrypted = decrypt(encrypted, key)
            data = json.loads(decrypted.decode())
            vault = Vault(data)
        except Exception:
            print("Incorrect password or corrupted vault.")
            sys.exit(1)

    key = derive_key(password, salt)

    # Commands
    if args.command == "add":
        vault.add(args.name, args.username, args.password)
        print(f"Added entry: {args.name}")

    elif args.command == "get":
        entry = vault.get(args.name)
        if entry:
            print(f"Username: {entry['username']}")
            print(f"Password: {entry['password']}")
        else:
            print("Not found.")

    elif args.command == "list":
        for name in vault.list():
            print("-", name)

    # Save vault
    encrypted = encrypt(json.dumps(vault.data).encode(), key)
    save_file(salt + encrypted)

if __name__ == "__main__":
    main()