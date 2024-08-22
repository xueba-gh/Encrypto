import streamlit as st
from cryptography.fernet import Fernet, InvalidToken # type: ignore
import base64
import os

def generate_key():
    return Fernet.generate_key()

def validate_key(key):
    try:
        if len(base64.urlsafe_b64decode(key)) != 32:
            raise ValueError("Invalid key length")
        return key.encode() if isinstance(key, str) else key
    except:
        raise ValueError("Invalid key format")

def encrypt_file(file_bytes, key, file_type):
    f = Fernet(key)
    encrypted_data = f.encrypt(file_bytes)
    return file_type.encode() + b"|" + encrypted_data

def decrypt_file(encrypted_data, key):
    try:
        file_type, data = encrypted_data.split(b"|", 1)
        f = Fernet(key)
        decrypted_data = f.decrypt(data)
        return file_type.decode(), decrypted_data
    except ValueError:
        raise ValueError("Invalid file format")
    except InvalidToken:
        raise InvalidToken("Invalid decryption key")

st.title("Simple Document Encryption")

tab1, tab2 = st.tabs(["Encrypt", "Decrypt"])

with tab1:
    st.header("Encrypt Your Document")
    uploaded_file = st.file_uploader("Choose a file to encrypt", type=['docx', 'doc', 'pdf', 'txt'])
    encryption_key = st.text_input("Enter an encryption key (leave blank to generate one)", type="password")

    if uploaded_file is not None:
        if st.button("Encrypt"):
            file_bytes = uploaded_file.getvalue()
            file_type = uploaded_file.type
            try:
                if not encryption_key:
                    encryption_key = generate_key()
                    st.warning("Generated encryption key. Please save it securely:")
                    st.code(encryption_key.decode())
                else:
                    encryption_key = validate_key(encryption_key)
                
                encrypted_data = encrypt_file(file_bytes, encryption_key, file_type)
                
                file_name, file_extension = os.path.splitext(uploaded_file.name)
                encrypted_file_name = f"{file_name}.encrypted"
                
                st.download_button(
                    label="Download Encrypted File",
                    data=encrypted_data,
                    file_name=encrypted_file_name,
                    mime="application/octet-stream"
                )
                st.info(f"File encrypted and saved as {encrypted_file_name}")
            except ValueError as e:
                st.error(f"Encryption failed: {str(e)}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")

with tab2:
    st.header("Decrypt Your Document")
    encrypted_file = st.file_uploader("Choose an encrypted file", type=None)
    decryption_key = st.text_input("Enter the decryption key", type="password")

    if encrypted_file is not None and decryption_key:
        if st.button("Decrypt"):
            try:
                file_bytes = encrypted_file.getvalue()
                decryption_key = validate_key(decryption_key)
                
                file_type, decrypted_data = decrypt_file(file_bytes, decryption_key)
                
                original_file_name = encrypted_file.name
                if original_file_name.endswith('.encrypted'):
                    original_file_name = original_file_name[:-10]
                
                st.download_button(
                    label="Download Decrypted File",
                    data=decrypted_data,
                    file_name=original_file_name,
                    mime=file_type
                )
                st.success(f"File decrypted successfully. Save as {original_file_name}")
                
                # Preview for text files only
                if file_type.startswith('text/'):
                    st.text_area("Preview of decrypted content:", decrypted_data.decode(), height=300)
                else:
                    st.info("File decrypted. Please download to view.")
                
            except InvalidToken:
                st.error("Decryption failed: Invalid token. This usually means the key is incorrect.")
            except ValueError as e:
                st.error(f"Decryption failed: {str(e)}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")
            
            # Debugging information (consider removing in production)
            st.write("Debugging Info:")
            st.write(f"File name: {encrypted_file.name}")
            st.write(f"File size: {len(file_bytes)} bytes")

st.sidebar.markdown("""
## How to use this app

1. **To encrypt:**
   - Upload your document (docx, doc, pdf, or txt)
   - Enter an encryption key or leave blank to generate one
   - Click 'Encrypt' and download the encrypted file
   - The file will be saved with a '.encrypted' extension
   - Save the encryption key securely

2. **To decrypt:**
   - Upload the encrypted file
   - Enter the correct decryption key
   - Click 'Decrypt' and download the original file

**Note:** Keep your encryption key safe. Without the correct key, you won't be able to decrypt your file!
""")