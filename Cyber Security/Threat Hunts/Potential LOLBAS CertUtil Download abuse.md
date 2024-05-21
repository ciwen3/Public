# Potential LOLBAS CertUtil Download abuse

Living Off the Land Binaries And Scripts are a type of activity that misuses tools and executables that are already there because they are part of the operating system. In this case, Certutil.exe is being used to download things from the internet. While the tool is capable of doing that, it is not standard practice and should be investigated to determine if it was legitimate activity or not. 

### References: 
https://lolbas-project.github.io/lolbas/Binaries/Certutil/
https://www.sentinelone.com/blog/malware-living-off-land-with-certutil/
https://www.bleepingcomputer.com/forums/t/674836/locking-down-certutil/

# KQL:
```kql
//Created by Christopher Iwen on 08/28/2023
let CertutilDownloadAbuse = @'(?i)(.*)(certutil)(.+)(-urlcache|-verifyctl)(.+)(-split)(.+)'
; 
let SEvent = SecurityEvent
| where CommandLine matches regex CertutilDownloadAbuse
;
let DEvent = DeviceEvents
| where InitiatingProcessCommandLine matches regex CertutilDownloadAbuse or ProcessCommandLine matches regex CertutilDownloadAbuse 
;
let DPEvent = DeviceProcessEvents
| where InitiatingProcessCommandLine matches regex CertutilDownloadAbuse or ProcessCommandLine matches regex CertutilDownloadAbuse 
;
let DFEvent = DeviceFileEvents
| where InitiatingProcessCommandLine matches regex CertutilDownloadAbuse 
;
let DREvent = DeviceRegistryEvents
| where InitiatingProcessCommandLine matches regex CertutilDownloadAbuse 
;
let SLog = Syslog
| where SyslogMessage matches regex CertutilDownloadAbuse
; 
SEvent
| join kind=fullouter (SLog) on TimeGenerated
| join kind=fullouter (DPEvent) on TimeGenerated
| join kind=fullouter (DFEvent) on TimeGenerated
| join kind=fullouter (DREvent) on TimeGenerated
| join kind=fullouter (DEvent) on TimeGenerated
```