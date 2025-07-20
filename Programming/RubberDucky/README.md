# Rubber Ducky scripts
## if you see arduino files (*.ino) it is for the Attiny85 which is a lot cheaper than the rubberducky but can do the same thing. 

# Hak5 Duck Encoder 2.6.3
Usage: duckencode -i [file ..]      encode specified file

   or: duckencode -i [file ..] -o [file ..] encode to specified file

# Arguments:
```
   -i [file ..]     Input File
   -o [file ..]     Output File
   -l [file ..]     Keyboard Layout (us/fr/pt or a path to a properties file)
```

# Script Commands:
```
   ALT [key name] (ex: ALT F4, ALT SPACE)
   CTRL | CONTROL [key name] (ex: CTRL ESC)
   CTRL-ALT [key name] (ex: CTRL-ALT DEL)
   CTRL-SHIFT [key name] (ex: CTRL-SHIFT ESC)
   DEFAULT_DELAY | DEFAULTDELAY [Time in millisecond * 10] (change the delay between each command)
   DELAY [Time in millisecond * 10] (used to overide temporary the default delay)
   GUI | WINDOWS [key name] (ex: GUI r, GUI l)
   REM [anything] (used to comment your code, no obligation :) )
   ALT-SHIFT (swap language)
   SHIFT [key name] (ex: SHIFT DEL)
   STRING [any character of your layout]
   REPEAT [Number] (Repeat last instruction N times)
   [key name] (anything in the keyboard.properties)
```

# Download the Duck Encoder
In order to begin creating our own Rubber Ducky payloads, we need to have the duck encoder installed. This is a program that takes our ducky script (more on that in a minute) and converts it into a cross-platform inject.bin file that the keyboard adapter will use to deliver our keystroke payload.

While there are a number of different formats for accessing the duck encoder, including a web interface https://ducktoolkit.com/encoder/ now at https://payloadstudio.com/community/ , if you’re comfortable with the command line, I’d recommend using the downloadable .jar java program since it allows you to compile the payload and copy it to the microSD card in one step.

When I first started testing the device, I used the link on the Rubber Ducky wiki https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Downloads and ended up downloading a very old version of the encoder from 2013 (1.2) which had trouble creating payloads for running keystrokes on newer operating systems https://github.com/hak5darren/USB-Rubber-Ducky/issues/79 .

downloading the latest version (2.6.3, as of this writing) directly from the github repository, here.


# References:
- https://infosecwriteups.com/make-usb-rubber-ducky-with-less-than-3-fa72dac9e4de
- https://downloads.arduino.cc/arduino-1.8.19-linux64.tar.xz
- https://debian.pkgs.org/sid/debian-main-arm64/arduino_1.8.19+dfsg1-1_arm64.deb.html
- https://ubuntu.pkgs.org/22.04/ubuntu-universe-amd64/arduino_1.8.19+dfsg1-1_amd64.deb.html
- http://digistump.com/package_digistump_index.json
- https://blog.hartleybrody.com/rubber-ducky-guide/


## All my projects are offered “as-is”, without warranty, and disclaiming liability for damages resulting from using this project. use at your own risk. 


# Payloads:
- https://github.com/dronus4x4/rubberducky/tree/master/payloads
- https://github.com/Koploseus/RubberDuckyScript
- https://github.com/Webby420/hak5rubberducky
- https://github.com/dsymbol/ducky-payloads/tree/main
