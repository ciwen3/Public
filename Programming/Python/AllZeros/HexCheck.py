#!/usr/bin/env python3

import binascii

def print_hex_code(file_path):
    with open(file_path, "rb") as file:
        # Read the file in binary mode
        data = file.read()
        # Convert the binary data to hexadecimal representation
        hex_data = binascii.hexlify(data)
        # Print the hexadecimal data
        print(hex_data)

# Ask the user for the file path
file_path = input("Enter the path to the file you want to examine: ")

# Examine the file
print_hex_code(file_path)
