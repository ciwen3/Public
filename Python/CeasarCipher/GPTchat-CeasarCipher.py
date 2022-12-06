#!/usr/bin/python3

import string

def main():
    # define the alphabet
    alphabet = string.ascii_lowercase

    # initialize the new message
    new_message = ''

    # ask the user whether they want to encrypt or decrypt
    action = int(input('Do you want to Encrypt or Decrypt? \n 1 for Encrypt \n 2 for Decrypt \n 3 to Close the Program \n'))

    if action == 1:
        # encrypt the message
        offset = int(input('Choose cipher offset: '))
        if abs(offset) > len(alphabet):
            print('Error: offset must be an integer between -26 and 26')
            return

        message = input('Please enter a message to encrypt: ').lower()
        for character in message:
            if character in alphabet:
                position = alphabet.find(character)
                new_position = (position + offset) % 26
                new_character = alphabet[new_position]
                new_message += new_character
            else:
                new_message += character

        print('The encrypted message is: ', new_message)
        input('Press Enter to Close Window')
    elif action == 2:
        # decrypt the message
        offset = - int(input('Choose cipher offset: '))
        if abs(offset) > len(alphabet):
            print('Error: offset must be an integer between -26 and 26')
            return

        message = input('Please enter a message to decrypt: ').lower()
        for character in message:
            if character in alphabet:
                position = alphabet.find(character)
                new_position = (position + offset) % 26
                new_character = alphabet[new_position]
                new_message += new_character
            else:
                new_message += character

        print('The decrypted message is: ', new_message)
        input('Press Enter to Close Window')
    else:
        raise SystemExit

if __name__ == '__main__':
    main()
