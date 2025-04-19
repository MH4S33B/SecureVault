function showProgress() {
  progressBar.classList.add("active");
  progress.style.width = "0";
  setTimeout(() => {
    progress.style.width = "100%";
  }, 100);
}

function showToast(msg) {
  toast.textContent = msg;
  toast.classList.add("show");
  setTimeout(() => {
    toast.classList.remove("show");
  }, 3000);
}

function copyKey() {
  navigator.clipboard.writeText(document.getElementById("generatedKey").textContent);
  showToast("Key copied to clipboard!");
}

function encryptFile() {
  const fileInput = document.getElementById("fileInput");
  if (!fileInput.files.length) {
    alert("Select a file first");
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  showProgress();
  document.getElementById("message").textContent = "Encrypting file...";

  fetch("/encrypt", { method: "POST", body: formData })
    .then(response => {
      if (!response.ok) {
        return response.json().then(err => { throw new Error(err.error || "Encryption failed"); });
      }
      return response.blob();
    })
    .then(blob => {
      const a = document.createElement("a");
      a.href = window.URL.createObjectURL(blob);
      a.download = fileInput.files[0].name + ".enc";
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      document.getElementById("message").textContent = "File encrypted successfully!";
      showToast("Encryption complete! File downloaded.");
    })
    .catch(error => {
      document.getElementById("message").textContent = `❌ ${error.message}`;
      showToast(error.message);
    })
    .finally(() => {
      progressBar.classList.remove("active");
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

  showProgress();
  document.getElementById("message").textContent = "Decrypting file...";

  fetch("/decrypt", { method: "POST", body: formData })
    .then(response => {
      if (!response.ok) {
        return response.json().then(err => { throw new Error(err.error || "Decryption failed"); });
      }
      return response.blob();
    })
    .then(blob => {
      const a = document.createElement("a");
      a.href = window.URL.createObjectURL(blob);
      a.download = fileInput.files[0].name.replace(".enc", "_decrypted");
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      document.getElementById("message").textContent = "File decrypted successfully!";
      showToast("Decryption complete! File downloaded.");
    })
    .catch(error => {
      document.getElementById("message").textContent = `❌ ${error.message}`;
      showToast(error.message);
    })
    .finally(() => {
      progressBar.classList.remove("active");
    });
}

function generateKey() {
  fetch("/generate-key")
    .then(response => {
      if (!response.ok) {
        return response.json().then(err => { throw new Error(err.error || "Key generation failed"); });
      }
      return response.json();
    })
    .then(data => {
      document.getElementById("generatedKey").textContent = data.key;
      document.getElementById("keyOutput").style.display = "flex";
      document.getElementById("message").textContent = "✅ Key generated!";
      showToast("Key generated! Click to copy.");
    })
    .catch(error => {
      console.error("Error:", error);
      document.getElementById("message").textContent = `❌ ${error.message}`;
      showToast(error.message);
    });
}
