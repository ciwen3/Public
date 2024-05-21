# Potentially Malicious LNK File
### EXECUTIVE SUMMARY
An LNK file is a windows shortcut used as a pointer to a file, folder, or application containing metadata like a path to the target application and arguments to run that application. LNK files can execute the targeted applications, so threat actors started to use this feature of LNK files to execute malicious scripts like PowerShell code. This method helps threat actors to bypass traditional security solutions.

Threat Actors have been increasingly using malicious LNK files to gain a foothold in networks and start their attacks.  This technique has been used by lots of threat actors like IcedID, Qakbot, Emotet, and Bumblebee. LNK files have also been employed by advanced persistent threat (APT) groups like Gamaredon (aka Armageddon) in its attacks aimed at Ukrainian government entities.

While there are already tools available to make LNK files, some malware developers took it one step further and created a tool being sold on the dark web specifically for creating malicious LNK files known as Quantum. It allows other criminals to create malicious files with extra capabilities such as UAC bypass, delayed execution, post-execution hiding, and a variety of double extensions.

### Hypothesis
Using known tactics, techniques, and procedures (TTPs) for threat actors using LNK files (Windows Shortcuts) we are able hunt for malicious LNK files running code, connecting to remote devices (like staging servers or C2 servers). 

## MITRE ATT&CK
    • Obfuscated Files or Information
        ◦ Obfuscated Files or Information: LNK Icon Smuggling
    • Execution
        ◦ User Execution: Malicious File
    • Lateral Movement
        ◦ Taint Shared Content

## TECHNICAL SUMMARY
### Overview
The Malicious LNK files are often used to download other files, run installed programs, or run malicious code (scripts). Below is the content of an LNK file used by Qakbot. It downloads a DLL from a remote location and executes it.

### Threat Description 
Malicious LNK files are usually the start of an attack or used to maintain persistence on a network. They are often sent via email to unsuspecting end users. Often the Threat Actors take advantage of the way windows will hide file extensions, to trick the user into clicking the file. This allows a file named ImportantDocument.pdf.lnk to show up on the system as ImportantDocument.pdf. When the user clicks on the LNK file, it does its hidden actions. This could be anything like running a malicious file download with it, mounting iso, downloading new files from the internet, opening remote connections, etc. 

### Prevention Recommendations
The best mitigation for malicious LNK files is to block them from being received via email when possible.

### Mitigation Recommendations
The best mitigation for malicious LNK files is to isolate the device that it was discovered on. Validate where it came from and check to see if anyone else may have encountered the Malicious LNK file. User accounts should have their passwords reset and all activities since the LNK file was used scrutinized. Since malicious LNK files are usually the start of an attack the investigation would expand from here depending on what the LNK file was doing. Any IOCs identified should be searched for across the network. 

### References 
    1. https://thehackernews.com/2022/06/new-quantum-builder-lets-attackers.html
    2. https://www.docguard.io/lnk-file-based-attacks-are-on-the-rise/
    3. https://intezer.com/blog/malware-analysis/how-threat-actors-abuse-lnk-files/
    4. https://attack.mitre.org/tactics/TA0002/
    5. https://attack.mitre.org/techniques/T1204/002/
    6. https://attack.mitre.org/techniques/T1027/
    7. https://attack.mitre.org/techniques/T1027/012/

### Notes
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