from flask import Flask, request, jsonify, render_template, Response
from werkzeug.utils import secure_filename
import os
from utils import encrypt_file, decrypt_file
from key_manager import generate_key

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"

# Ensure folders exist and are writable
for folder in [UPLOAD_FOLDER, RESULT_FOLDER]:
    os.makedirs(folder, exist_ok=True)
    if not os.access(folder, os.W_OK):
        raise Exception(f"Cannot write to folder: {folder}")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate-key", methods=["GET"])
def generate():
    try:
        key = generate_key()  # Assuming generate_key() returns the key
        return jsonify({"status": "Key generated", "key": key.decode()})
    except Exception as e:
        return jsonify({"status": "Key generation failed", "error": str(e)}), 500

@app.route("/encrypt", methods=["POST"])
def encrypt():
    # Define paths as None initially
    input_path = None
    output_path = None
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file part in request"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400

        filename = secure_filename(file.filename)
        input_path = os.path.join(UPLOAD_FOLDER, filename)
        output_path = os.path.join(RESULT_FOLDER, filename + ".enc")

        # Save the uploaded file
        file.save(input_path)

        # Ensure the file was saved correctly
        if not os.path.exists(input_path):
            raise Exception("Failed to save uploaded file")

        # Encrypt the file
        encrypt_file(input_path, output_path)

        # Read the encrypted file into memory and close the file handle
        with open(output_path, "rb") as f:
            encrypted_data = f.read()

        # Create a response with the file data
        response = Response(
            encrypted_data,
            mimetype="application/octet-stream",
            headers={"Content-Disposition": f"attachment; filename={filename}.enc"}
        )

        return response

    except Exception as e:
        # Log the error
        print(f"[!] Encryption failed: {str(e)}")
        return jsonify({"error": f"Encryption failed: {str(e)}"}), 500

    finally:
        # Clean up temporary files
        for path in [input_path, output_path]:
            if path and os.path.exists(path):
                try:
                    os.remove(path)
                    print(f"[+] Successfully removed {path}")
                except Exception as e:
                    print(f"[!] Failed to remove {path}: {str(e)}")

@app.route("/decrypt", methods=["POST"])
def decrypt():
    # Define paths as None initially
    input_path = None
    output_path = None
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file part in request"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400

        filename = secure_filename(file.filename)
        input_path = os.path.join(UPLOAD_FOLDER, filename)
        # Remove '.enc' and any existing extension, then append '.txt'
        base_name = os.path.splitext(filename.replace(".enc", ""))[0]
        decrypted_filename = f"{base_name}_decrypted.txt"
        output_path = os.path.join(RESULT_FOLDER, decrypted_filename)

        # Save the uploaded file
        file.save(input_path)

        # Ensure the file was saved correctly
        if not os.path.exists(input_path):
            raise Exception("Failed to save uploaded file")

        # Decrypt the file
        success = decrypt_file(input_path, output_path)
        if not success:
            raise Exception("Decryption failed. Invalid key or corrupted file.")

        # Read the decrypted file into memory and close the file handle
        with open(output_path, "rb") as f:
            decrypted_data = f.read()

        # Create a response with the file data, ensuring the downloaded file has .txt extension
        response = Response(
            decrypted_data,
            mimetype="text/plain",
            headers={"Content-Disposition": f"attachment; filename={decrypted_filename}"}
        )

        return response

    except Exception as e:
        # Log the error
        print(f"[!] Decryption failed: {str(e)}")
        return jsonify({"error": f"Decryption failed: {str(e)}"}), 400

    finally:
        # Clean up temporary files
        for path in [input_path, output_path]:
            if path and os.path.exists(path):
                try:
                    os.remove(path)
                    print(f"[+] Successfully removed {path}")
                except Exception as e:
                    print(f"[!] Failed to remove {path}: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
