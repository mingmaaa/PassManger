# PassManager

A simple command-line password manager written in Python.

## Features

- Create and store credentials securely in an encrypted local vault
- Add new entries (`name`, `username`, `password`)
- Retrieve stored credentials
- List saved entry names
- Master-password-based key derivation and encryption

## Project Structure

- `main.py` — CLI flow and command handling
- `cli.py` — argument parsing
- `storage.py` — vault file read/write
- `crypto.py` — key derivation, encryption, decryption
- `models.py` — `Vault` data model
- `utils.py` — helper utilities (e.g., password prompt)

## Requirements

- Python 3.9+
- `cryptography`

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py add <name> <username> <password>
python main.py get <name>
python main.py list
```