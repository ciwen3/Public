# Office products spawning WMIC
This analytic will look for Potential WMIC Abuse. Windows Management Instrumentation Command retrieves a huge range of information about local or remote computers. Makes configuration changes to multiple remote machines. The WMIC is a deprecated tool as of 2021. While it is unlikely to stop working for a few years, no new features will be added and it may eventually be removed. WMIC is a Feature on Demand (FoD) that's preinstalled by default in Windows 11. 

- For decoding a command see: https://gchq.github.io/CyberChef/
- For better understanding of the WMIC command see: https://ss64.com/nt/wmic.html

### Things of Note: 
    - /NODE: which is used to connect to remote devices. this can show up in any of the scenarios. 
    - /FORMAT: Executes JScript or VBScript embedded in the target remote XSL stylesheet.

### Office products spawning WMIC:
It’s almost always malicious when wmic.exe spawns as a child process of Microsoft Office and similar products. As such, it makes sense to examine the chain of execution and follow-on activity when this occurs.

Office apps shouldn't run WMIC commands. This should be reported right away. if this is happening it is likely a "macro" setup on the office file. Malicious macros are often used. the only exception I have seen is when the command run was something like opening excel without any additional parameters. 

### Red Flags: 
1. reaching out to the internet 
2. obfuscated code (base64, rot13, etc)
3. any kind of encryption taking place on the device

### Reference:
https://services-na.insight.com/now/nav/ui/classic/params/target/kb_view.do%3Fsys_kb_id%3D0376e53593014a50cf8730384dba10bd%26sysparm_rank%3D1%26sysparm_tsqueryId%3Dfc40941293ed4a1050873bba6aba105c

# KQL:
```kql
//Office products spawning WMI
let OfficeApp = dynamic(['winword.exe', 'excel.exe', 'outlook.exe'])
;
let DEvents = DeviceEvents
| where InitiatingProcessFileName has_any (OfficeApp) and FileName contains "wmic"
;
let DPEvents = DeviceProcessEvents
| where InitiatingProcessFileName has_any (OfficeApp) and FileName contains "wmic"
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
```
