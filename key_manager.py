from cryptography.fernet import Fernet

def generate_key():
    try:
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        print("[+] Key generated and saved as 'key.key'")
        return key  # Return the key
    except Exception as e:
        print(f"[!] Failed to generate key: {e}")
        raise

def load_key():
    try:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
        # Validate key format (Fernet keys are 44 bytes base64-encoded)
        if not key or len(key) != 44:
            raise Exception("Invalid key format or corrupted key file")
        return key
    except Exception as e:
        print(f"[!] Failed to load key: {e}")
        raise
