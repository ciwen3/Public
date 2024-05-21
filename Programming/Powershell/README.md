# My Powershell Scripts
![Screenshot](https://img.shields.io/badge/Language-Powershell-blue)
![Screenshot](https://img.shields.io/badge/Platform-Windows-brightgreen)



```Powershell
PS C:\> Get-Childitem -Path Env:* | Sort-Object Name

Name                           Value
----                           -----
ALLUSERSPROFILE                C:\ProgramData
APPDATA                        C:\Users\<user>\AppData\Roaming
CommonProgramFiles             C:\Program Files\Common Files
CommonProgramFiles(x86)        C:\Program Files (x86)\Common Files
CommonProgramW6432             C:\Program Files\Common Files
COMPUTERNAME                   DESKTOP-<random#>
ComSpec                        C:\WINDOWS\system32\cmd.exe
DriverData                     C:\Windows\System32\Drivers\DriverData
GOPATH                         C:\Users\<user>\go
HOMEDRIVE                      C:
HOMEPATH                       \Users\<user>
LOCALAPPDATA                   C:\Users\<user>\AppData\Local
LOGONSERVER                    \\DESKTOP-<random#>
Medit_CHITUBOX_Basic_Bridge    C:\Program Files\CHITUBOX V1.9.2\CHITUBOX.exe
NUMBER_OF_PROCESSORS           8
OneDrive                       C:\Users\<user>\OneDrive
OS                             Windows_NT
Path                           C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Python27amd64;C:\Python27amd64\Scripts;C:\Program Files\Go\bin;C:\User...
PATHEXT                        .COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.CPL
PROCESSOR_ARCHITECTURE         AMD64
PROCESSOR_IDENTIFIER           Intel64 Family 6 Model 94 Stepping 3, GenuineIntel
PROCESSOR_LEVEL                6
PROCESSOR_REVISION             5e03
ProgramData                    C:\ProgramData
ProgramFiles                   C:\Program Files
ProgramFiles(x86)              C:\Program Files (x86)
ProgramW6432                   C:\Program Files
PSModulePath                   D:\Documents\WindowsPowerShell\Modules;C:\Program Files\WindowsPowerShell\Modules;C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules
PUBLIC                         C:\Users\Public
SystemDrive                    C:
SystemRoot                     C:\WINDOWS
TEMP                           C:\Users\<user>\AppData\Local\Temp
TMP                            C:\Users\<user>\AppData\Local\Temp
USERDOMAIN                     DESKTOP-<random#>
USERDOMAIN_ROAMINGPROFILE      DESKTOP-<random#>
USERNAME                       <user>
USERPROFILE                    C:\Users\<user>
VBOX_MSI_INSTALL_PATH          C:\Program Files\Oracle\VirtualBox\
windir                         C:\WINDOWS
```



# Powershell: 
```Powershell
Set-Location $env:WinDir\temp\
Remove-Item * -recurse -force

Set-Location $env:WinDir\Prefetch
Remove-Item * -recurse -force

Set-Location "$env:SystemDrive\Documents and Settings"
Remove-Item “.\*\Local Settings\temp\*” -recurse -force

Set-Location "$env:SystemDrive\Users”
Remove-Item “.\*\Appdata\Local\Temp\*” -recurse -force

Set-Location $env:SystemDrive
Remove-Item *.log -recurse -force
Remove-Item *.bak -recurse -force
Remove-Item *.gid -recurse -force

Set-Location "$env:Temp"
Remove-Item * -recurse -force
```





#
Powershell is outside my normal comfort zone so don't expect much here. 
Please feel free to offer constructive criticism.











# All of my Public projects, opinions and advice are offered “as-is”, without warranty, and disclaiming liability for damages resulting from using any of my software or taking any of my advice.
