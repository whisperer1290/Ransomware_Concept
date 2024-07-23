import os
import secrets
from cryptography.fernet import Fernet # type: ignore

def generate_key():
    """Generate a random encryption key"""
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    """Encrypt a file using the given key"""
    
    with open(file_path, 'rb') as file:
        file_data = file.read()
    f = Fernet(key)
    encrypted_data = f.encrypt(file_data)
    with open(file_path + '.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

def main():
    # Get the file to encrypt from the user
    
    file_path = input("Enter the file path to encrypt: ")

    # Check if the file exists
    
    if not os.path.exists(file_path):
        print("File not found!")
        return

    # Generate a random encryption key
    
    key = generate_key()
    with open('deckey.txt', 'a+') as f1:
        f1.write(key.decode())

    # Encrypt the file
    
    encrypt_file(file_path, key)
    #print(f"Generated key: {key.decode()}")
    print(f"File encrypted successfully! Encrypted file saved as {file_path}.encrypted")
    os.remove(file_path)

#if __name__ == "__main__":
#    main()