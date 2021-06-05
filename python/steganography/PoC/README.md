# Steganography Decode and Run Proof of Concept

This Steganography program was created to retrieve or decode the message from an image made with this program and run it in a terminal. 

## This project is offered “as-is”, without warranty, and disclaiming liability for damages resulting from using this project.

**The project is under development, any suggestion is welcome!**

![Screenshot](https://img.shields.io/badge/Platform-Universal-brightgreen)
![Screenshot](https://img.shields.io/badge/Language-Python3-blue)

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
1. python -m pip install --upgrade pip
2. python -m pip install --upgrade Pillow
## Install Bitstring
1. python3 -m pip install --upgrade bitstring

# Use:
1. Run program followed by the name of the picture you want to decode and run commands from. 
```Steganography-Poc.py /path/to/picture/to/decode```
2. wait for program to run. 

# Example Decode Linux:
1. chmod +x Steganography-Poc.py
2. ```Steganography-Poc.py redheart-firefox.PNG``
3. if firefox is install it should open. 

# Example Decode Windows:
1. chmod +x Steganography-Poc.py
2. ```Steganography-Poc.py redheart-calc.PNG``
3. if Caclulator is install it should open. 

# Troubleshooting
if you get an error about indentation use untabify to change all tabs to 4 spaces. 
(I am bad about mixing spaces and tabs, and have to run untabify to fix problems occationally.)
Good Luck!
