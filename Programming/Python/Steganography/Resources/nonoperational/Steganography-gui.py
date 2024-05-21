import sys
import datetime
import time
import os
from os.path import expanduser

from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog,messagebox
# from tkinter import messagebox

from PIL import ImageTk,Image,ImageColor
import binascii


root = Tk()
root.title('Steganography')
# root.geometry('1000x500')

def open_file():
    global my_label
    input_picture = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select the Image you would like to use")
    print(input_picture)
    my_img1 = ImageTk.PhotoImage(Image.open(input_picture))
    my_label.grid_forget()
    my_label = Label(image=my_img1, relief=SUNKEN)
    my_label.grid(row=1, column=0, rowspan=30, padx=10, pady=10)
    print(my_img1)

def save_file():
    timestr = time.strftime("%Y-%m-%d")
    savefilename = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="What would you like to save the Image as?", initialfile=("Steganography-" + timestr), defaultextension=".PNG", filetypes=((".PNG",".png"),("all files","*.*")))
    print(savefilename)
    # image.save(savefilename)

def donothing():
    x = 0

def popabout():
    messagebox.showinfo("About this program", "Created by Christopher Iwen \nThis program is free and opensource code. You can redistribute it free of charge. This software should never be sold. You are allowed to make any modifications you see fit.")

def pophelp():
    messagebox.showinfo("Help!", "https://github.com/ciwen3/Public/tree/master/python/steganography")

def popissue():
    messagebox.showerror("Error!", "There are not enough pixels to encode your message.\nTry picking a bigger picture or a shorter message.")

# the following definitions are from 
# https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

# the following definitions are from 
# https://stackoverflow.com/questions/9916334/bits-to-string-python
def bits2a(b):
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))

# encode function
def encode(pixe):
    input_text = ("#start#" +  origtext + "#end#")
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
        popissue()
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
    # image.save(output_picture)
    save_file()

# decode function
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


# Menu Bar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open Image File", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create help menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help!", command=pophelp)
helpmenu.add_command(label="About", command=popabout)
menubar.add_cascade(label="More", menu=helpmenu)

root.config(menu=menubar)


# start image
my_img1 =  ImageTk.PhotoImage(Image.open("/home/strat0m/GitHub/encryption/resources/redheart.PNG"))
my_label = Label(image=my_img1, relief=SUNKEN)
my_label.grid(row=1, column=0, rowspan=30, padx=10, pady=10)


# text box
origtext_label = Label(root, text="Message to encode:")
origtext_label.grid(row=1, column=40, padx=10, pady=10)
origtext = Text(root, height=20, relief=SUNKEN)
origtext.grid(row=2, column=40, columnspan=20, padx=10)
origtext.insert(END, "Insert you message to be hidden here.")

# add scroll bar for text widget
# scroll = root.Scrollbar(root, COMMAND=msg1.yview)
# msg1.configure(yscrollcommand=scroll.set)


# for when we want to grab the message and do something with it. 
# plaintext = origtext.get()

# for changeing the text to show it encrypted
# origtext.delete()
# origtext.insert(END, encrypted_text)


# drop down window for encryption choice
var1 = StringVar()
drop = OptionMenu(root,var1,"NONE","NONE") #,"AES","RSA")
drop.grid(row=30, column=40, padx=10, pady=10)


# button to encrypt message
crypt = Button(root, text="Encrypt", command=donothing)
crypt.grid(row=30, column=45, padx=10, pady=10)

# button to encode message in Image
code = Button(root, text="Encode", command=encode(my_img1))
code.grid(row=30, column=50, padx=10, pady=10)
# !!!!!add a popup to choose what to save the image as!!!!!

# button to decode message in Image
code = Button(root, text="Decode", command=decode(my_img1))
code.grid(row=30, column=55, padx=10, pady=10)





root.mainloop()



    # origtext = input("\nWhat text would you like to hide?\n")
    # input_picture = input("\nWhat picture would you like to hide it in?\n")
    # output_picture = input("\nWhat would you like to save the new picture as?\n")
    # input_text = ("#start#" +  origtext + "#end#")
    # encode(input_picture)