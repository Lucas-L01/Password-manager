import secrets
import hashlib
import os
import json
import base64
import sys

# hash the master password and add the salt
def derive_key(master_password, salt):
    key = hashlib.pbkdf2_hmac(
        "sha256",
        master_password.encode("utf-8"),
        salt.encode("utf-8"),
        600000,
        32
    )
    return base64.b64encode(key).decode("utf-8")

def login():
    VAULT_FILE = "data/vault.json"
    print("Enter your master password")
    Password = input("> ")

    with open(VAULT_FILE, "r") as f:
        data = json.load(f)
    Master_Hash = data["Master_Hash"]
    Salt = data["Salt"]
    hashed_salted_password = derive_key(Password, Salt)
    if hashed_salted_password == Master_Hash:
        print("correct master password")
    else:
        print("wrong master pasword")
        sys.exit()
        

def setup():
    VAULT_FILE = "data/vault.json"
    os.mkdir("data")
    salt = secrets.token_hex(16)

    print("set your Master Password for the Password Manager")
    MP = input("> ")
    Hashed_MP_salted = derive_key(MP, salt)
    with open(VAULT_FILE, "w") as f:
        json.dump({"Master_Hash": Hashed_MP_salted, "Salt": salt}, f, indent=4)
