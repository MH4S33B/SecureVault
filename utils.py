from cryptography.fernet import Fernet
import os
import struct
from key_manager import load_key
from cryptography.fernet import InvalidToken

def encrypt_file(file_path, output_path):
    # Check if key exists
    if not os.path.exists("key.key"):
        raise Exception("Encryption key not found. Please generate a key first.")

    # Check if input file exists and is readable
    if not os.path.isfile(file_path) or not os.access(file_path, os.R_OK):
        raise Exception(f"Cannot read input file: {file_path}")

    # Check if output path is writable
    output_dir = os.path.dirname(output_path)
    if not os.access(output_dir, os.W_OK):
        raise Exception(f"Cannot write to output directory: {output_dir}")

    try:
        key = load_key()
        fernet = Fernet(key)
    except Exception as e:
        raise Exception(f"Failed to initialize Fernet with key: {str(e)}")

    try:
        with open(file_path, "rb") as file, open(output_path, "wb") as encrypted_file:
            while chunk := file.read(8192):  # Read 8KB at a time
                encrypted_chunk = fernet.encrypt(chunk)
                # Write the length of the encrypted chunk as a 4-byte integer
                encrypted_file.write(struct.pack("!I", len(encrypted_chunk)))
                # Write the encrypted chunk
                encrypted_file.write(encrypted_chunk)
    except Exception as e:
        raise Exception(f"Encryption failed: {str(e)}")

def decrypt_file(file_path, output_path):
    # Check if key exists
    if not os.path.exists("key.key"):
        print("[-] Key not found. Generate key first.")
        raise Exception("Decryption key not found. Please generate a key first.")

    # Check if input file exists and is readable
    if not os.path.isfile(file_path) or not os.access(file_path, os.R_OK):
        raise Exception(f"Cannot read input file: {file_path}")

    # Check if output path is writable
    output_dir = os.path.dirname(output_path)
    if not os.access(output_dir, os.W_OK):
        raise Exception(f"Cannot write to output directory: {output_dir}")

    try:
        key = load_key()
        fernet = Fernet(key)
    except Exception as e:
        print(f"[-] Failed to initialize Fernet with key: {str(e)}")
        raise Exception(f"Failed to initialize Fernet with key: {str(e)}")

    try:
        with open(file_path, "rb") as enc_file, open(output_path, "wb") as dec_file:
            while True:
                # Read the length of the next encrypted chunk (4 bytes)
                length_bytes = enc_file.read(4)
                if not length_bytes:  # End of file
                    break
                # Unpack the length
                (chunk_length,) = struct.unpack("!I", length_bytes)
                # Read the encrypted chunk
                encrypted_chunk = enc_file.read(chunk_length)
                if len(encrypted_chunk) != chunk_length:
                    raise Exception("Incomplete encrypted chunk read: file may be corrupted")
                # Decrypt the chunk
                decrypted_chunk = fernet.decrypt(encrypted_chunk)
                # Write the decrypted chunk
                dec_file.write(decrypted_chunk)

        print(f"[+] File decrypted and saved as '{output_path}'")
        return True
    except InvalidToken as e:
        print(f"[-] Decryption failed: Invalid token - the file may be corrupted or the key is incorrect: {str(e)}")
        raise Exception("Decryption failed: Invalid token - the file may be corrupted or the key is incorrect")
    except Exception as e:
        print(f"[-] Decryption failed: {str(e)}")
        raise Exception(f"Decryption failed: {str(e)}")
