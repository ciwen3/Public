# THREAT HUNT ADVISORY: 
## Deleting or Resizing Shadow Copies by Ransomware Operations
### Authored by: Christopher Iwen
#### September 29, 2023 

### EXECUTIVE SUMMARY
Ransomware operators want to make sure their victims can’t recover on their own. One way to do this is to remove all back-ups (Shadow Copies) using the command line. These techniques can be seen in recent Ransomware campaigns like the attack on MGM. 

### Hypothesis
Using known Ransomware operators’ tactics, techniques, and procedures (TTPs) for deleting shadow copies we can search for malicious activity that could indicate more nefarious activity is on the horizon.

### MITRE ATT&CK
    • Inhibit System Recovery

## TECHNICAL SUMMARY
### Overview
The Shadow Copy Service is a program which allows manual or automatic backup of computer files and volumes even if they are in use. Shadow copies can be used to restore a system to the shadow copy (snapshot) state. Shadow Copies can be created on local and external volumes by Microsoft Windows from version 8. Deleting or Resizing Shadow Copies (Windows system restore files) is a tactic that is used by many Ransomware groups to prevent victims from recovering the infected system without paying the ransom. Resizing of the Sadow Copies to a small size can lead to all copies getting deleted automatically by the system. Vssadmin and wmic are the most common command line tools used to maliciously delete shadow copies. This step precedes the encryption of files on the infected system.

### Threat Description 
Vssadmin and wmic can be used to destroy backs on a windows system. 

### Mitigation Recommendations
The best mitigation for potential or actively occurring back-up file resizing or deletion, is to back up the shadow copies offline where they can’t be removed. This would allow you to restore even after a malicious attack. Saving a lot of offline backups can be expensive; if cost of remediation is a hinderance, then you should prioritize the most important systems for offline backups.

### References:
    1. https://attack.mitre.org/techniques/T1490/


# Notes: 
```
Deleting or Resizing Shadow Copies (Windows system restore files) is a tactic that is used by many Ransomware groups to prevent victims from recovering the infected system without paying the ransom. Resizing of the Shadow Copies to a small size can lead to all copies getting deleted automatically by the system. vssadmin, wbadmin, and wmic are the most common command line tools used to maliciously delete shadow copies. This step precedes the encryption of files on the infected system.
Check to make sure the command is not normal to run in this environment.
For instance, https://github.com/monosoul/MS-Deployment-toolkit-scripts/blob/master/Scripts/LTICleanup.wsf is a commonly used script that can be used to clean up a windows system. The thing it does is resize shadow copies to a specified size. If commonly used in the clients environment it should show up with some basic KQL and can be verified as expected activity with the client.
```

# KQL:
```kql
let suppression = SecurityAlert // Insight Suppression
    | where TimeGenerated >= ago(14d) // Insight Suppression
    | where AlertName == "Deleting or Resizing Shadow Copies - Insight Custom Threat Hunt" // Insight Suppression
    | mv-expand parse_json(Entities) // Insight Suppression
   | extend HostName_ = tostring(Entities.HostName)
    | where isnotempty(HostName_) // Inisght Suppression
    | distinct HostName_; // Inisght Suppression;
    let DeleteShadow1 = @'(?i)(.*)(vssadmin|wbadmin)(.+)(delete|resize)+(.?)(shadowstorage|shadows|catalog)(.+)'
;
let DeleteShadow2 = @'(?i)(.*)(wmic|Get-WmiObject)(.+)(shadowcopy)(.+)(delete)?'
; 
let SEvent = SecurityEvent
    | where TimeGenerated >= ago(1h)
    | where CommandLine matches regex DeleteShadow1 or CommandLine matches regex DeleteShadow2 
;
let DEvent = DeviceEvents
    | where TimeGenerated >= ago(1h)
    | where DeviceName !in (suppression)
    | where InitiatingProcessCommandLine matches regex DeleteShadow1
        or ProcessCommandLine matches regex DeleteShadow1
        or InitiatingProcessCommandLine matches regex DeleteShadow2
        or ProcessCommandLine matches regex DeleteShadow2 
;
let DPEvent = DeviceProcessEvents
    | where TimeGenerated >= ago(1h)
    | where DeviceName !in (suppression)
    | where InitiatingProcessCommandLine matches regex DeleteShadow1
        or ProcessCommandLine matches regex DeleteShadow1
        or InitiatingProcessCommandLine matches regex DeleteShadow2
        or ProcessCommandLine matches regex DeleteShadow2 
;
let DFEvent = DeviceFileEvents
    | where TimeGenerated >= ago(1h)
    | where DeviceName !in (suppression)
    | where InitiatingProcessCommandLine matches regex DeleteShadow1 or InitiatingProcessCommandLine matches regex DeleteShadow2 
;
let DREvent = DeviceRegistryEvents
     | where TimeGenerated >= ago(1h)
     | where DeviceName !in (suppression)
    | where InitiatingProcessCommandLine matches regex DeleteShadow1 or InitiatingProcessCommandLine matches regex DeleteShadow2 
;
let SLog = Syslog
     | where TimeGenerated >= ago(1h)
    | where SyslogMessage matches regex DeleteShadow1 or SyslogMessage matches regex DeleteShadow2
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
// Some run a clean up program that reduces the size of shadow copies to 5% "C:\***\Scripts\LTICleanup.wsf"
| where InitiatingProcessCommandLine !contains "vssadmin resize shadowstorage" and InitiatingProcessCommandLine !contains "/MaxSize=5%" 
| where ProcessCommandLine !contains "vssadmin resize shadowstorage" and ProcessCommandLine !contains "/MaxSize=5%"
```
