function encryptFile() {
    const fileInput = document.getElementById("fileInput");
    if (!fileInput.files.length) {
      alert("Select a file first");
      return;
    }
  
    const formData = new FormData();
    formData.append("file", fileInput.files[0]);
  
    fetch("/encrypt", { method: "POST", body: formData })
      .then(response => response.blob())
      .then(blob => {
        const a = document.createElement("a");
        a.href = window.URL.createObjectURL(blob);
        a.download = fileInput.files[0].name + ".enc";
        a.click();
        document.getElementById("status").textContent = "✅ File encrypted!";
      })
      .catch(() => {
        document.getElementById("status").textContent = "❌ Encryption failed.";
      });
  }
  
  function decryptFile() {
    const fileInput = document.getElementById("fileInput");
    if (!fileInput.files.length) {
      alert("Select a file first");
      return;
    }
  
    const formData = new FormData();
    formData.append("file", fileInput.files[0]);
  
    fetch("/decrypt", { method: "POST", body: formData })
      .then(response => response.blob())
      .then(blob => {
        const a = document.createElement("a");
        a.href = window.URL.createObjectURL(blob);
        a.download = fileInput.files[0].name.replace(".enc", "_decrypted");
        a.click();
        document.getElementById("status").textContent = "✅ File decrypted!";
      })
      .catch(() => {
        document.getElementById("status").textContent = "❌ Decryption failed.";
      });
  }
  
  function generateKey() {
    fetch("/generate-key")
      .then(() => {
        document.getElementById("status").textContent = "✅ Key generated!";
      })
      .catch(() => {
        document.getElementById("status").textContent = "❌ Key generation failed.";
      });
  }
  