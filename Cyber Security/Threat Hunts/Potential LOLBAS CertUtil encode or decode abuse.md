# Potential LOLBAS CertUtil encode/decode abuse
Living Off the Land Binaries And Scripts are a type of activity that misuses tools and executables that are already there because they are part of the operating system. In this case, Certutil.exe is being used to encode or decode a file. This can be an indication of malicious activity, since certutil is not often used for this. Investigate this to determine if it was legitimate activity or not. 

### References: 
https://lolbas-project.github.io/lolbas/Binaries/Certutil/
https://www.sentinelone.com/blog/malware-living-off-land-with-certutil/

# KQL:
```kql
//Created by Christopher Iwen for on 08/28/2023
let CertutilEncodeDecode = @'(?i)(.*)(certutil)(.+)((-en|-de)code)(.+)'
; 
let SEvent = SecurityEvent
| where CommandLine matches regex CertutilEncodeDecode
;
let DEvent = DeviceEvents
| where InitiatingProcessCommandLine matches regex CertutilEncodeDecode or ProcessCommandLine matches regex CertutilEncodeDecode 
;
let DPEvent = DeviceProcessEvents
| where InitiatingProcessCommandLine matches regex CertutilEncodeDecode or ProcessCommandLine matches regex CertutilEncodeDecode 
;
let DFEvent = DeviceFileEvents
| where InitiatingProcessCommandLine matches regex CertutilEncodeDecode 
;
let DREvent = DeviceRegistryEvents
| where InitiatingProcessCommandLine matches regex CertutilEncodeDecode 
;
let SLog = Syslog
| where SyslogMessage matches regex CertutilEncodeDecode
; 
SEvent
| join kind=fullouter (SLog) on TimeGenerated
| join kind=fullouter (DPEvent) on TimeGenerated
| join kind=fullouter (DFEvent) on TimeGenerated
| join kind=fullouter (DREvent) on TimeGenerated
| join kind=fullouter (DEvent) on TimeGenerated
```