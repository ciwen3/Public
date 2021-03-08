# Bedtime Bash Script
![Screenshot](https://img.shields.io/badge/Language-Bash-blue)
![Screenshot](https://img.shields.io/badge/Platform-Linux-brightgreen)

### Notes:
used to power down my kids Linux computers at a set time. the files can be installed anywhere so long as your kids don't have sudo access and you use the chattr command to make the scripts immutable. 


1. save both files to the hard drive
2. make bedtime script executable ```chmod +x bedtime.sh```
3. make final-countdown.sh executable and setuid bit ```chmod 4111 final-countdown.sh```
4. create cron job to start bedtime.sh at reboot



# Work in Progress:
I will update this from time to time, when I have spare time (which isn't often). 

# All of my Public projects, opinions and advice are offered “as-is”, without warranty, and disclaiming liability for damages resulting from using any of my software or taking any of my advice.



