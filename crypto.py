import base64
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.fernet import Fernet

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt(data: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(data)

def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)