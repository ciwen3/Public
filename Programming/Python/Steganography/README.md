# Steganography 

## Versions: 
1. Text - This Steganography program was created to hide or encode a Message in a PNG image by manipulating the pixel data and to retrieve or decode the message from an image made with this program. 
2. Create Image - This Steganography program was created to hide or encode a Message in a PNG image that it can create on the fly. 
3. File - This Steganography program was created to hide or encode a File in a PNG image by manipulating the pixel data. 
4. PoC - Proof-of-Concept on how this could be weaponized to get a harmless seeming PNG past EDR and Anti virus that contains hidden commands. the PoC program will decode the hidden commands and run them in a terminal with whatever access it has. 
## Resources:
contains Images to use for testing the programs. redheart.PNG is an un encoded image. Every other png is encoded with something to test decoding with each version of the program. 

## This project is offered “as-is”, without warranty, and disclaiming liability for damages resulting from using this project.

**The project is under development, any suggestion is welcome!**

![Screenshot](https://img.shields.io/badge/Platform-Universal-brightgreen)
![Screenshot](https://img.shields.io/badge/Language-Python3-blue)

## To Do:
1. make graphical interface using Tkinter
2. add encryption modules 
3. ~~add the ability to save the text output as a .txt file~~
4. ~~add the ability to read a message from a .txt file~~
5. add option to copy the exif data from original photo to new photo (need to make a version that works with JPEG instead of PNG files which uses a different color mode "CMYK".) https://guides.lib.umich.edu/c.php?g=282942&p=1885348
6. ~~add option to create image from scratch (possibly just a solid color)?? (still debating)~~
7. ~~add file upload option that copies bits instead of text (test on .pdf, .txt,~~ .exe, .docx, .odt, etc.)
8. add a file name option so that the file name is automatically set based on its original name or name given at image encoding time. 
9. make pop-up windows ask for a file if none is given

## Requirements to run python code:
***doesn't apply to compiled binaries***
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

```
[root@root ~]$ which pyinstaller
which: no pyinstaller in (/bin:/usr/bin:/usr/local/bin:/usr/local/sbin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl)
[root@root ~]$ export PATH=$PATH:~/.local/bin
[root@root ~]$ which pyinstaller
/root/.local/bin/pyinstaller
```
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


## Executable
### Warning: I have also made an Executable .exe for the Steganography program however Microsoft Defender Flags that as Malicious because it is not signed. 

# Steganogrphy Decode and Run PoC:
## Use:
1. Run program followed by the name of the picture you want to decode and run commands from. 
2. ``` Steganography-Poc.py /path/to/picture/to/decode ```
3. wait for program to run. 

## Example Decode and Run on Linux option 1:
1. ``` chmod +x Steganography-Poc ```
2. ``` Steganography-Poc redheart-firefox.PNG ```
3. if firefox is installed it should open. 

## Example Decode and Run on Linux option 2:
1. ``` chmod +x Steganography-Poc.py ```
2. ``` Steganography-Poc.py redheart-firefox.PNG ```
3. if firefox is installed it should open. 

## Example Decode and Run on Linux option 3:
1. ```python3 Steganography-Poc.py redheart-firefox.PNG ```
2. if firefox is installed it should open. 

## Example Decode and Run on Windows option 1:
1. ``` python Steganography-Poc.py redheart-calc.PNG ```
2. Caclulator should open.  

## Example Decode and Run on Windows option 2:
1. drag and drop redheart-calc.PNG onto Steganography-Poc.exe
2. Caclulator should open. 

## Example Decode and Run on Windows option 3:
1. Open CMD or PowerShell
2. ``` Steganography-Poc.exe redheart-calc.PNG ```
3. Caclulator should open. 

## Troubleshooting
if you get an error about indentation use untabify to change all tabs to 4 spaces. 
(I am bad about mixing spaces and tabs, and have to run untabify to fix problems occationally.)
Good Luck!
