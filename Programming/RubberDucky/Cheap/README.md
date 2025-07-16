For making USB Rubber Ducky, you just need this stuff:
1. Digispark Attiny 85 ($2.94)
2. Arduino IDE
3. A glass of coffee with music.

### Setup the environment [Linux]

Download and Install the latest Arduino software at https://www.arduino.cc/en/software. For this project, I use Arduino IDE 1.8.19 for Linux 64 bits. And In this tutorial, I will skip for installation of the Aduino IDE.
```bash
tar -xvf ./arduino-1.8.19-linux64.tar.xz 
cd arduino-1.8.19
sudo ./install.sh
./arduino
```

### Arduino IDE download page
- Run Arduino IDE and go to File menu, and select Preferences. 
- Then in the Additional Boards Manager Urls, put this link ``` http://digistump.com/package_digistump_index.json ```
- And click ok.

```
NOTE: the link http://digistump.com/package_digistump_index.json no longer works.
you can get a copy of the json from https://web.archive.org/web/20220530184059/https://raw.githubusercontent.com/digistump/arduino-boards-index/master/package_digistump_index.json  
then use the file:///<location of the file> in place of a URL
you can use any browser to figure out the specific 'URL'
```

### Preference window
Go to Tools menu, then the Boards submenu, select Board Manager. In the Type field, select Contributed and install Digistump AVR Boards.

### Boards Manager window
After the installation is finished, close the Boards Manager window.

### The last step, select Digispark (Default — 16.5mhz) as your main board.
Go to Tools menu, then Boards submenu, Click Digistump AVR Board and select Digispark (Default — 16.5mhz). You have been finished setup the Digispark Environment.

### Testing with Example Code

Try with testing code from File > Example > DigisparkKeyboard > Keyboard.
```
#include "DigiKeyboard.h"
void setup() {
  // don't need to set anything up to use DigiKeyboard
}
void loop() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.println("Hello Digispark!");
  DigiKeyboard.delay(5000);
}
```
Verify the code, and if it’s okay click the upload button at the right side of the verify button.

And Then plug in your Digispark.

# References:
https://infosecwriteups.com/make-usb-rubber-ducky-with-less-than-3-fa72dac9e4de
