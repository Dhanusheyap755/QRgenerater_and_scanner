# QR Code Generator & Scanner Utility

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=flat&logo=opencv&logoColor=white)](https://opencv.org/)

## 📌 Project Overview
A lightweight, versatile **Python CLI utility** for generating custom QR code images and decoding QR data from image files using **OpenCV** and the `qrcode` library.

---

## 🚀 Key Features
- **Instant QR Generation:** Encodes text, contact details, Wi-Fi credentials, or URLs into high-contrast PNG images.
- **Computer Vision Scanning:** Decodes QR codes from image inputs using OpenCV's `QRCodeDetector`.
- **Command-Line Interface:** Intuitive subcommands (`generate` and `scan`).

---

## 📂 Project Folder Structure
```
qr-generator-and-scanner/
├── .gitignore
├── README.md
├── qr_tool.py             # Core CLI utility
└── requirements.txt       # Dependencies
```

---

## 💻 Installation & Usage

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Generate a QR code
python qr_tool.py generate "https://github.com/Dhanusheyap755" -o my_qr.png

# 3. Scan a QR code image
python qr_tool.py scan my_qr.png
```
