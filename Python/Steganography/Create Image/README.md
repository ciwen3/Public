# Steganography 
## This version of the program is capable of creating a PNG Image big enough to fit the Text in. It is hard coded to one color. 

This Steganography program was created to hide or encode a message in a PNG image by manipulating the pixel data and to retrieve or decode the message from an image made with this program. 

## This project is offered “as-is”, without warranty, and disclaiming liability for damages resulting from using this project.

**The project is under development, any suggestion is welcome!**

![Screenshot](https://img.shields.io/badge/Platform-Universal-brightgreen)
![Screenshot](https://img.shields.io/badge/Language-Python3-blue)

## Requirements:
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
1. python -m pip install --upgrade pip
2. python -m pip install --upgrade Pillow
## Install Bitstring
1. python3 -m pip install --upgrade bitstring

## Install pyinstaller
1. python3 -m pip install --upgrade pyinstaller
### or
1. python -m pip install --upgrade pyinstaller
### to compile with pyinstaller
pyinstaller --onefile /path/to/pythonpton/script
## if pyinstaller is not working as a command
export PATH=$PATH:~/.local/bin

## Use:
1. Run program
2. Type E or Encode to add text to an image OR Type D or Decode to pull text from an image
3. Input options (ie. text to hide, output image and/or input image)
4. Get image with hidden message when Encoding OR get hidden message from an image when Decoding. 


## Example Encode:
1. Run program
2. Encode
3. text input = Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. 
4. input image = ./resources/redheart.PNG
5. output image = ./resources/redheart-loremipsum.PNG


## Example Decode:
1. Run program
2. Decode
3. input image = ./resources/redheart-loremipsum.PNG
4. prints out message: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. 


## Troubleshooting
if you get an error about indentation use untabify to change all tabs to 4 spaces. 
(I am bad about mixing spaces and tabs, and have to run untabify to fix problems occationally.)
Good Luck!