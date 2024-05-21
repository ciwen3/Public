from Crypto.Cipher import AES

# Encrypt the file using the given password
def encrypt_file(file_path, password):
    # Read the file data
    with open(file_path, "rb") as file:
        file_data = file.read()

    # Generate a random 16-byte IV
    iv = os.urandom(16)

    # Derive the encryption key from the password
    key = PBKDF2(password, salt).read(32)

    # Encrypt the file data using AES-256 in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = iv + cipher.encrypt(file_data)

    # Write the encrypted data to the output file
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

# Decrypt the file using the given password
def decrypt_file(file_path, password):
    # Read the encrypted file data
    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    # Derive the encryption key from the password
    key = PBKDF2(password, salt).read(32)

    # Decrypt the file data using AES-256 in CBC mode
    iv = encrypted_data[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data[16:])

    # Write the decrypted data to the output file
    with open(file_path, "wb") as file:
        file.write(decrypted_data)
