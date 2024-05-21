# Potential LOLBAS CertUtil encode/decode abuse
### EXECUTIVE SUMMARY
Living Off the Land Binaries And Scripts (LOLBAS) have become an important set of tools for Advanced Persistent Threats (APTs) and other sophisticated hackers to use. This is because the tools are already in place, trusted, and have public shared knowledge on how to abuse those tools. 

The CertUtil.exe is a very popular LOLBAS to abuse. CertUtil can be used to encoding or decoding a file, download files from the internet, and save files to alternate data streams. While some of these features have legitimate use it is rarely used to download files because there are more user-friendly ways to download files from the internet. Encoding or decoding a file could be an indication of preparing data for exfiltration or reading obscured data that would be invisible to traditional antivirus software. There is no legitimate reason to save files to alternate data streams other than to hide those files from the users and file system. 

### Hypothesis
Using the data on https://lolbas-project.github.io/lolbas/Binaries/Certutil/ we can craft queries to find malicious activity related to CertUtil.exe.  We will use these queries in Sentinels Log Analytics to hunt for possible malicious activity going back 90 days from the date on this document. If any possible malicious activity is found, we will follow up with an investigation.

## MITRE ATT&CK
    • TA0011: Command and Control
        ◦ T1105: Ingress Tool Transfer
    • TA0005: Defense Evasion
        ◦ T1564.004: NTFS File Attributes
        ◦ T1027: Obfuscated Files or Information
        ◦ T1140: Deobfuscate/Decode Files or Information

## TECHNICAL SUMMARY
### Overview
Highly sophisticated threat actors, often known as Advanced Persistent Threats (APT), look for ways to fly under the radar. This often leads to them abusing legitimate software that already exists in the environment. This activity has been defined as “Living Off the Land” and can be difficult to detect. 

One of the more abused tools is CertUtil.exe. “Certutil.exe is a command-line program, installed as part of Certificate Services. You can use certutil.exe to display certification authority (CA) configuration information, configure Certificate Services, backup and restore CA components. The program also verifies certificates, key pairs, and certificate chains.” (1)

This tool has a lot of legitimate abilities that aren’t used very often, like downloading files from the internet via the command line or encoding and decoding files. The average workstation user will never touch this tool. CertUtil.exe comes from and is signed by Microsoft making it seem like its activity is allowed.  This makes it a prime target for malicious activity. 

### Threat Description 
CertUtil.exe can be used to download malicious files from the internet, can save data to alternate data streams, and can encode or decode files in hexadecimal and base64 for exfiltration or obfuscation. 

### Mitigation Recommendations
If Malicious activity is identified, an Incident Response Analyst should proceed to review the related activity and files to better understand the scope of what happened. This includes reviewing the commands issued by the process, its parent process, what user or permission level the process ran as, and if there are any unusual discrepancies in the process chain.

If a suspicious binary, script, or other artifact is identified in the investigation that is indicative of ransomware or other malicious activity, then it is recommended to quarantine the host from the network and initiate typical incident response measures against such a breach. Hash values, strings, and other indicators of compromise derived from the analysis of the suspicious files and actions can be searched across the environment for the identification of other potentially impacted hosts. 

### Prevention Recommendations
Using the firewall setting in Windows you can block specific tools from connecting to the internet. This would be the easiest and most direct way to block CertUtil.exe from being used to download malicious files from the Internet. 
### References 
    1. https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil
    2. https://lolbas-project.github.io/lolbas/Binaries/Certutil/

### NOTES
Living Off the Land Binaries And Scripts are a type of activity that misuses tools and executables that are already there because they are part of the operating system. In this case, Certutil.exe is being used to encode or decode a file. This can be an indication of malicious activity, since certutil is not often used for this. Investigate this to determine if it was legitimate activity or not. 

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