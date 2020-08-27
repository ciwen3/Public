# This project is offered “as-is”, without warranty, and disclaiming liability for damages resulting from using this project.


# Requirements:
1. Python 3 (check in a terminal by running: python --version)
2. Pillow (PIL) for Python

## Install Python:
1. Debian based Linux: sudo apt install python3.8
2. Fedora based Linux: sudo yum install python3.8
3. Windows https://www.python.org/downloads/windows/

## Install pip3:
1. Debian based Linux: sudo apt install python3-pip 
2. Fedora based Linux: sudo yum install python3-pip 

## Install Pillow with pip (all OS's): taken from https://pillow.readthedocs.io/en/stable/installation.html
1. python3 -m pip install --upgrade pip
2. python3 -m pip install --upgrade Pillow
### or
3. python -m pip install --upgrade pip
4. python -m pip install --upgrade Pillow


# Use:
1. Run program
2. Type E or Encode to add text to a picture OR Type D or Decode to pull text from a picture
3. Input options (ie. text to hide, output photo and/or input photo)
4. Get Photo with hidden message when Encoding OR get hidden message from photo when Decoding. 


# Example Encode:
1. Run program
2. Encode
3. text input = Hello World!
4. input image = ./resources/HelloWorldBlank.PNG
5. output image = ./resources/HelloWorldEncoded.PNG


# Example Decode:
1. Run program
2. Decode
3. ./resources/HelloWorldEncoded.PNG
4. prints out message: Hello World!


# To Do:
1. add check to make sure message will fit in the number of pixel found in the picture
2. add begining and end notifiers for text, only display the output from between the notifiers to clear up the output
3. make graphical interface using Tkinter
4. add encryption modules 
5. add option to create picture from scratch (possibly just a solid color)?? (still debating)


# Troubleshooting
if you get an error about indentation use untabify to change all tabs to 4 spaces. 
(I am bad about mixing spaces and tabs, and have to run untabify to fix problems occationally.)
Good Luck!
