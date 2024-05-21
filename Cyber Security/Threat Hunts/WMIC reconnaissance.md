# WMIC reconnaissance
This analytic will look for Potential WMIC Abuse. Windows Management Instrumentation Command retrieves a huge range of information about local or remote computers. Makes configuration changes to multiple remote machines. The WMIC is a deprecated tool as of 2021. While it is unlikely to stop working for a few years, no new features will be added and it may eventually be removed. WMIC is a Feature on Demand (FoD) that's preinstalled by default in Windows 11. 

For decoding a command see: https://gchq.github.io/CyberChef/
For better understanding of the WMIC command see: https://ss64.com/nt/wmic.html

### Things of Note: 
    - /NODE: which is used to connect to remote devices. this can show up in any of the scenarios. 
    - /FORMAT: Executes JScript or VBScript embedded in the target remote XSL stylesheet.

### WMIC reconnaissance:
Reconnaissance is harder to detect because it looks very similar to normal admin behavior. A relatively high volume of adversaries leveraging WMI to quickly gather domain information such as system updates, antivirus installed, users, groups, or computers in the domain. There is a chance this could be normal admin activity so this may require checking with the client to verify. This query is looking for WMIC to a command with one of the following '\ldap', 'ntdomain', 'AntiVirusProduct', or 'qfe list'.

Check which user did this activity. 
    - is this common activity for this user? 
    - when in doubt check with client to see. can add automation or edit analytic to ignore approved users. 

check activity done surrounding this. 
    - was there other suspicious activity? 
    - was any data exfiltrated?
    - was any software installed? 
    - were any other commands run by the same user or on the same device? 

### Example Reconnaissance commands: 
```wmic qfe list```

The QFE here stands for “Quick Fix Engineering”, and will return a list of all KB updates (https://www.catalog.update.microsoft.com/Search.aspx?q=KB) installed on the system. This is helpful to Threat Actors because they can see what updates are missing and use that to find a known vulnerability that has not been patched. 

```wmic share list```

The result will also include hidden shares (named with a $ at the end). Share drives are an easy way to distribute malware to an entire company.

# KQL:
```kql
//WMI reconnaissance
let reconList = dynamic(['\\ldap', 'ntdomain', 'AntiVirusProduct', 'qfe list'])
;
let DEvents = DeviceEvents
| where InitiatingProcessFileName contains "wmic" and InitiatingProcessCommandLine has_any (reconList)
;
let DPEvents = DeviceProcessEvents
| where InitiatingProcessFileName contains "wmic" and InitiatingProcessCommandLine has_any (reconList)
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
