from cryptography.fernet import Fernet
import os
from key_manager import load_key

def encrypt_file(file_path, output_path):
    if not os.path.exists("key.key"):
        raise Exception("Key not found. Generate it first.")

    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(output_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt_file(file_path, output_path):
    if not os.path.exists("key.key"):
        print("[-] Key not found. Generate key first.")
        return False

    key = load_key()
    fernet = Fernet(key)

    try:
        with open(file_path, "rb") as enc_file:
            encrypted = enc_file.read()

        decrypted = fernet.decrypt(encrypted)

        with open(output_path, "wb") as dec_file:
            dec_file.write(decrypted)

        print(f"[+] File decrypted and saved as '{output_path}'")
        return True

    except Exception as e:
        print("[-] Decryption failed. Invalid key or file.")
        return False