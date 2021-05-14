# MouseJiggler

## How to Setup:
https://air-gap.com.au/how-to-make-a-mouse-jiggler-with-digispark/

## Iformation about making the MouseJiggler look like a real mouse:
1. https://ericdraken.com/usb-mouse-jiggler/
2. https://devicehunt.com/
3. https://devicehunt.com/view/type/usb/vendor/045E/device/0083
```
Microsoft USB Mouse: 
Vendor: 045E
Device: 0083

#define USB_CFG_VENDOR_ID 0x5e, 0x04
#define USB_CFG_DEVICE_ID 0x83, 0x00
```




## Simple Mouse Jiggler: https://ericdraken.com/usb-mouse-jiggler/
```
#include <DigiMouse.h>
void setup(){
  DigiMouse.begin();
  pinMode(1, OUTPUT);
}
 
void loop() {
  while(true) {
    digitalWrite(1, HIGH);  
    DigiMouse.move(200,0,0); // 200px right
    DigiMouse.delay(50);
    DigiMouse.move(-200,0,0); // 200px left
    digitalWrite(1, LOW);
    DigiMouse.delay(30000);
  }
}
```

#### Advanced:
If you prefer the USB mouse jiggler to look like a real mouse to most computers, then you can edit the usbconfig.h deep in the Digistump hardware folder.

edit: 
```%LOCALAPPDATA%\Arduino15\packages\digistump\hardware\avr\1.6.7\libraries\DigisparkMouse\usbconfig.h```

scroll down to: 
```/* -------------------------- Device Description --------------------------- */```

change the lines to match so it identifies as a Microsoft USB Mouse
```
#define USB_CFG_VENDOR_ID 0x5e, 0x04
#define USB_CFG_DEVICE_ID 0x83, 0x00
```
