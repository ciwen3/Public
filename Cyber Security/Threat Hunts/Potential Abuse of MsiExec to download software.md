# Potential Abuse of MsiExec to download software
### EXECUTIVE SUMMARY
MsiExec provides the means to install, modify, and perform operations on Windows Installer from the command line. MsiExec is the command-line utility for the Windows Installer and is thus commonly associated with executing installation packages MSI and MSP files. Msiexec.exe can also execute DLLs.

Adversaries may abuse MsiExec to proxy execution of malicious payloads. MsiExec can be used to bypass application control solutions that do not account for its potential abuse. MsiExec execution may also be elevated to SYSTEM privileges if the AlwaysInstallElevated policy is enabled. MsiExec does not connect to the internet directly, so we expect to see no network calls from MsiExec.

While MsiExec can only install MSI, MSP, and DLL files, it does not check the file extension. This means someone could change the file extension on a piece of MSI, MSP, or DLL malware to easily hide it from the average user. LokiBot, IcedID, Maze, QakBot, and Ragnar Locker have all used MsiExec to install their malware in the past. 

### Hypothesis
Using known tactics, techniques, and procedures (TTPs) for threat actors we can look for commands that initiate network connections from MsiExec. 

## MITRE ATT&CK 
### Tactics:
• Defense Evasion https://attack.mitre.org/tactics/TA0005/

### Techniques:
• System Binary Proxy Execution: MsiExec https://attack.mitre.org/techniques/T1218/007/

## TECHNICAL SUMMARY
### Overview
When functioning properly, MsiExec exhibits the following behavior:
    • Single instance – There is typically only one msiexec.exe process running.
    • Temporary processes – It starts up temporarily to handle installer packages and then shuts down.
    • Child processes – May spawn msiexec.exe child processes when handling nested packages.
    • Low resource usage – Requires little CPU or memory itself. High usage indicates an issue.
    • No network calls – msiexec.exe does not connect to the internet directly.

Location: C:\Windows\System32\msiexec.exe, C:\Windows\SysWOW64\msiexec.exe
Default name: msiexec.exe
Digitally signed by: Microsoft Corporation

Using this information, we can hunt for MsiExec use outside of this context and alert on it as potentially malicious activity.

### Red Flags
    1. external internet connection (add internal IP chart for reference)
        a. check IP or URl on OSINT tools like VT and AbuseIPdb.
        b. Internal IP addresses can be ignored. 
                • NOTE: there will be occasional false positives like the example below. 
            "msiexec.exe" /qb /i 5.10.3.406.msi  <== this is not an IP  address. This is the name of the file. It took me a minute to figure that out. Thankfully that is not a valid IP address (the last octet is 406 and shouldn't go above 255) so there was no doubt. If you are unsure then check it using OSINT tools to verify.  
    2. MsiExec being used to install formats other than .msi, .msp and .dll. MsiExec will only install .msi, .msp and .dll files but a hacker can easily rename the file so that the extension appears as .png or anything else and MsiExec will still run the file. This is because MsiExec doesn't check file extensions and will attempt to install anything it is told to.
    3. When in doubt check with the client. 

Using this information, we can hunt for MsiExec use outside of this context and alert on it as potentially malicious activity.

### Threat Description 
Hackers can abuse MsiExec to help them install malware and potentially bypass security controls. There is a large variation of commands that can accomplish this activity. The main thing that the malicious use of MsiExec have in common is using the tool to install a file from the internet rather than a local or intranet location. Using Regex and KQL we are able to look for this MsiExec internet commands. 

### PREVENTION RECOMMENDATIONS
• Disable or Remove Feature or Program - Consider disabling the AlwaysInstallElevated policy to prevent elevated execution of Windows Installer packages. This can be done in the registry. for more information see: https://learn.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated
• Privileged Account Management - Restrict execution of Msiexec.exe to privileged accounts or groups that need to use it to lessen the opportunities for malicious usage.

### MITIGATION RECOMMENDATIONS
If Malicious activity is identified, an Incident Response Analyst should proceed to review the related activity and files to better understand the scope of what happened. This includes reviewing the commands issued by the process, its parent process, what user and permission level the process ran as, and if there are any unusual discrepancies in the process chain. If a suspicious binary, script, or other artifact is identified in the investigation that is indicative of ransomware or other malicious activity, then it is recommended to quarantine the host from the network and initiate typical incident response measures against such a breach. Hash values, strings, and other indicators of compromise derived from the analysis of the suspicious files and actions can be searched across the environment for the identification of other potentially impacted hosts. If determined to be malicious then the user account that was used to run the commands should have the password reset, authentication token and sessions terminated, and MFA setup if not already in place. The user’s activity while being hijacked by a hacker should be scrutinized very closely to see if there was any attempt to move laterally or abuse the account to compromise another company.

### References
1. https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/msiexec
2. https://lolbas-project.github.io/lolbas/Binaries/Msiexec/
3. https://attack.mitre.org/techniques/T1218/007/
4. https://attack.mitre.org/tactics/TA0005/
5. https://learn.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated
6. https://ss64.com/nt/msiexec.html
7. https://research.splunk.com/endpoint/827409a1-5393-4d8d-8da4-bbb297c262a7/
8. https://malwaretips.com/blogs/remove-msiexec-exe-virus/
9. https://www.trendmicro.com/en_za/research/18/b/attack-using-windows-installer-msiexec-exe-leads-lokibot.html

# KQL:
```kql
// MsiExec connecting to the internet
// looks for http, https, ftp, or ip address connection to install a file
let Msiexec = @'(?i)(.*)msiexec(\.exe)?(")?\s((\/|-)\w+\s?)*(\/|-)(package|i|a|y|z| )+(")?(((http|https|ftp):\/\/)|((\d{1,3}\.){3}\d{1,3}))(.+)'
;
let SEvent = SecurityEvent
| where CommandLine matches regex Msiexec 
;
let DEvent = DeviceEvents
| where InitiatingProcessCommandLine matches regex Msiexec or ProcessCommandLine matches regex Msiexec
;
let DPEvent = DeviceProcessEvents
| where InitiatingProcessCommandLine matches regex Msiexec or ProcessCommandLine matches regex Msiexec
;
let DFEvent = DeviceFileEvents
| where InitiatingProcessCommandLine matches regex Msiexec
;
let DREvent = DeviceRegistryEvents
| where InitiatingProcessCommandLine matches regex Msiexec 
;
let SLog = Syslog
| where SyslogMessage matches regex Msiexec 
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
