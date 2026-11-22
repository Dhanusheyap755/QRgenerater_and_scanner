"""
QR Generator & Scanner Utility
Author: Dhanusheya P
A clean CLI utility to generate customized QR codes and decode QR code data from image files.
"""

import sys
import argparse

def generate_qr(data: str, output_path: str = "qrcode.png"):
    try:
        import qrcode
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(output_path)
        print(f"✅ QR Code generated successfully: {output_path}")
    except ImportError:
        print("❌ 'qrcode' library not found. Run: pip install qrcode[pil]")

def scan_qr(image_path: str):
    try:
        import cv2
        img = cv2.imread(image_path)
        if img is None:
            print(f"❌ Failed to load image: {image_path}")
            return
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            print(f"✅ Decoded QR Data: {data}")
        else:
            print("⚠️ No QR code detected in image.")
    except ImportError:
        print("❌ 'opencv-python' not found. Run: pip install opencv-python")

def main():
    parser = argparse.ArgumentParser(description="Generate and Scan QR Codes")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    gen_parser = subparsers.add_parser("generate", help="Generate a QR code image")
    gen_parser.add_argument("data", type=str, help="Text or URL to encode in QR")
    gen_parser.add_argument("-o", "--output", type=str, default="qrcode.png", help="Output file path (default: qrcode.png)")

    scan_parser = subparsers.add_parser("scan", help="Scan a QR code from an image")
    scan_parser.add_argument("image", type=str, help="Path to image file to scan")

    args = parser.parse_args()
    if args.command == "generate":
        generate_qr(args.data, args.output)
    elif args.command == "scan":
        scan_qr(args.image)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
