# Potential LOLBAS MSHTA running HTA file
This will flag MSHTA.exe being used to run .hta files, which needs to be validated as safe or malicious. HTA files are common. HTA files that run from the users Download or Temp file might be an indication of unauthorized use. It is a common tactic for hackers to trick an end user into downloading and running the HTA file by double clicking it. When this happens the file is usually saved in the Downloads folder. Running from a Temp folder could be an indication of a malicious user running commands on their system. Sometimes legitimate software will run HTA files from a temp folder while doing updates. Research will be necessary to determine if it is legitimate use or not. 

### Red flags: 
Downloading additional things from the internet (especially programs or iso files), Changing registry keys, Disabling antivirus, etc. If you see something suspicious then flag it, if needed ask an L2 or an L3 to review the information. 

### Example Malicious Command:
"mshta.exe" "C:\Users\UserName\Downloads\PROD_Start_DriverPack.hta"

### References:
1.	https://lolbas-project.github.io/lolbas/Binaries/Mshta/
2.	https://community.cymulate.com/community-guide-32/how-to-use-mitigation-steps-to-block-mshta-execution-scenarios-773
3.	https://support.microsoft.com/en-us/windows/change-default-programs-in-windows
4.	https://nandocs.com/en/windows/default-file-associations-extension-windows-11

# KQL:
```kql
let SketchyLocation = dynamic(['download', 'downloads', 'temp', 'tmp']);
let HtaFile = @'(?i)(.*)(mshta)(.+\.hta)(\"|\s)'; 
let SEvent = SecurityEvent
//| where TimeGenerated >= ago(90d)
| where CommandLine matches regex HtaFile and CommandLine has_any (SketchyLocation)
;
let DEvent = DeviceEvents
//| where TimeGenerated >= ago(90d)
| where InitiatingProcessCommandLine matches regex HtaFile and InitiatingProcessCommandLine has_any (SketchyLocation) or (ProcessCommandLine matches regex HtaFile and ProcessCommandLine has_any (SketchyLocation))
;
let DPEvent = DeviceProcessEvents
//| where TimeGenerated >= ago(90d)
| where InitiatingProcessCommandLine matches regex HtaFile and InitiatingProcessCommandLine has_any (SketchyLocation) or (ProcessCommandLine matches regex HtaFile and ProcessCommandLine has_any (SketchyLocation))
;
let DFEvent = DeviceFileEvents
//| where TimeGenerated >= ago(90d)
| where InitiatingProcessCommandLine matches regex HtaFile and InitiatingProcessCommandLine has_any (SketchyLocation)
;
let DREvent = DeviceRegistryEvents
//| where TimeGenerated >= ago(90d)
| where InitiatingProcessCommandLine matches regex HtaFile and InitiatingProcessCommandLine has_any (SketchyLocation)
;
let SLog = Syslog
//| where TimeGenerated >= ago(90d)
| where SyslogMessage matches regex HtaFile and SyslogMessage has_any (SketchyLocation)
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
| where ProcessCommandLine !contains "\\AppData\\Local\\Temp\\" 
| where InitiatingProcessCommandLine !contains "\\AppData\\Local\\Temp\\"
```