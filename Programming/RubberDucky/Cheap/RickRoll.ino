//This DigiSpark script opens up Rick Astley's - Never Gonna Give You Up and also a fake Windows update screen and then maximizes it using F11

//sendKeyStroke(key, modifier): Sends a keystroke with an optional modifier (like CTRL, ALT, etc.). key represents the keycode of the key, and modifier is the keycode of the modifier key.
//print(text): Types the specified text as if it was typed on a keyboard.
//println(text): Types the specified text and then sends a return (enter key), effectively like pressing ‘Enter’ after typing the text.
//write(byte): Sends a single byte of data as a keystroke, which can represent special characters or function keys.
//setModifier(modifier): Sets a modifier key (like CTRL, SHIFT, ALT) which will be held down.
//setKey(key): Sets a regular key to be pressed.
//sendKeyPress(): Sends the current modifier and key values set by setModifier and setKey.
//releaseKey(): Releases any pressed keys. It’s good practice to use this after sending a keypress to avoid the key being held down indefinitely.

#include "DigiKeyboard.h"
void setup() {
  //empty
}
void loop() {
  //Windows version
  DigiKeyboard.delay(2000);
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(600);
  DigiKeyboard.println("chrome https://youtu.be/dQw4w9WgXcQ?t=43s");
  //DigiKeyboard.sendKeyStroke(KEY_SPACE);
  //Mac version
  DigiKeyboard.delay(2000);
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(KEY_SPACE, MOD_GUI_LEFT);
  DigiKeyboard.delay(600);
  DigiKeyboard.println('open -a "Google Chrome" https://youtu.be/dQw4w9WgXcQ?t=43s');
  //DigiKeyboard.println("open -a Safari https://youtu.be/dQw4w9WgXcQ?t=43s");
  //DigiKeyboard.sendKeyStroke(KEY_SPACE);
  //Linux version
  DigiKeyboard.delay(2000);
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(MOD_CONTROL_LEFT, KEY_T);
  DigiKeyboard.delay(600);
  DigiKeyboard.println("chromium https://youtu.be/dQw4w9WgXcQ?t=43s || firefox https://youtu.be/dQw4w9WgXcQ?t=43s || chrome https://youtu.be/dQw4w9WgXcQ?t=43s");
  //DigiKeyboard.sendKeyStroke(KEY_SPACE);
}
