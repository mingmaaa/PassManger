import os

VAULT_FILE = "vault.enc"

def load_file():
    if not os.path.exists(VAULT_FILE):
        return None
    with open(VAULT_FILE, "rb") as f:
        return f.read()

def save_file(data: bytes):
    with open(VAULT_FILE, "wb") as f:
        f.write(data)