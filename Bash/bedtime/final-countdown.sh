#!/bin/bash

secs=$((5 * 60)) # 5 min timer
while [ $secs -gt 0 ]
do
  clear # clear the screen so that the info is not scrolling
  echo "It is Bedtime! Say good night to your friends. We love you. Now go to sleep."
  echo "This Computer Will Shutdown in $secs seconds" | figlet -f big
  sleep 1
  secs=$(($secs -1)) # Count down by 1 sec
done
sudo shutdown -h now # shutdown the computer right now
