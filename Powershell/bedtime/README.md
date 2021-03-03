# Bedtime Powershell Script
![Screenshot](https://img.shields.io/badge/Language-Powershell-blue)
![Screenshot](https://img.shields.io/badge/Platform-Windows-brightgreen)
#
used to power down my kids Windows computers at a set time. 

# Setup
1. place a copy of the script in C:\Windows
2. Open GPO editor: 
3. User Configurations > Windows Settings > Scripts (Logon / Logoff) > Logon
4. Add: 
5. Script Name: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
6. Script Parameters: -ExecutionPolicy bypass -file C:\Windows\bedtime.ps1


# All of my Public projects, opinions and advice are offered “as-is”, without warranty, and disclaiming liability for damages resulting from using any of my software or taking any of my advice.



