import tkinter as tk

def caesar_cipher(plaintext, key):
    # Create a mapping of the alphabet to itself shifted by the key
    shifted_alphabet = {chr(i): chr((i + key - 65) % 26 + 65) for i in range(65, 91)}  # Uppercase
    shifted_alphabet.update({chr(i): chr((i + key - 97) % 26 + 97) for i in range(97, 123)})  # Lowercase

    # Use the mapping to transform the plaintext into the ciphertext
    ciphertext = ''
    for ch in plaintext:
        if ch.isalpha():
            ciphertext += shifted_alphabet[ch]
        else:
            ciphertext += ch
    return ciphertext

def encrypt():
    # Get the plaintext and key from the user input
    plaintext = plaintext_entry.get()
    key = int(key_entry.get())

    # Encrypt the plaintext using the Caesar cipher
    ciphertext = caesar_cipher(plaintext, key)

    # Display the ciphertext in the output label
    output_label['text'] = ciphertext

def decrypt():
    # Get the ciphertext and key from the user input
    ciphertext = plaintext_entry.get()
    key = int(key_entry.get())

    # Decrypt the ciphertext using the Caesar cipher
    plaintext = caesar_cipher(ciphertext, -key)

    # Display the plaintext in the output label
    output_label['text'] = plaintext

# Create the main window
window = tk.Tk()
window.title('Caesar Cipher')

# Create the input fields for the plaintext and key
plaintext_label = tk.Label(text='Plaintext:')
plaintext_entry = tk.Entry()
key_label = tk.Label(text='Key:')
key_entry = tk.Entry()

# Create the buttons to encrypt and decrypt the text
encrypt_button = tk.Button(text='Encrypt', command=encrypt)
decrypt_button = tk.Button(text='Decrypt', command=decrypt)

# Create the label to display the output
output_label = tk.Label(text='')

# Add all of the widgets to the window
plaintext_label.pack()
plaintext_entry.pack()
key_label.pack()
key_entry.pack()
encrypt_button.pack()
decrypt_button.pack()
output_label.pack()

# Run the main loop
window.mainloop()
