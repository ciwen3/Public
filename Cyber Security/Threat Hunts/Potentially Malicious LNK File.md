# Potentially Malicious LNK File
This is looking for potentially malicious lnk files (windows shortcut), by identifying .lnk files that run commands with tools like PowerShell, cmd, mshta, VBScript, etc. with pre-defined arguments or execute commands from another file. It is becoming a common tactic used by Threat Actors because it’s easy to get the victim to click on it without realizing what they did. This will take some research to determine if the activity was malicious, as .lnk files are common for a lot of things. If the .lnk file came to an end user via email it would need extra scrutiny, especially if from a user outside the receiving companies’ organizations. For instance, if the .lnk came in an email sent from a free email account like Gmail or Yahoo (but not limited to these) then it should be considered more of a risk.

# KQL:
```kql
let binary = datatable(filename:string) ["powershell", "cmd", "mshta", "VBScript", "rundll32", "wscript", "wmi"] //any binary that we want to include in the suspicious activity alert 
; 
let binary2 = datatable(filename:string) ['"powershell.exe"', '"powershell.exe" ', '"cmd.exe"']  //app with quotes to rule out any time the lnk call just the app with no arguments 
;
let allowpath = datatable(filename:string) ["start menu", "desktop", "LenovoBatteryGaugeAddin", "C:\\Program Files", "\\AppData\\Roaming\\Microsoft\\Internet Explorer\\Quick Launch"] //] 
;
let allowfile = datatable(filename:string) [] 
;
let allowprocess = datatable(filename:string) ['"WScript.exe" "\\\\stprodsgzbwdfs1.file.core.windows.net\\sgzbwdfs1-dfsdata-dedupe\\DFS\\ADM\\Logon\\GZBW_AD_LogonSkript.vbs"'] // https://www.tenforums.com/tutorials/77458-rundll32-commands-list-windows-10-a.html 
;
DeviceEvents 
| where FileName endswith ".lnk" //looking for lnk files 
| where FileName !endswith "shortcut.lnk" and not(FileName has_any(allowfile)) //these arent trying to hide or have been approved
| where not(FolderPath has_any (allowpath)) 
| where not(InitiatingProcessCommandLine has_any (allowprocess))
| where InitiatingProcessFileName has_any (binary) // actual name of app 
| where InitiatingProcessCommandLine !in~ (binary2) //app with quotes to rule out any time the lnk call just the app with no arguments 
| where not(InitiatingProcessCommandLine contains "zzzzInvokeManagedCustomActionOutOfProc" and InitiatingProcessParentFileName == "msiexec.exe") // https://twitter.com/SBousseaden/status/1388064061087260675?lang=en  
| union (DeviceFileEvents)
| where FileName endswith ".lnk" //looking for lnk files 
| where FileName !endswith "shortcut.lnk" and not(FileName has_any(allowfile)) //these arent trying to hide or have been approved
| where not(FolderPath has_any (allowpath)) 
| where not(InitiatingProcessCommandLine has_any (allowprocess))
| where InitiatingProcessFileName has_any (binary) // actual name of app 
| where InitiatingProcessCommandLine !in~ (binary2) //app with quotes to rule out any time the lnk call just the app with no arguments 
| where not(InitiatingProcessCommandLine contains "zzzzInvokeManagedCustomActionOutOfProc" and InitiatingProcessParentFileName == "msiexec.exe") // https://twitter.com/SBousseaden/status/1388064061087260675?lang=en  

```