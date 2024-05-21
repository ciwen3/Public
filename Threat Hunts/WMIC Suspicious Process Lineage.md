# WMIC Suspicious Process Lineage
This analytic will look for Potential WMIC Abuse. Windows Management Instrumentation Command retrieves a huge range of information about local or remote computers. It makes configuration changes to multiple remote machines. The WMIC is a deprecated tool as of 2021. While it is unlikely to stop working for a few years, no new features will be added and it may eventually be removed. WMIC is a Feature on Demand (FoD) that's preinstalled by default in Windows 11. 

For decoding a command see: https://gchq.github.io/CyberChef/
For better understanding of the WMIC command see: https://ss64.com/nt/wmic.html

### Things of Note: 
    - /NODE: which is used to connect to remote devices. this can show up in any of the scenarios. 
    - /FORMAT: Executes JScript or VBScript embedded in the target remote XSL stylesheet.

### Suspicious process lineage :
In general, trusted binaries and known administrative tools and processes will initiate WMI activity. As such, it makes sense to look for known bad processes launching WMI or deviations from the expected where a legitimate but unusual Windows binary spawns WMI—or spawns from it. may require tuning to prevent high volumes of false positives.

Our query is looking for WMIC to spawn "rundll32", "msbuild", "powershell", "cmd", or "mshta". This requires understanding the command. using co pilot might help to get a summary of what the command is doing. 

### Red Flags: 
1. reaching out to the internet 
    - can ignore internal IP address or loopback IP (127.0.0.1)
2. obfuscated code (base64, rot13, etc) https://gchq.github.io/CyberChef/
3. any kind of encryption taking place on the device


# KQL:
```kql
//Suspicious process lineage Generic
let SusProcess = dynamic(["rundll32", "msbuild", "powershell", "cmd", "mshta"]);
let Allowed = dynamic(["start_eng.bat", "C:\\WINDOWS\\CCM", "C:\\WINDOWS\\ccmcache", "appcmd.exe", "Install-Edge.ps1", "nessus", "WindowsDefenderATPOnboardingScript.cmd", "ScanForFiles.ps1", "Deploy_DCU_5.1.ps1", "C:\\ProgramData\\Microsoft\\Windows Defender Advanced Threat Protection\\DataCollection", "OldAlertus.ps1", "Restart Services.ps1", "SoftwareLicenseAzure.ps1", "PolyLens Install.ps1", "RestartHealthService.ps1", "svc_servicenow", "WSUS_Clean.ps1", "Server Manager Performance Monitor", "\\Machine\\Scripts\\Startup\\ipamprovisioning.ps1"]); //specific allowed parameters
let Accounts = dynamic([]); // accounts we want to allow like service accounts ie. svc_servicenow
let DEvents = DeviceEvents
| where InitiatingProcessFileName contains "wmiprvse" and ProcessCommandLine has_any (SusProcess)
;
let DPEvents = DeviceProcessEvents
| where InitiatingProcessFileName contains "wmiprvse" and ProcessCommandLine has_any (SusProcess)
;
DEvents
| join kind=fullouter (DPEvents) on TimeGenerated
| extend InitiatingProcessCommandLine = coalesce(InitiatingProcessCommandLine, InitiatingProcessCommandLine1)
| extend ProcessCommandLine = coalesce(ProcessCommandLine, ProcessCommandLine1)
| extend TimeGenerated = coalesce(TimeGenerated, TimeGenerated1)
| extend DeviceName = coalesce(DeviceName, DeviceName1)
| extend AccountName = coalesce(AccountName, AccountName1)
| extend InitiatingProcessAccountName = coalesce(InitiatingProcessAccountName, InitiatingProcessAccountName1)
| extend InitiatingProcessAccountUpn = coalesce(InitiatingProcessAccountUpn, InitiatingProcessAccountUpn1)
| where not(ProcessCommandLine has_any (Allowed))
| extend B64decoded = base64_decode_tostring(extract(@"(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$", 0, ProcessCommandLine))
| where B64decoded !contains "nessus" //Known scanner used by lots of clients that makes this noisy
| where not(AccountName has_any (Accounts))
```
