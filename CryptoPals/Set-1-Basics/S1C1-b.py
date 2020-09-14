
# https://cryptopals.com/sets/1/challenges/1
# Convert hex to base64
# The string:

# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# Should produce:

# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
# So go ahead and make that happen. You'll need to use this code for the rest of the exercises.

# Cryptopals Rule
# Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.


import binascii
import base64
# ask for hex to convert to base64
print("CryptoPals Set 1: Challenge 1")
print("Convert hex to base64")
print("")
new_hex = input('Input the hex string you would like to convert to base64?\n')
# print(new_hex)

def convert(hex):
    # make function to take raw bytes and convert hex to base64
    raw_bytes = binascii.unhexlify(hex)

    # Base64 encode the raw bytes
    base = base64.b64encode(raw_bytes, altchars=None)
    print("")
    print("Your Base64 encoded output is:")
    print(base)

convert(new_hex)