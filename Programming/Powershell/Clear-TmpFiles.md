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
$startTime = Get-Date
$totalFiles = 0
$totalSize = 0

Get-ChildItem "$env:TEMP", "$env:TMP", "$env:SystemDrive\Windows\Temp", "$env:SystemDrive\Temp" -Recurse -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $totalFiles++
    $totalSize += $_.Length
    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue $_.FullName
}

# Clear browser temp files
Get-ChildItem "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\Cache", "$env:LOCALAPPDATA\Mozilla\Firefox\Profiles\*.default\cache2", "$env:LOCALAPPDATA\Microsoft\Edge\User Data\Default\Cache", "$env:LOCALAPPDATA\Microsoft\Internet Explorer\Recovery\Active" -Recurse -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $totalFiles++
    $totalSize += $_.Length
    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue $_.FullName
}

# Clear Steam temp files
Get-ChildItem "$env:APPDATA\Steam\Temp" -Recurse -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $totalFiles++
    $totalSize += $_.Length
    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue $_.FullName
}

# Clear recycling bin
Clear-RecycleBin -Force -ErrorAction SilentlyContinue

$endTime = Get-Date
$elapsedTime = New-TimeSpan -Start $startTime -End $endTime

Write-Host "Cleaned up $totalFiles files, totaling $([Math]::Round($totalSize / 1MB, 2)) MB in $($elapsedTime.TotalSeconds) seconds."
```



```
# Clear temp files
$startTime = Get-Date
$totalFiles = 0
$totalSize = 0

Get-ChildItem "$env:TEMP", "$env:TMP", "$env:SystemDrive\Windows\Temp", "$env:SystemDrive\Temp" -Recurse -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $totalFiles++
    $totalSize += $_.Length
    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue $_.FullName
}

# Clear browser temp files
Get-ChildItem "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\Cache", "$env:LOCALAPPDATA\Mozilla\Firefox\Profiles\*.default\cache2", "$env:LOCALAPPDATA\Microsoft\Edge\User Data\Default\Cache", "$env:LOCALAPPDATA\Microsoft\Internet Explorer\Recovery\Active" -Recurse -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $totalFiles++
    $totalSize += $_.Length
    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue $_.FullName
}

# Clear Steam temp files
Get-ChildItem "$env:APPDATA\Steam\Temp" -Recurse -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $totalFiles++
    $totalSize += $_.Length
    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue $_.FullName
}

# Clear Defender temp files
Get-ChildItem "$env:ProgramData\Microsoft\Windows Defender\Scans\History\Service\DetectionHistory", "$env:ProgramData\Microsoft\Windows Defender\Scans\History\Service\Resource" -Recurse -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $totalFiles++
    $totalSize += $_.Length
    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue $_.FullName
}

# Clear Startup folder
Get-ChildItem "$env:ProgramData\Microsoft\Windows\Start Menu\Programs\Startup" -Recurse -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $totalFiles++
    $totalSize += $_.Length
    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue $_.FullName
}

# Clear App Repository state
Get-ChildItem "$env:ProgramData\Microsoft\Windows\AppRepository\StateRepository-Machine.srd", "$env:ProgramData\Microsoft\Windows\AppRepository\StateRepository-Machine.srd.old", "$env:ProgramData\Microsoft\Windows\AppRepository\StateRepository-Machine.srd.temp" -Recurse -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $totalFiles++
    $totalSize += $_.Length
    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue $_.FullName
}

# Clear Package Repository state
Get-ChildItem "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd", "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.old", "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.temp" -Recurse -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $totalFiles++
    $totalSize += $_.Length
    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue $_.FullName
}

# Clear Package Repository log files
Get-ChildItem "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log", "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log.old", "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log.temp" -Recurse -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $totalFiles++
    $totalSize += $_.Length
    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue $_.FullName
}

# Clear Package Repository log XML files
Get-ChildItem "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log.xml", "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log.xml.old", "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log.xml.temp" -Recurse -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $totalFiles++
    $totalSize += $_.Length
    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue $_.FullName
}

# Clear Package Repository log XML log files
Get-ChildItem "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log.xml.log", "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log.xml.log.old", "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log.xml.log.temp" -Recurse -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $totalFiles++
    $totalSize += $_.Length
    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue $_.FullName
}

# Clear Package Repository log XML log XML files
Get-ChildItem "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log.xml.log.xml", "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log.xml.log.xml.old", "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log.xml.log.xml.temp" -Recurse -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $totalFiles++
    $totalSize += $_.Length
    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue $_.FullName
}

# Clear Package Repository log XML log XML log files
Get-ChildItem "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log.xml.log.xml.log", "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log.xml.log.xml.log.old", "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log.xml.log.xml.log.temp" -Recurse -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $totalFiles++
    $totalSize += $_.Length
    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue $_.FullName
}

# Clear Package Repository log XML log XML log XML files
Get-ChildItem "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log.xml.log.xml.log.xml", "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log.xml.log.xml.log.xml.old", "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log.xml.log.xml.log.xml.temp" -Recurse -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $totalFiles++
    $totalSize += $_.Length
    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue $_.FullName
}

# Clear Package Repository log XML log XML log XML log files
Get-ChildItem "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log.xml.log.xml.log.xml.log", "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log.xml.log.xml.log.xml.log.old", "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-Machine.srd.log.xml.log.xml.log.xml.log.temp" -Recurse -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $totalFiles++
    $totalSize += $_.Length
    Remove-Item -Force -Recurse -ErrorAction SilentlyContinue $_.FullName
}

# Clear Package Repository log XML log XML log XML log XML files
Get-ChildItem "$env:ProgramData\Microsoft\Windows\AppRepository\PackageRepository-
```
