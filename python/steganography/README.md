# This project is offered “as-is”, without warranty, and disclaiming liability for damages resulting from using this project.


# Is Steganography Encryption?
I know technically Steganography is not encryption but I couldn't think of a better word to use for the option to hide text or retrieve text at 3am. I am open to suggestions.
For best protection all text to should be encrypted before entering it into this program. This program won't truly encrypt anything, it just obscures the data from obvious viewing. 


# Requirements:
1. Pillow (PIL) for Python
2. binascii


# Use:
1. Run program
2. Type E or Encrypt to add text to a picture OR Type D or Decrypt to pull text from a picture
3. Input options (ie. text to hide, output photo and/or input photo)
4. Get Photo with hidden message when Encryopting OR get hidden message from photo when Decrypting. 


# Example Encrypt:
1. Run program
2. Encrypt
3. text input = Hello World!
4. input image = ./resources/HelloWorldBlank.PNG
5. output image = ./resources/HelloWorldEncrypted.PNG


# Example Decrypt:
1. Run program
2. Decrypt
3. ./resources/HelloWorldEncrypted.PNG
4. prints out message: Hello World!


# To Do:
1. add check to make sure message will fit in the number of pixel found in the picture
2. add begining and end notifiers for text
3. add option to create picture from scratch (possible just a solid color)?? (still debating)
4. make graphical interface using Tkinter


# Troubleshooting
if you get an error about indentation use untabify to change all tabs to 4 spaces. 
(I am bad about mixing spaces and tabs, and have to run untabify to fix problems occationally.)
Good Luck!
