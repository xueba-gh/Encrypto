# File Encryption App

## Live Demo
The app is live and can be accessed at: [https://file-encrypto.streamlit.app/](https://file-encrypto.streamlit.app/)

## Description
This Streamlit-based web application provides a simple and secure way to encrypt and decrypt files. It uses the Fernet symmetric encryption scheme from the cryptography library to ensure the confidentiality of your files.

## Features
- File encryption: Upload any file and encrypt it with a secure key
- File decryption: Decrypt previously encrypted files using the correct key
- Key generation: Automatically generate secure encryption keys
- Supports various file types: .docx, .doc, .pdf, .txt, and more
- User-friendly interface: Easy-to-use tabs for encryption and decryption

## How to Use

### Encryption
1. Navigate to the "Encrypt" tab
2. Upload the file you want to encrypt
3. Enter an encryption key or leave it blank to generate one automatically
4. Click the "Encrypt" button
5. Download the encrypted file

### Decryption
1. Navigate to the "Decrypt" tab
2. Upload the encrypted file
3. Enter the correct decryption key
4. Click the "Decrypt" button
5. Download the decrypted file

## Installation for Local Development

To run this app locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/xueba-gh/Encrypto
   cd Encrypto
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```
   streamlit run encrypto.py
   ```

5. Open your web browser and go to `http://localhost:8501`

## Dependencies
- streamlit
- cryptography

## Security Considerations
- Keep your encryption key secure. Without the correct key, encrypted files cannot be decrypted.
- This app uses client-side encryption. Your files and keys are not stored on any server.
- For highly sensitive data, consider additional security measures.

## Contributing
Contributions to improve the app are welcome.
@Xueba
