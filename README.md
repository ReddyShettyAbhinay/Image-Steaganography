# Secure Data Hiding in Image Using Steganography

## Project Overview
This project is a Python-based application that implements steganography to securely hide sensitive data within digital images. By utilizing the Least Significant Bit (LSB) insertion technique combined with strong encryption, this tool enables covert communication while maintaining the integrity of the original image.

## Features
- Enhanced Security: Combines steganography with AES-256 encryption for increased data protection.
- Intuitive GUI: A streamlined, user-friendly interface makes the encoding and decoding process easy.
- Tamper Detection: Includes a mechanism to detect if the image has been altered, potentially corrupting the hidden message.
- Secure Data Hiding: Employs LSB insertion for imperceptible data embedding, ensuring hidden messages remain undetectable to the naked eye.

## Technologies Used
- Python 3: Programming language used for development.
- Pillow: Library for image processing.
- Tkinter: Library for creating the graphical user interface (GUI).
- Cryptography: Library for implementing encryption algorithms.

## Installation
1. Clone the repository: git clone https://github.com/ReddyShettyAbhinay/Image-Steganography.git
2. Navigate to the project directory
3. Install the required libraries


## Usage
1. Run the application: python steg.py
2. Use the "Encode" tab to select an image and enter a secret message to hide within it.
3. Use the "Decode" tab to retrieve hidden messages from encoded images.

