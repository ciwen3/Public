# Bedtime Powershell Script
![Screenshot](https://img.shields.io/badge/Language-Powershell-blue)
![Screenshot](https://img.shields.io/badge/Platform-Windows-brightgreen)
#
used to power down my kids computers at a set time. 

# Setup
place a copy of the script in C:\Windows
Open GPO editor: 
User Configurations > Windows Settings > Scripts (Logon / Logoff) > Logon
Add: 
Script Name: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
Script Parameters: -ExecutionPolicy bypass -file C:\Windows\bedtime.ps1


# All of my Public projects, opinions and advice are offered “as-is”, without warranty, and disclaiming liability for damages resulting from using any of my software or taking any of my advice.



