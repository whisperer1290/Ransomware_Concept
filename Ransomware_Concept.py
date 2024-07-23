import encrypt
import decrypt

print("This is a simple concept and demo application for how ransomware works.")
print("This application is NOT intended to be used for malicious purposes.")
print("This program encrypts a file and creates a decryption key file which contains decryption key to your encrypted file so be careful while deleting that file.")
print("I am not responsible for any loss of data or permanent encryption of files in case of deletion of decryption key by the user.")

ch = int(input("Choose an option by typing the number preceeding it:\n1) File encryption\n2)File decryption\n3)Exit\nYour Choice: "))

while ch!=3:
    if ch==1:
        encrypt.main()
    elif ch==2:
        decrypt.main()
    ch = int(input("Choose an option by typing the number preceeding it:\n1) File encryption\n2)File decryption\n3)Exit\nYour Choice: "))