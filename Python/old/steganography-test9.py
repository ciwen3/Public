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

# the following definitions are from 
# https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

# the following definitions are from 
# https://stackoverflow.com/questions/9916334/bits-to-string-python
def bits2a(b):
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))


# might not need
# def save():
#     image.save(output_picture)


def encode(pixe):
    # print(text_to_bits(origtext))
    # create variable to hold message as bits
    bits = text_to_bits(input_text)
    # print(bits)
    # To create an image from a file...
    image = Image.open(pixe)
    # For easy and direct pixel editing...
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    # To get the color of a pixel...
    pixels = image.load()
    # To get the width/height of an image...
    imgwidth, imgheight = image.size
    # check to make sure that the message will fit in the picture
    pixcheck = int(imgwidth * imgheight / 2)
    bitcheck = len(bits)
    if pixcheck < bitcheck:
        print("")
        print("*****************************************************")
        print("*There are not enough pixels to encode your message.*")
        print("*Try picking a bigger picture or a shorter message. *")
        print("*****************************************************")
        print("")
    else:
        # ======Steg=====
        # this finally works don't touch it!!!
        # For each pixel
        for wid in range(imgwidth):            # loop through every width option
            for hei in range(imgheight):    # loop through every height option
                color = pixels[wid, hei]    # grab tuple for that pixel
                # print(color)                # sanity check
                temppix = []                # Empty List
                # print(temppix)
                if bits == "":
                    break
                else:
                    for num in color[0:4]: # for each values in tuple
                        # print(num)
                        if (num % 2) == 0:          # check if number from pixel tuple is even
                            # print("pixel is even: " + str(num))
                            if (int(bits[0]) % 2) == 0:
                                # print("bit[0] is even: " + str(bits[0]))
                                # print("No change needed")
                                temppix.append(num)
                                # print(temppix)
                                # print(bits)
                                bits = bits[1:len(bits)]    # if both even no change needed, shorten by 1 bit
                                # print(bits)                 # sanity check
                            else:                       # pixel and bit are not both even
                                # print("bit[0] is odd: " + str(bits[0]))
                                # print("Change needed adding one")
                                temppix.append(num +1)
                                # print(temppix)
                                bits = bits[1:len(bits)]
                                # print(bits)
                        else:
                            # print("pixel is odd: " + str(num))
                            if (int(bits[0]) % 2) == 0:
                                # print("bit[0] is even: " + str(bits[0]))
                                # print("Change needed")
                                if num == 255:
                                    # print("num is 255: " + str(num))
                                    # print("minus one")
                                    temppix.append(num -1)
                                    # print(temppix)
                                    # print(bits)
                                    bits = bits[1:len(bits)]  
                                    # print(bits)
                                else:
                                    # print("num is less than 255: " + str(num))
                                    # print("add one")
                                    temppix.append(num +1)
                                    # print(temppix)
                                    # print(bits)
                                    bits = bits[1:len(bits)]  
                                    # print(bits)
                            else:
                                # print("Both pixel and bit are odd")
                                # print("no change needed")
                                temppix.append(num)
                                # print(temppix)
                                # print(bits)
                                bits = bits[1:len(bits)]
                                # print(bits) 
                    # print(temppix)
                    pixels[wid, hei] = tuple(temppix)
                    # print(pixels[wid, hei])
    image.save(output_picture)


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
    print("The hidden message is:")
    print(realtext)


    # take in original text and change it from ASCII to bits
print("Usage: To Hide Message in digital image")
print("Type Encode to add hidden text to a digital image")
print("Then type in your message. \nIf you want it to be truly secure then enter an already encrypted message.")
print("Then type the file path and name of the image you want to add the message to.")
print("Then type the file path and name that you want the new image to be saved as.")
print("Wait for it to finish and check to see if the new image was created.")
print("")
print("Usage: To Retrieve Message from digital image")
print("Type Decode to get hidden text from a digital image")
print("Then type the file path and name of the image you want to extract the message from.")
print("Wait for it to finish and check the output. \n")
print("")

ask = input("Do you want to (E)ncode or (D)ecode?\n")
if ask.upper() == "E" or ask.upper() == "ENCODE":
    origtext = input("\nWhat text would you like to hide?\n")
    input_picture = input("\nWhat picture would you like to hide it in?\n")
    output_picture = input("\nWhat would you like to save the new picture as?\n")
    input_text = ("#start#" +  origtext + "#end#")
    encode(input_picture)
elif ask.upper() == "D" or ask.upper() == "DECODE":
    input_picture = input("\nWhat picture would you like to get text from?\n")
    # To create an image from a file...
    decode(input_picture)
else:
    print("")
    print("That was not an option, maybe you misspelled it.")
    print("You should try again.")
    print("")
    print("Usage: To Hide Message in digital image")
    print("Type Encode to add hidden text to a digital image")
    print("Then type in your message. \nIf you want it to be truly secure then enter an already encrypted message.")
    print("Then type the file path and name of the image you want to add the message to.")
    print("Then type the file path and name that you want the new image to be saved as.")
    print("Wait for it to finish and check to see if the new image was created.")
    print("")
    print("Usage: To Retrieve Message from digital image")
    print("Type Decode to get hidden text from a digital image")
    print("Then type the file path and name of the image you want to extract the message from.")
    print("Wait for it to finish and check the output. \n")
    print("")

print("")
input("Press Enter to close window")
