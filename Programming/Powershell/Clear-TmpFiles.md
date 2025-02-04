# Powershell: 
```Powershell
Set-Location “C:\Windows\Temp”
Remove-Item * -recurse -force

Set-Location “C:\Windows\Prefetch”
Remove-Item * -recurse -force

Set-Location “C:\Documents and Settings”
Remove-Item “.\*\Local Settings\temp\*” -recurse -force

Set-Location “C:\Users”
Remove-Item “.\*\Appdata\Local\Temp\*” -recurse -force
```
# Powershell: 
```Powershell
Get-Volume

Set-Location $env:WinDir\temp
Remove-Item * -recurse -force

Set-Location $env:WinDir\Prefetch
Remove-Item * -recurse -force

Set-Location "$env:SystemDrive\Documents and Settings"
Remove-Item “.\*\Local Settings\temp\*” -recurse -force

Set-Location $env:SystemDrive\Users
Remove-Item “.\*\Appdata\Local\Temp\*” -recurse -force

Set-Location $env:SystemDrive
Remove-Item *.log -recurse -force
Remove-Item *.bak -recurse -force
Remove-Item *.gid -recurse -force

Set-Location $env:Temp
Remove-Item * -recurse -force

Get-Volume
```
```Powershell
Get-ChildItem -Path C:\temp -File | Remove-Item -Verbose
Get-ChildItem -Path C:\temp -File -Recurse | Remove-Item -Verbose
Remove-Item -Path $env:TEMP -Recurse -Force -ErrorAction SilentlyContinue


```


```Powershell
# Clear temp files
Get-ChildItem "$env:TEMP", "$env:TMP", "$env:SystemDrive\Windows\Temp", "$env:SystemDrive\Temp" -Recurse -Force -ErrorAction SilentlyContinue | Remove-Item -Force -Recurse -ErrorAction SilentlyContinue

# Clear recycling bin
Clear-RecycleBin -Force -ErrorAction SilentlyContinue
```
