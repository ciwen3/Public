#!/bin/bash
: '
Wrote this script to close down my kids Linux Desktop computer at 10 PM on school nights
chmod 700 bedtime.sh # make bash script executable by root only
sudo apt install cron # install cron jobs
sudo systemctl enable cron # enable cron jobs service
sudo crontab -e # add the next line at the bottom
@reboot bedtime.sh 
sudo crontab -l # to view the crontab
'
while : # infinite loop
do 
  DAY="date +%u" # Set Day Variable, will be used to check the day of the week 1-7, 1 is Monday 7 is Sunday
  HOUR="date +%H" # Set Hour Variable, will be used to check the HOUR in Military time
  if [[ $DAY == 5 ]] 
  then 
    sleep 1d  # Friday sleep for 1 day then check again 
  elif [[ $DAY == 6 ]] 
  then 
    sleep 6h # Saturday sleep for 6 hours then check again
  elif [[ $HOUR -ge 22 ]]
  then 
    secs=$((5 * 60)) # 5 min timer
    while [ $secs -gt 0 ]
    do
      clear # clear the screen so that the info is not scrolling
      echo "It is Bedtime! Say good night to your friends. We love you. Now go to sleep."
      echo "This Computer Will Shutdown in \n$secs seconds" | figlet -f big
      sleep 1
      secs=$(($secs -1)) # Count down by 1 sec
    done
    sudo shutdown -h now # shutdown the computer right now
  else
    sleep 5m # sleep for 5 min and then check again. 
  fi
done
