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
OR
```
//This DigiSpark script opens up Rick Astley's - Never Gonna Give You Up and also a fake Windows update screen and then maximizes it using F11
#include "DigiKeyboard.h"
void setup() {
  //empty
}
void loop() {
  DigiKeyboard.delay(2000);
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(600);
  DigiKeyboard.print("https://youtu.be/dQw4w9WgXcQ?t=43s");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(5000);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(3000);
  DigiKeyboard.print("http://fakeupdate.net/win10ue");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(2000);
  DigiKeyboard.sendKeyStroke(KEY_F11);
  for(;;){ /*empty*/ }
}
```

Verify the code, and if it’s okay click the upload button at the right side of the verify button.

And Then plug in your Digispark.



### Typing and Key Presses
```
sendKeyStroke(key, modifier): Sends a keystroke with an optional modifier (like CTRL, ALT, etc.). key represents the keycode of the key, and modifier is the keycode of the modifier key.
print(text): Types the specified text as if it was typed on a keyboard.
println(text): Types the specified text and then sends a return (enter key), effectively like pressing ‘Enter’ after typing the text.
Special Characters and Keycodes
write(byte): Sends a single byte of data as a keystroke, which can represent special characters or function keys.
setModifier(modifier): Sets a modifier key (like CTRL, SHIFT, ALT) which will be held down.
setKey(key): Sets a regular key to be pressed.
sendKeyPress(): Sends the current modifier and key values set by setModifier and setKey.
releaseKey(): Releases any pressed keys. It’s good practice to use this after sending a keypress to avoid the key being held down indefinitely.
```

### Digikeyboard Command List and Keystrokes
The DigiKeyboard library, a part of the DigiSpark Arduino package, provides various keystrokes that can be used to emulate a USB keyboard. These keystrokes correspond to different keys on a standard keyboard and are used in conjunction with the sendKeyStroke function in the DigiKeyboard library.

Here’s a list of common keystrokes that are typically available in the DigiKeyboard library:

### Standard Keys
```
KEY_A, KEY_B, KEY_C, …, KEY_Z: Representing the alphabet keys.
KEY_1, KEY_2, …, KEY_9, KEY_0: Representing the number keys.
KEY_ENTER
KEY_ESC
KEY_BACKSPACE
KEY_TAB
KEY_SPACE
KEY_MINUS: The ‘-‘ key.
KEY_EQUAL: The ‘=’ key.
KEY_LEFT_BRACE: The ‘[‘ key.
KEY_RIGHT_BRACE: The ‘]’ key.
KEY_BACKSLASH: The ” key.
KEY_SEMICOLON: The ‘;’ key.
KEY_QUOTE: The ”’ key.
KEY_TILDE: The ‘`’ key.
KEY_COMMA: The ‘,’ key.
KEY_PERIOD: The ‘.’ key.
KEY_SLASH: The ‘/’ key.
KEY_CAPS_LOCK
```

### Function Keys
```
KEY_F1, KEY_F2, …, KEY_F12: Representing the function keys.
```

### Control Keys
```
KEY_LEFT_CTRL
KEY_LEFT_SHIFT
KEY_LEFT_ALT
KEY_LEFT_GUI: Often represents the Windows key or Command key on Mac.
KEY_RIGHT_CTRL
KEY_RIGHT_SHIFT
KEY_RIGHT_ALT
KEY_RIGHT_GUI
```

### Navigation Keys
```
KEY_UP_ARROW
KEY_DOWN_ARROW
KEY_LEFT_ARROW
KEY_RIGHT_ARROW
KEY_HOME
KEY_END
KEY_PAGE_UP
KEY_PAGE_DOWN
KEY_INSERT
KEY_DELETE
```

### Numeric Keypad Keys
```
KEYPAD_0, KEYPAD_1, …, KEYPAD_9
KEYPAD_PERIOD
KEYPAD_DIVIDE
KEYPAD_MULTIPLY
KEYPAD_MINUS
KEYPAD_PLUS
KEYPAD_ENTER
```

### Special Keys
```
KEY_PRINTSCREEN
KEY_SCROLLLOCK
KEY_PAUSE
KEY_NUM_LOCK
```

### Media Playback Controls
```
MEDIA_PLAY_PAUSE: Toggles play/pause of the media player.
MEDIA_STOP_CD: Stops playback.
MEDIA_PREVIOUS_TRACK: Goes to the previous track.
MEDIA_NEXT_TRACK: Goes to the next track.
MEDIA_REWIND: Rewinds the current track.
MEDIA_FAST_FORWARD: Fast forwards the current track.
```

### Volume Controls
```
MEDIA_VOLUME_UP: Increases the system volume.
MEDIA_VOLUME_DOWN: Decreases the system volume.
MEDIA_VOLUME_MUTE: Mutes/unmutes the system volume.
```

### Additional Media Functions
```
MEDIA_EJECT_CD: Ejects the CD or DVD (if applicable).
MEDIA_PLAY: Starts playback (may be different from play/pause toggle).
MEDIA_PAUSE: Pauses playback (may be different from play/pause toggle).
```

### Web and Application Controls
```
MEDIA_WWW: Opens the default web browser.
MEDIA_CALCULATOR: Opens the calculator application.
MEDIA_EMAIL: Opens the default email application.
MEDIA_BROWSER_SEARCH: Activates the browser’s search function.
MEDIA_BROWSER_HOME: Goes to the browser’s home page.
MEDIA_BROWSER_BACK: Goes back in the browser.
MEDIA_BROWSER_FORWARD: Goes forward in the browser.
```



# References:
- https://infosecwriteups.com/make-usb-rubber-ducky-with-less-than-3-fa72dac9e4de
- https://web.archive.org/web/20220306215955/https://digistump.com/wiki/digispark/tutorials/linuxtroubleshooting
- https://rootsaid.com/digispark-hid-digikeyboard-commands/
