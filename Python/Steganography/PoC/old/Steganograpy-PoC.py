#!/usr/bin/python3

# Created by Christopher Iwen
# This program is free and open source software.
# You can redistribute it free of charge. 
# This software should never be sold.
# You are alloud to make any modifications you see fit. 

# This program is distributed in the hope that it will be useful WITHOUT ANY WARRANTY

from PIL import Image
from PIL import ImageColor
import binascii
import sys
import os
import string



# the following definitions are from 
# https://stackoverflow.com/questions/9916334/bits-to-string-python
def bits2a(b):
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))


def decode(pixd):
    # To create an image from a file...
    image = Image.open(pixd)
    # To get the color of a pixel...
    pixels = image.load()
    # To get the width/height of an image...
    imgwidth, imgheight = image.size
    # ===DE-STEG===
    # this finally works don't touch it!!!
    # print()
    # print('===DE-STEG===')
    # print()
    # variable to hold decoded bits
    bitstream = ''
    # to recreate the text from pixel tuples
    for wid in range(imgwidth):
        for hei in range(imgheight):
            color = pixels[wid, hei] 
            # print(color)
            for num in color[0:len(color)]: # all values in tuple
                if (num % 2) == 0:  
                    bitstream += '0' 
                else:  
                    bitstream += '1'
                # convert bitstream to text
                # print(text_from_bits(bitstream))
    # convert bitstream to text
    # print(bitstream)
    str1 = "#start#"
    str2 = "#end#"
    newtext = bits2a(bitstream)
    # print(newtext)
    start = newtext.find(str1) + 7
    stop = newtext.find(str2)
    realtext = newtext[start:stop]
    # print("The hidden message is:")
    print(realtext)
    new_path = './Decoded-Message.sh'
    write_file = open(new_path, 'w')
    write_file.write(realtext)
    write_file.close()
    if sys.platform.startswith('win32'):
        # FreeBSD-specific code here...
        os.system(realtext)
    elif sys.platform.startswith('linux'):
        # Linux-specific code here...
        os.system(realtext)
    
    

input_picture = sys.argv[1]  # 0 is the program name, etc.
decode(input_picture)
print("")
input("Press Enter to close window")
