# LOLBAS CertUtil Alt Data Stream Abuse

Living Off the Land Binaries And Scripts are a type of activity that misuses tools and executables that are already there because they are part of the operating system. In this case, Certutil.exe is being used to download things from the internet to an altername datastream. This should be treated as a P1. There is no legitimate reason to download to an alternate data stream. This is a technique often employeed by malicious actors to hide files on a target system. The alternate data stream won't show up in a normal file viewer. 

To view the hidden data streams in CMD run the following command in the folder that alternate data stream is expected to be. 
CMD: "dir /r"

### References: 
https://infosecwriteups.com/alternate-data-streams-ads-54b144a831f1
https://lolbas-project.github.io/lolbas/Binaries/Certutil/
https://www.sentinelone.com/blog/malware-living-off-land-with-certutil/
https://www.bleepingcomputer.com/forums/t/674836/locking-down-certutil/

# KQL:
```kql
//Created by Christopher Iwen for Insight on 08/28/2023
let CertutilAltDataStream = @'(?i)(.*)(certutil)(.+)(\s([a-z]\:\\)?\w+(\:)\w+\s)'
; 
let SEvent = SecurityEvent
| where CommandLine matches regex CertutilAltDataStream
;
let DEvent = DeviceEvents
| where InitiatingProcessCommandLine matches regex CertutilAltDataStream or ProcessCommandLine matches regex CertutilAltDataStream 
;
let DPEvent = DeviceProcessEvents
| where InitiatingProcessCommandLine matches regex CertutilAltDataStream or ProcessCommandLine matches regex CertutilAltDataStream 
;
let DFEvent = DeviceFileEvents
| where InitiatingProcessCommandLine matches regex CertutilAltDataStream 
;
let DREvent = DeviceRegistryEvents
| where InitiatingProcessCommandLine matches regex CertutilAltDataStream 
;
let SLog = Syslog
| where SyslogMessage matches regex CertutilAltDataStream
; 
SEvent
| join kind=fullouter (SLog) on TimeGenerated
| join kind=fullouter (DPEvent) on TimeGenerated
| join kind=fullouter (DFEvent) on TimeGenerated
| join kind=fullouter (DREvent) on TimeGenerated
| join kind=fullouter (DEvent) on TimeGenerated
```
