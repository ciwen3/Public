# Steganography 
## This version of the program is capable of encoding a entire ***File***. So far is only working for .txt and .pdf
This Steganography program was created to hide or encode a message in a PNG image by manipulating the pixel data and to retrieve or decode the message from an image made with this program. 

## This project is offered “as-is”, without warranty, and disclaiming liability for damages resulting from using this project.

**The project is under development, any suggestion is welcome!**

### Test:
| File Type | Functionality |
|-----------|---------------|
| txt | working (with extra symbol) |
| pdf | working |
| docx | not working |
| odt | not working |
| png | not tested |
| jpeg | not tested |
| exe | not tested |
| pe | not working |

![Screenshot](https://img.shields.io/badge/Platform-Universal-brightgreen)
![Screenshot](https://img.shields.io/badge/Language-Python3-blue)

## Requirements:
1. Python 3 (check in a terminal by running: python --version)
2. Pillow (PIL) for Python

![Screenshot](https://github.com/ciwen3/Public/blob/master/Python/Steganography/Resources/file.JPG)

## Use:
1. Run program
2. Type E or Encode to add text to an image OR Type D or Decode to pull text from an image
3. Input options (ie. File to encode , output image and/or input image)
4. Get image with hidden File when Encoding OR get hidden message from an image when Decoding. 


## Example Encode:
1. Run program
2. Encode
3. File = ./Resume.pdf
4. input image = ./resources/butterfly.PNG
5. output image = ./resources/Resume.PNG


## Example Decode:
1. Run program
2. Decode
3. input image = ./resources/Resume.PNG
4. output file = Resume.pdf
5. creates the file you specify. 


## Troubleshooting
if you get an error about indentation use untabify to change all tabs to 4 spaces. 
(I am bad about mixing spaces and tabs, and have to run untabify to fix problems occationally.)
Good Luck!
