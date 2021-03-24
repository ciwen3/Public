#!/bin/bash
: '
Wrote this script to close down my kids Linux Desktop computer at 10 PM on school nights
chmod 700 bedtime.sh # make bash script executable by root only
sudo apt install cron # install cron jobs
sudo systemctl enable cron # enable cron jobs service
sudo crontab -e # add the next line at the bottom
5,10,15,20,25,30,35,40,45,50,55 * * * * /path/to/bedtime.sh # Check every 5 mins of every hour
sudo crontab -l # to view the crontab
sudo apt install exo-utils -y # this is required to pop a window for the count down. 
'

  if [[ $(date +%u) == 5 ]] # check if it is Friday
  then 
    exit 0
  elif [[ $(date +%u) == 6 ]] # check if it is Saturday
  then 
    exit 0
  elif [[ $(date +%H) -ge 22 ]] # after 10PM any other day of the week
  then 
    exo-open --launch TerminalEmulator /final-countdown.sh 
  else
    sleep 5m # sleep for 5 min and then check again. 
  fi
