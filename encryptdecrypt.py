from cryptography.fernet import Fernet

#generating a key
def generate_key():
    return Fernet.generate_key()

#function to save the key into a file
def save_key(key, filename="secret.key"):
    with open(filename, "wb") as key_file:
        key_file.write(key)

#loading the key from the file
def load_key(filename="secret.key"):
    with open(filename, "rb") as key_file:
        return key_file.read()

#function for encryption
def encrypt_file(file_name, key):
    f = Fernet(key)
    
    with open(file_name, "rb") as file:
        file_data = file.read()
    
    
    print("Original Data:")
    print(file_data)  #preview
    
    encrypted_data = f.encrypt(file_data)

    with open(file_name + ".enc", "wb") as enc_file:
        enc_file.write(encrypted_data)
    
    #encrypted
    print("\nEncrypted Data :")
    print(encrypted_data)  #preview
    
    print(f"\nFile {file_name} encrypted successfully!")

    return encrypted_data

#function for decryption
def decrypt_file(encrypted_file, key):
    f = Fernet(key)

    with open(encrypted_file, "rb") as enc_file:
        encrypted_data = enc_file.read()

    
    print("\nEncrypted Data:")
    print(encrypted_data)  # Print content

    decrypted_data = f.decrypt(encrypted_data)

    
    print("\nDecrypted Data (first 100 bytes):")
    print(decrypted_data)  # Print content

    with open(encrypted_file[:-4], "wb") as dec_file:
        dec_file.write(decrypted_data)

    print(f"\nFile {encrypted_file} decrypted successfully!")

if __name__ == "__main__":
    #Generate and save the key
    key = generate_key()
    print("Generated Key:")
    print(key)  #generated encryption key
    save_key(key)
    
    #Encrypt a file 
    encrypted_data = encrypt_file("my_file.txt", key)
    
    #Decrypt the file 
    decrypt_file("my_file.txt.enc", key)
