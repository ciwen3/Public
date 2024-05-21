Updated Chicken Man Game Instructions 
Taken From: https://github.com/skickar/ChickenManGame
======
    ,~.
    ,-'__ `-,
    {,-'  `. }              ,')
    ,( a )   `-.__         ,',')~,      ________         _______   _     __         
    <=.) (         `-.__,==' ' ' '}    /_  __/ /  ___   / ___/ /  (_)___/ /_____ ___     
    (   )                      /)       / / / _ \/ -_) / /__/ _ \/ / __/  '_/ -_) _ \    
    `-'\   ,                    )      /_/_/_//_/\__/  \___/_//_/_/\__/_/\_\\__/_//_/    
     |  \        `~.        /           /  |/  /__ ____    / ___/__ ___ _  ___          
     \   `._        \      /           / /|_/ / _ `/ _ \  / (_ / _ `/  ' \/ -_)         
      \     `._____,'    ,'           /_/  /_/\_,_/_//_/  \___/\_,_/_/_/_/\__/          
       `-.             ,'
          `-._     _,-'
              77jj'
             //_||
          __//--'/`      
        ,--'/`  '

## Overview:

The Chicken Man Wi-Fi hacking game is a WPA/WPA2 cracking game for CTF's and hackerspaces.

The purpose of this game is to have an ultra low-cost microcontroller based Wi-Fi hacking game for beginners. It is designed to be easy to set up, cost less than $50 to play, and requires no deauthing to practice. It has been tested on the D1 mini and NodeMCU.

![A glorious flock](
https://media.giphy.com/media/XErcue5rxXKBdbw6u6/giphy.gif "PCC Hardware Setup")

This project was created by Kody Kinzie and Brandon Paiz for the Leadership in Technology club in Pasadena and the Retia team, with much assistance from Stefan "Chicken Man" Kremser. 


## What you need:

This game requires three elements to play. We need a device to create a Wi-Fi access point, a device to join that Wi-Fi network to generate handshakes, and a device to try cracking the passwords on.

1) We need a device to create a Wi-Fi access point to hack, called a Chicken. For this, we'll use a ESP8266 based device, like the D1 mini or NodeMCU. We'll also need a breadboard, a 330 ohm resistor, and one green, blue, and red LED.

2) We also need a device to join the Chicken's Wi-Fi network to generate handshakes for us to crack and keep track of the score. This is called the Chicken Man. The setup for a Chicken Man is identical as for a Chicken, but includes a wire connecting pin D7 to ground. This converts a Chicken into a Chicken Man.

3) Finally, we need a device to play the game on! You can use any computer running Kali Linux, including the Raspberry Pi. You will need the Aircrack-ng suite, and a wireless network adapter that supports monitor mode. Want to do it the cheapest and easiest way? This is our setup:
* ANY computer with the Google Chrome browser and Secure Shell extension.
* 1 Raspberry Pi running Kali Linux with SSH enabled
On your computer, connect to the Raspberry Pi in the browser via SSH. You can follow this guide if you need help: https://null-byte.wonderhowto.com/how-to/use-chrome-browser-secure-shell-app-ssh-into-remote-devices-0181892/

## How to play:

![Playing the game](https://i.imgur.com/uXYOqcX.jpg "The Chicken Man Game at PCC!")

After connecting between 1-5 Chickens and at least one Chicken Man, you will see the Chickens appear as WPA2 encrypted Wi-Fi networks that start with “Chicken”.
Your goal is to access the web interface on each Chicken, and set it to your team’s color.
Your team gets points for every second a Chicken is set to your team color.
To join the network, you have to find the password. We will be using WPA2 handshake cracking to get the password.

Here is a video walkthrough of playing the game using a Raspberry Pi: https://youtu.be/e9W8uEUr4uI

## The Legend of the Chicken Man:

To win the game, you need to have the most points at the end of our 45 minute match.
Your team gets points by cracking the password to a Chicken network and logging in. Once you log in, you can go to 192.168.4.1 in a browser menu to see the Chicken’s menu

![Who will be the chicken man?](https://i.imgur.com/CWArhK1.jpg "Set your team color!")

To play, open Wireshark or Airodump-ng and search for the channel the game piece has created an access point on using a wireless network adapter that supports monitor mode.
Begin capturing Wi-Fi traffic from the access point, apply filters to show when 4-way handshake is captured from the Chicken Man joining the Chicken.
Save the captured handshake as a .CAP file, run Aircrack-ng or another cracking program against a password list to brute-force the password to the Chicken.
Try accessing the Wi-Fi access point of the Chicken with the cracked password. If it works, scan the network to find the IP address of the Chicken's webserver (192.168.4.1 by default)
Open the Chicken's webserver in a browser, and (if you are the red team) click the "Red Team" button to turn the LED of the game piece to your team's color.

## The Commands:
- List network adapters - ifconfig
- Put adapter in monitor mode (changes wlan0 to wlan0mon) - airmon-ng start wlan0
- Watch traffic on all channels (MUST BE IN MONITOR MODE FIRST) - airodump-ng wlan0mon
- Capture handshake on a channel - airodump-ng -w capturefile -c [channel number] wlan0mon
- Crack the handshake - aircrack-ng -w [password list] [capture file].cap


#### Verify that airmon-ng has no issues:
sudo airmon-ng check 

![check](https://i.imgur.com/O2zgQTV.png "check")


#### Kill any issues with using airmon-ng:
sudo airmon-ng check kill

![check kill](https://i.imgur.com/lsQMJq8.png "check kill")


#### Find Network Interface Cards:
"ip addr" or "ifconfig"

![ip addr](https://i.imgur.com/ToTLRNL.png "ip addr")


#### Start airmon-ng on interface:
yours will be different from wlp1s0 based on the output from "ifconfig" or "ip addr" command

sudo airmon-ng start wlp1s0

![start](https://i.imgur.com/c7hv7Cb.png "start")


#### Start monitor mode on interface:
yours will be different from wlp1s0mon based on output from the previous command

sudo airodump-ng wlp1s0mon

Ctrl + C to quit

![airodump](https://i.imgur.com/En6BNJV.png "airodump")


#### Save packets from airodump:
sudo airodump-ng -w [Save to this File Name] -c [Channel#] [Interface]

sudo airodump-ng -w test -c 2 wlp1s0mon

Ctrl + C to quit

![airodump](https://i.imgur.com/frSQCbs.png "airodump")



#### Use aircrack and passwordlist of your choice:
sudo aircrack-ng -w [Password list] [Name of CAP file] 

sudo aircrack-ng -w ~/github/ChickenManGame/ChickenDay/passwords/darkweb2017-top10000.txt test-02.cap 



#### Stop monitor mode on interface:
yours will be different from wlp1s0mon based on what you used for the Start monitor mode on interface command

sudo airmon-ng stop wlp1s0mon


#### Start Network Manager so you can get back online:
sudo service network-manager start




## How Chickens Work:

Each Chicken can be set to easy, medium or hard.
When you set your team’s color on a Chicken, it creates a new Wi-Fi network with a harder password
Harder difficulty Chickens have harder passwords, and your team gets more points for hacking them.
After 45 minutes, count up the score and see which team wins

Set up the game:
1) Download the .ZIP file or run "git clone https://github.com/skickar/ChickenManGame.git" in a terminal window
2) Unzip the folder and copy the ChickenDay folder to your Raspberry Pi.
3) Install Arduino software (actual Arduino not needed). Copy the ChickenManGame folder to the Arduino folder on your computer.
4) Install the SimpleCLI library by downloading the ZIP from https://github.com/spacehuhn/SimpleCLI, unzipping it, and dropping the folder in your Arduino library folder
5) Open the ChickenManGame.INO file in Arduino software. (File > Open > Browse to file location).
6) If you haven't used an esp8266 before, Click on the Arduino software drop-down menu File, then select "Preferences" (File > Preferences). Then paste "http://arduino.esp8266.com/stable/package_esp8266com_index.json" into the Additional Boards Manager URLs field and Click "OK" to continue. 

![File > Preferences](https://i.imgur.com/0naG98l.png "File > Preferences")

![esp8266](https://i.imgur.com/B1SCojs.png "esp8266")

7) Click on "Tools," then hover over the "Board" section to see the list of supported boards. At the top, click "Boards Manager" to open the window that will allow us to add more boards. (Tools > Board > Board Manager)

![Tools > Board > Board Manager](https://i.imgur.com/BCHgfQr.png "Tools > Board > Board Manager")

When the Boards Manager window opens, type "esp8266" into the search bar. Select "esp8266" by ESP8266 Community, and install it to add support for the D1 Mini to your Arduino IDE. 

![ESP8266 Community](https://i.imgur.com/5KPnj9o.png "ESP8266 Community")

8) Go to the Sketch menu, click Inlcude Library, and go to Manage Libraries. Install the Adafruit NeoPixel library. (Sketch > Include Library > Manage Libraries)

![Sketch > Include Library > Manage Libraries](https://i.imgur.com/9BqOeGe.png "Sketch > Include Library > Manage Libraries")

![Adafruit NeoPixel](https://i.imgur.com/gozbiVR.png "Adafruit NeoPixel")

9) Select the "WeMos D1 R2 & mini" board or NodeMCU (if you're using that) and set the IwIP Variant to "1.4 Higher Bandwidth" under the Tools Menu. (Tools > IwIP Variant: > v1.4 Higher Bandwidth)

![NodeMCU](https://i.imgur.com/zGzpfyL.png "NodeMCU")

10) Connect USB-A to Micro-USB cable to NodeMCU. Press the green arrow to upload the sketch to your esp8266. 

![sketch](https://i.imgur.com/dQndaSy.png "sketch")

Open the serial monitor and set the baud rate to 115200 to watch for errors and confirm the game is working!

![serial monitor](https://i.imgur.com/hHiTHTX.jpg "serial monitor")

## Hardware Setup:

![Who will be the chicken man?](https://i.imgur.com/WOdqsh2.jpg "WHO WILL BE THE CHICKEN MAN")


1) Plug the positive pin of a red LED to pin D1, and the negative to a 330 ohm resistor. Connect the other end of the resistor to ground.
2) Connect a green LED to pin D2, and a blue LED to pin D3, each with a resistor connecting the negative pin to ground.
* If you're feeling brave, you can connect all three LED's to the same resistor, which is connected to ground.
* If you hate your LED's, connect them directly to ground with no resistor. They will burn out in glory.

![Chicken](https://i.imgur.com/Gneu509.png "Chicken")

3) Plug a wire connecting pin D7 to ground to change a Chicken into a Chicken Man.

![ChickenMan](https://i.imgur.com/qqIpGrU.png "ChickenMan")



## Easter egg:
* To create an Uber Chicken Man, connect a neopixel stip to pin D5, and set the value of "const bool NEOPIXEL" to "true" in the hardware.h configuration file. This will make the Chicken Man use the neopixel stip to show who is winning. Also remember to define the number of pixels in the strip.

![Who will be the chicken man?](https://media.giphy.com/media/hQtpKVKeEYXtu4Ji8u/giphy.gif "WHO WILL BE THE CHICKEN MAN")


## Set up the Raspberry Pi:

1) Download the "Kali Linux RPi0w Nexmon" image from: https://www.offensive-security.com/kali-linux-arm-images/
2) Insert a micro SD card with at least 8 GB (16 recommended) and use Etcher to flash the image to the disk
3) Plug the micro SD card into your Pi and connect it via ethernet to a router
4) Connect your computer to the router via Wi-Fi or ethernet and scan for the Pi's IP address
5) Connect to the Pi via a terminal window or in a browser with the Secure Shell Google Chrome extension
6) Download the ChickenDay folder from this repo, and put it on your Raspberry Pi

![Who will be the chicken man?](https://i.imgur.com/AkssX5r.png "WHO WILL BE THE CHICKEN MAN")

