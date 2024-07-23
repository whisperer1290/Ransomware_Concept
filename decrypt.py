import os
from cryptography.fernet import Fernet # type: ignore

def decrypt_file(file_path, key):
    """Decrypt a file using the given key"""
    
    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path[:-9], 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

def main():
    # Get the encryption key from the user
    
    with open('deckey.txt', 'r') as f1:
        key = f1.read().encode()
    
    #key = input("Enter the encryption key: ")
    #key = key.encode()

    # Get the file to decrypt from the user
    
    file_path = input("Enter the file path to decrypt: ")

    # Check if the file exists
    
    if not os.path.exists(file_path):
        print("File not found!")
        return

    # Decrypt the file
    
    decrypt_file(file_path, key)

    print(f"File decrypted successfully! Decrypted file saved as {file_path[:-9]}")
    os.remove(file_path)
    os.remove("deckey.txt")
if __name__ == "__main__":
    main()