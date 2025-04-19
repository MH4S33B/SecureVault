# 🔐 SecureVault

SecureVault is a modern web-based application designed to securely encrypt and decrypt files using symmetric encryption. Built with Flask for the backend and a sleek, futuristic frontend, SecureVault provides an intuitive interface for users to protect their sensitive files with ease. Whether you're safeguarding personal documents or sharing encrypted files, SecureVault ensures your data remains secure.

---

## ✨ Features

- **File Encryption & Decryption**: Securely encrypt files with a `.enc` extension and decrypt them using a Fernet key.
- **Key Generation**: Generate a unique symmetric encryption key for secure file processing.
- **Drag-and-Drop Interface**: Upload files effortlessly with a responsive drag-and-drop feature.
- **Futuristic UI**: Enjoy a visually stunning interface with glassmorphism, neon glow effects, and light/dark theme toggle.
- **Real-Time Feedback**: Progress bars, toast notifications, and particle animations enhance the user experience.
- **Cross-Platform**: Works on any modern browser, with a responsive design for mobile and desktop.
- **Open Source**: Licensed under the MIT License, inviting contributions and customization.

---

## 🛠️ Technologies Used

- **Backend**: Python, Flask, `cryptography` (Fernet)
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Custom CSS with animations, Google Fonts (Poppins), Font Awesome
- **Dependencies**: Listed in `requirements.txt`

---

## 📂 Project Structure

```
file-encryption-app/
│
├── main.py
├── key_manager.py
├── utils.py
├── requirements.txt
├── LICENSE
│
├── templates/
│   └── index.html
│
├── static/
|   └── script.js
|
└── assets/
    └── All Project related Screenshots and an mp4 video
```
---
## 🚀 Getting Started

Follow these steps to set up and run SecureVault locally.

### 🔧 Prerequisites

- Python 3.8 or higher  
- pip (Python package manager)  
- Git (optional, for cloning the repository)

### 💻 Installation

**Clone the Repository:**

```bash
git clone https://github.com/MH4S33B/SecureVault.git
cd SecureVault
```
**Create a Virtual Environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
**Install Dependencies:**
```bash
pip install -r requirements.txt
```
**Run the Application:**
```bash
python main.py
```
**Access the App:**
Open your browser and navigate to ```http://127.0.0.1:5000```.

---
### 🗂 Directory Setup
The app automatically creates two folders:
- ```uploads/```: Stores uploaded files temporarily.
- ```results/```: Stores encrypted and decrypted files.

---
## 📖 Usage
### 🔑 Generate a Key
- Click the "Generate Key" button to create a ```key.key``` file for encryption/decryption.
- Important: Store this key securely, as it’s required for decryption.
### 🔐 Encrypt a File
- Drag and drop a file or click to upload.
- Click "Encrypt" to process the file.
- Download the encrypted file (with ```.enc``` extension).
### 🔓 Decrypt a File
- Upload an encrypted ```.enc``` file.
- Ensure the correct ```key.key``` is present in the project root.
- Click "Decrypt" to process the file.
- Download the decrypted file (with ```_decrypted``` in the name).
### 🌗 Toggle Theme
- Use the moon/sun icon to switch between dark and light modes.
## 🖼️ Screenshots

## ⚠️ Notes
- **Key Management**: Always back up your ```key.key``` file. Without it, encrypted files cannot be decrypted.

- **Debug Mode**: The app runs in debug mode by default (```app.run(debug=True)```). For production, use a WSGI server like Gunicorn and disable debug mode.

- **Security**: Fernet provides strong symmetric encryption, but ensure the key is stored securely and not exposed publicly.

- **Client-Side Key Display**: The JavaScript ```generateKey``` function displays a random string for UI purposes, not the actual Fernet key.

## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch: ```git checkout -b feature/your-feature```.
3. Make your changes and commit: ```git commit -m 'Add your feature'```.
4. Push to the branch: ```git push origin feature/your-feature```.
5. Open a Pull Request.
Please ensure your code follows the project's style and includes tests where applicable.

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 🙌 Acknowledgments
Built with ❤️ by <a href="https://github.com/MH4S33B">MH4S33B</a>
Powered by <a href="https://defang.io/deploy/how-to-deploy-flask/?gad_source=1&gbraid=0AAAAA9xJmWYD-jxEzePCHdb83WzHgaLJ6&gclid=CjwKCAjwk43ABhBIEiwAvvMEB2wa-UKAWF90Ev_qmcZMn-xy9AIKfEgnkgcD9uHH8Fos5HBQ0WLEfhoClDYQAvD_BwE">Flask</a> and <a href="https://en.wikipedia.org/wiki/Cryptography">cryptography</a>
Icons from <a href="https://fontawesome.com/">Font Awesome</a> and <a href="https://simpleicons.org/">Simple Icons</a>
Fonts by <a href="https://fonts.google.com/">Google Fonts</a>

## 📬 Contact
GitHub: <a href="https://github.com/MH4S33B">MH4S33B</a>
LinkedIn: <a href="https://www.linkedin.com/in/mhaseeb211/">mhaseeb211</a>
Medium: <a href="https://medium.com/@mh4s33b">mh4s33b</a>
Email: mhaseebraja2006@gmail.com
Support: <a href="https://ko-fi.com/mh4s33b">Ko-Fi</a>

⭐ Star this repository if you find SecureVault useful! Let’s make file encryption accessible and secure for everyone.
```
Let me know if you want to auto-generate badges, add GIF demos, or include setup screenshots!
```
