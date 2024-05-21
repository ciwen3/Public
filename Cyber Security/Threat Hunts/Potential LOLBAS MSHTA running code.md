# Potential LOLBAS MSHTA running code
### EXECUTIVE SUMMARY
Living Off the Land Binaries And Scripts (LOLBAS) have become an important set of tools for Advanced Persistent Threats (APTs) and other sophisticated hackers to use. This is because the tools are already in place, trusted, and have public shared knowledge on how to abuse those tools. 

Mshta.exe is a Windows-native binary that can execute Windows Script Host code (VBScript and JScript) embedded within HTML or an HTA (HTML Application) file. Because the HTA file is a relatively unknown file format most end users don't know how dangerous it can be. Double clicking the HTA file will automatically run it with MSHTA.exe. The relative ease of running HTA files, delivering the files, and obscurity of file format make it a reliable technique during both initial and later stages of a malicious attack.

### Hypothesis
Using the data on https://lolbas-project.github.io/lolbas/Binaries/Mshta/ we can craft queries to find malicious activity related to MSHTA.exe.  We will use these queries in Sentinels Log Analytics to hunt for possible malicious activity going back 90 days from the date on this document. If any possible malicious activity is found, we will follow up with an investigation.

## MITRE ATT&CK
    • Defense Evasion
        ◦ System Binary Proxy Execution
            ▪ System Binary Proxy Execution: Mshta
    • Ingress Tool Transfer
        ◦ Command and Control

## TECHNICAL SUMMARY
### Overview
Highly sophisticated threat actors, often known as Advanced Persistent Threats (APTs), look for ways to fly under the radar. This often leads to them abusing legitimate software that already exists in the environment. This activity has been defined as “Living Off the Land” and can be difficult to detect. 

One of the more commonly abused tools is MSHTA.exe. MSHTA.exe is a trustworthy file from Microsoft and a Windows core system program. This tool has legitimate uses and is often seen in websites that need to run code or software updates. MSHTA.exe can execute a payload hosted remotely. It can be run from the command line but is more often run by tricking end users into clicking on the malicious file or browsing to a website with the malicious code embedded. The ability of the malicious code is only limited by the hackers’ abilities and the sophistication of antivirus/EDR installed on the device. This could include anything from disabling antivirus software, changing registry keys, or dumping passwords, just to name a few known techniques. 

### Threat Description 
MSHTA.exe can be used to download malicious files from the internet, can save data to alternate data streams, and can run malicious code directly or in an HTA file. 

### Mitigation Recommendations
If Malicious activity is identified, an Incident Response Analyst should proceed to review the related activity and files to better understand the scope of what happened. This includes reviewing the commands issued by the process, its parent process, what user or permission level the process ran as, and if there are any unusual discrepancies in the process chain.

If a suspicious binary, script, or other artifact is identified in the investigation that is indicative of ransomware or other malicious activity, then it is recommended to quarantine the host from the network and initiate typical incident response measures against such a breach. Hash values, strings, and other indicators of compromise derived from the analysis of the suspicious files and actions can be searched across the environment for the identification of other potentially impacted hosts. 

### Prevention Recommendations
MSHTA can be locked down using Local Group Policy settings. Depending on your environment it might not be feasible to do this on all computers. It depends on whether you expect HTA code to be run on the computer or not. This may require some research and validation to determine which machines would be suitable for completely blocking this activity. 

Alternatively, you can change the default application that handles HTA file from MSHTA.exe to something less capable of being abused like Notepad.exe. This would mean that double clicking the file would open the text in Notepad rather than executing the code in the file. This can be done manually on individual devices or with GPO. 

### References 
    1. https://lolbas-project.github.io/lolbas/Binaries/Mshta/
    2. https://community.cymulate.com/community-guide-32/how-to-use-mitigation-steps-to-block-mshta-execution-scenarios-773
    3. https://support.microsoft.com/en-us/windows/change-default-programs-in-windows
    4. https://nandocs.com/en/windows/default-file-associations-extension-windows-11


### NOTES
This will flag MSHTA.exe being used to run code, which needs to be validated as safe or malicious. The code should be visible in the command line arguments. Red flags would include: Obfuscated code (base64 or other encoding), Downloading things from the internet (especially other commands, programs, or iso files), Changing registry keys, Disabling antivirus, etc. If you see something suspicious then flag it, if needed ask an L2 or an L3 to review the information.

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