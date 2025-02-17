# 🔒 Image Steganography using OpenCV

This project allows you to **hide and retrieve secret messages** within an image using **Python & OpenCV**. The encryption process modifies the pixel values of the image to store the message securely, which can later be decrypted using the correct passcode.

---

## 📌 Features
✅ Encrypt text into an image without noticeable changes.  
✅ Secure decryption with a passcode.  
✅ Stores message length for accurate extraction.  
✅ Uses OpenCV for image manipulation.  
✅ Works with **any image format** (JPG, PNG, etc.).

---

## 🛠️ Setup & Installation

### ** Install Dependencies**
Ensure you have **Python 3.x** installed, then run:
```bash
pip install opencv-python
```

---

## 🔹 Usage
### **🔐 Encrypt a Message**
1. Place your image in the project folder (e.g., `mypic.jpg`).
2. Run the encryption script:
   ```bash
   python encrypt.py
   ```
3. Enter your **secret message** and **passcode**.
4. The encrypted image (`encryptedImage.jpg`) will be generated.

### **🔓 Decrypt a Message**
1. Run the decryption script:
   ```bash
   python decrypt.py
   ```
2. Enter the **correct passcode**.
3. The **hidden message** will be displayed.

---

## 📁 Project Structure
```
image-steganography/
│── encrypt.py            # Encryption script
│── decrypt.py            # Decryption script
│── key.txt               # Stores passcode (generated during encryption)
│── mypic.jpg             # Original image
│── encryptedImage.jpg    # Encrypted image (generated output)
│── README.md             # Project documentation
```

---

## 📷 Example
```
Enter secret message: Hello, World!
Enter a passcode: 1234
Encryption complete. Image saved as 'encryptedImage.jpg'.
```
```
Enter passcode for decryption: 1234
Decrypted message: Hello, World!
```

---

## 🛠️ Future Improvements
🔹 Improve encryption security using cryptographic methods.  
🔹 Add a GUI for easier interaction.  
🔹 Support for different image formats.  

---

## 📜 License
This project is **open-source** under the MIT License.

---

## 🤝 Contributing
Pull requests are welcome! If you find any bugs or have suggestions, feel free to open an **issue**.

🚀 **Happy Coding!**

