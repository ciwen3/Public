# Bedtime Bash Script
![Screenshot](https://img.shields.io/badge/Language-Bash-blue)
![Screenshot](https://img.shields.io/badge/Platform-Linux-brightgreen)

### Notes:
used to power down my kids Linux computers at a set time. the files can be installed anywhere so long as your kids don't have sudo access and you use the chattr command to make the scripts immutable. 

1. save both files to the hard drive
2. make sure bedtime.sh points to final-countdown.sh
3. make bedtime.sh executable and setuid bit 

```chmod 4111 bedtime.sh```

4. make final-countdown.sh executable and setuid bit 

```chmod 4111 final-countdown.sh```

5. create cron job to start bedtime.sh at reboot
```
sudo apt install cron
sudo crontab -e 
or 
crontab -e -u root
# add the following line
@reboot sleep 300 && /path/to/bedtime.sh 
sudo systemctl enable cron.service
sudo systemctl restart cron.service
```

## All of my Public projects, opinions and advice are offered “as-is”, without warranty, and disclaiming liability for damages resulting from using any of my software or taking any of my advice.



