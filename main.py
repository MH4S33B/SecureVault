from flask import Flask, request, send_file, jsonify, render_template
from werkzeug.utils import secure_filename
import os
from utils import encrypt_file, decrypt_file
from key_manager import generate_key

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate-key", methods=["GET"])
def generate():
    generate_key()
    return jsonify({"status": "Key generated"})

@app.route("/encrypt", methods=["POST"])
def encrypt():
    try:
        file = request.files["file"]
        filename = secure_filename(file.filename)
        input_path = os.path.join(UPLOAD_FOLDER, filename)
        output_path = os.path.join(RESULT_FOLDER, filename + ".enc")
        file.save(input_path)

        encrypt_file(input_path, output_path)
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        print(f"[!] Encryption failed: {e}")
        return "Encryption failed", 500

@app.route("/decrypt", methods=["POST"])
def decrypt():
    if "file" not in request.files:
        return "No file part", 400

    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    filename = secure_filename(file.filename)
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    output_path = os.path.join(RESULT_FOLDER, filename.replace(".enc", "_decrypted"))
    file.save(input_path)

    success = decrypt_file(input_path, output_path)
    if not success:
        return "Decryption failed. Invalid key or corrupted file.", 400

    return send_file(output_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
