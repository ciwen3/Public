#!/usr/bin/env python3

from PIL import Image
from PIL import ImageColor
import binascii
import argparse

def file_to_bits(path1):
    with open(path1, "rb") as file1:
        number = file1.read()
    bits = bin(int(binascii.hexlify(number), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')

def encode(bits, pixe, output_path):
    image = Image.open(pixe)
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    pixels = image.load()
    imgwidth, imgheight = image.size
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
        for wid in range(imgwidth):
            for hei in range(imgheight):
                color = pixels[wid, hei]
                temppix = []
                if bits == "":
                    break
                else:
                    for num in color[0:4]:
                        if (num % 2) == 0:
                            if (int(bits[0]) % 2) == 0:
                                temppix.append(num)
                                bits = bits[1:len(bits)]
                            else:
                                temppix.append(num + 1)
                                bits = bits[1:len(bits)]
                        else:
                            if (int(bits[0]) % 2) == 0:
                                temppix.append(num - 1)
                                bits = bits[1:len(bits)]
                            else:
                                temppix.append(num)
                                bits = bits[1:len(bits)]
                    temppix.append(color[3])
                    pixels[wid, hei] = tuple(temppix[0:4])
        image.save(output_path)

def decode(pixe):
    image = Image.open(pixe)
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    pixels = image.load()
    imgwidth, imgheight = image.size
    bits = ""
    for wid in range(imgwidth):
        for hei in range(imgheight):
            color = pixels[wid, hei]
            temppix = []
            for num in color[0:3]:
                if (num % 2) == 0:
                    temppix.append(0)
                else:
                    temppix.append(1)
            for bit in temppix:
                bits += str(bit)
    return bitstring_to_bytes(bits)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", choices=["encode", "decode"], help="the mode to run the script in")
    parser.add_argument("-f", "--file", help="the file to encode/decode")
    parser.add_argument("-i", "--image", help="the image to encode/decode from")
    parser.add_argument("-o", "--output", help="the output path for the encoded image")
    args = parser.parse_args()

    if args.mode == "encode":
        bits = file_to_bits(args.file)
        encode(bits, args.image, args.output)
    elif args.mode == "decode":
        decoded_file = decode(args.image)
        with open(args.output, "wb") as f:
            f.write(decoded_file)
