# Powershell: 
```
Set-Location “C:\Windows\Temp”
Remove-Item * -recurse -force

Set-Location “C:\Windows\Prefetch”
Remove-Item * -recurse -force

Set-Location “C:\Documents and Settings”
Remove-Item “.\*\Local Settings\temp\*” -recurse -force

Set-Location “C:\Users”
Remove-Item “.\*\Appdata\Local\Temp\*” -recurse -force
```
