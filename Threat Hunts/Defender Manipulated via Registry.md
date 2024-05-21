# Defender Manipulated via Registry

All threat actors try to avoid being detected for as long as possible to achieve their ultimate goals. These defense evasion techniques often include uninstalling, disabling, or manipulating security software. Hackers often target Defender because it comes as the default Windows antimalware tool and is often the first line of defense against their attacks. There are many ways to impair the defenses and achieve the same goal. These techniques often include running one of several possible commands or editing security related registry keys that disable or hinder Defender. Meteor, QakBot, StrongPity, Indrik Spider, and WhisperGate have been observed manipulating Defender exclusion list to bypass antimalware protections without having to disable or remove any antimalware tools. Agent Tesla, Babuk, Conficker, FIN6, H1N1, Ryuk, and TrickBot are just a small sample of threat actors that have used disabling antivirus software on victim computers as a tactic to further their offensive goals. 

# KQL:
```kql
//Defender Registry Change
let DefenderReg = @'(?i)(.*reg add )(.*)(HKLM|HKEY_LOCAL_MACHINE)((\\SOFTWARE\\Policies\\Microsoft\\(Microsoft|Windows) Defender)|(\\SOFTWARE\\Microsoft\\Security Center))(.+)(\/v )(.*)(DisableBehaviorMonitoring|DisableAntiSpyware|AntiSpywareOverride)(.*)(\/t REG_(D)?WORD \/d.*1.*)'
;  
let SEvent = SecurityEvent
//| where TimeGenerated >= ago(90d)
| where CommandLine matches regex DefenderReg
;
let DEvent = DeviceEvents
//| where TimeGenerated >= ago(90d)
| where InitiatingProcessCommandLine matches regex DefenderReg or ProcessCommandLine matches regex DefenderReg 
;
let DPEvent = DeviceProcessEvents
//| where TimeGenerated >= ago(90d)
| where InitiatingProcessCommandLine matches regex DefenderReg or ProcessCommandLine matches regex DefenderReg 
;
let DFEvent = DeviceFileEvents
//| where TimeGenerated >= ago(90d)
| where InitiatingProcessCommandLine matches regex DefenderReg 
;
let DREvent = DeviceRegistryEvents
//| where TimeGenerated >= ago(90d)
| where InitiatingProcessCommandLine matches regex DefenderReg 
;
let SLog = Syslog
//| where TimeGenerated >= ago(90d)
| where SyslogMessage matches regex DefenderReg
; 
SEvent
| join kind=fullouter (SLog) on TimeGenerated
| join kind=fullouter (DPEvent) on TimeGenerated
| join kind=fullouter (DFEvent) on TimeGenerated
| join kind=fullouter (DREvent) on TimeGenerated
| join kind=fullouter (DEvent) on TimeGenerated
| extend InitiatingProcessCommandLine = coalesce(InitiatingProcessCommandLine, InitiatingProcessCommandLine1, InitiatingProcessCommandLine2, InitiatingProcessCommandLine3)
| extend ProcessCommandLine = coalesce(ProcessCommandLine, ProcessCommandLine1, SyslogMessage)
| extend TimeGenerated = coalesce(TimeGenerated, TimeGenerated1, TimeGenerated2, TimeGenerated3, TimeGenerated4, TimeGenerated5)
| extend DeviceName = coalesce(DeviceName, DeviceName1, DeviceName2, DeviceName3, Computer, Computer1)
| extend AccountName = coalesce(AccountName, AccountName1, AccountName2)
| extend InitiatingProcessAccountName = coalesce(InitiatingProcessAccountName, InitiatingProcessAccountName1, InitiatingProcessAccountName2)
| extend InitiatingProcessAccountUpn = coalesce(InitiatingProcessAccountUpn, InitiatingProcessAccountUpn1, InitiatingProcessAccountUpn2)
```
