# Potential LOLBAS MSHTA running code
This will flag MSHTA.exe being used to run code, which needs to be validated as safe or malicious. The code should be visible in the command line arguments. Red flags would include: Obfuscated code (base64 or other encoding), Downloading things from the internet (especially other commands, programs, or iso files), Changing registry keys, Disabling antivirus, etc. If you see something suspicious then flag it, if needed ask an L2 or an L3 to review the information.

### References:
1.	https://lolbas-project.github.io/lolbas/Binaries/Mshta/
2.	https://community.cymulate.com/community-guide-32/how-to-use-mitigation-steps-to-block-mshta-execution-scenarios-773
3.	https://support.microsoft.com/en-us/windows/change-default-programs-in-windows
4.	https://nandocs.com/en/windows/default-file-associations-extension-windows-11

# KQL:
```kql
let MshtaRunCode = @'(?i)(.*)(mshta)(.+)(javascript:|vbscript:|hta:)'
; 
let SEvent = SecurityEvent
//| where TimeGenerated >= ago(90d)
| where CommandLine matches regex MshtaRunCode
;
let DEvent = DeviceEvents
//| where TimeGenerated >= ago(90d)
| where InitiatingProcessCommandLine matches regex MshtaRunCode or ProcessCommandLine matches regex MshtaRunCode 
;
let DPEvent = DeviceProcessEvents
//| where TimeGenerated >= ago(90d)
| where InitiatingProcessCommandLine matches regex MshtaRunCode or ProcessCommandLine matches regex MshtaRunCode 
;
let DFEvent = DeviceFileEvents
//| where TimeGenerated >= ago(90d)
| where InitiatingProcessCommandLine matches regex MshtaRunCode 
;
let DREvent = DeviceRegistryEvents
//| where TimeGenerated >= ago(90d)
| where InitiatingProcessCommandLine matches regex MshtaRunCode 
;
let SLog = Syslog
//| where TimeGenerated >= ago(90d)
| where SyslogMessage matches regex MshtaRunCode
; 
SEvent
| join kind=fullouter (SLog) on TimeGenerated
| join kind=fullouter (DPEvent) on TimeGenerated
| join kind=fullouter (DFEvent) on TimeGenerated
| join kind=fullouter (DREvent) on TimeGenerated
| join kind=fullouter (DEvent) on TimeGenerated
| extend InitiatingProcessCommandLine = coalesce(InitiatingProcessCommandLine, InitiatingProcessCommandLine1, InitiatingProcessCommandLine2, InitiatingProcessCommandLine3)
| extend ProcessCommandLine = coalesce(ProcessCommandLine, ProcessCommandLine1)
| extend TimeGenerated = coalesce(TimeGenerated, TimeGenerated1, TimeGenerated2, TimeGenerated3, TimeGenerated4, TimeGenerated5)
| extend DeviceName = coalesce(DeviceName, DeviceName1, DeviceName2, DeviceName3, Computer, Computer1)
| extend AccountName = coalesce(AccountName, AccountName1, AccountName2)
| extend InitiatingProcessAccountName = coalesce(InitiatingProcessAccountName, InitiatingProcessAccountName1, InitiatingProcessAccountName2)
| extend InitiatingProcessAccountUpn = coalesce(InitiatingProcessAccountUpn, InitiatingProcessAccountUpn1, InitiatingProcessAccountUpn2)
```