# Disabled logs
### EXECUTIVE SUMMARY
Windows Event Logs are a record of a computer's alerts and notifications. Clearing and disabling logs is a common tactic of threat actors to hide their activities from alerting tools like a SIEM (ex. Sentinel, Taegis, etc) that would use these logs for detections and audits. This data is used by security tools and analysts to generate detections. Disabling logging usually happens early on to prevent the system from alerting. Clearing the logs will happen after some identifiable activity to hide the malicious activity. This type of activity has been seen in use by many threat actors, from normal hacking groups like Charming Kitten to government-grade commercial surveillance spyware like FinFisher. For instance, APT29 (aka.
NOBELIUM or Cozy Bear) used these tactics in the infamous SolarWinds compromise.

### HYPOTHESIS
Using known tactics, techniques, and procedures (TTPs) for threat actors disabling and clearing logfiles we can track these activities.

## MITRE ATT&CK
### Tactics:
- Defense Evasion https://attack.mitre.org/tactics/TA0005/

### Techniques:
- Indicator Removal https://attack.mitre.org/techniques/T1070/
- Indicator Removal: Clear Windows Event Logs https://attack.mitre.org/techniques/T1070/001/
- Impair Defenses https://attack.mitre.org/techniques/T1562/
- Impair Defenses: Disable Windows Event Logging https://attack.mitre.org/techniques/T1562/002/
- Impair Defenses: Impair Command History Logging https://attack.mitre.org/techniques/T1562/003/

## TECHNICAL SUMMARY
### OVERVIEW
Logging allows tools to create alerts that can be investigated. Without the logs no alerting will happen and threat actors would be able to get away with a lot more malicious activity. We will be looking for activity related to the event logging service being shut down, the security audit log getting cleared. Either of these could cause a blind spot in the logs that prevents detection.

### THREAT DESCRIPTION
Using the command line and tools like “wevtutil” and “auditpol” threat actors can hide their actions to prevent security professionals from catching them.

### PREVENTION RECOMMENDATIONS
To prevent malicious use your company can set Group Policies that enable logging to make sure logging is turned on. Ensure proper process and file permissions are in place to prevent adversaries from disabling or interfering with logging or deleting or modifying .evtx logging files. Ensure proper user and Registry permissions are in place to prevent adversaries from disabling or interfering with logging.

### MITIGATION RECOMMENDATIONS
If malicious then client should start investigation into how and why this activity took place. If the user doesn’t have any knowledge of doing this activity and it isn’t associated with a scheduled task, then they should consider the users account possibly compromised and take appropriate actions, like logging the user out of all connections, resetting passwords, setting up MFA, and monitoring the user closely for a while. If the user was compromised then they should investigate what activity was done under that user’s account, expanding the search as needed.

### command to turn logging back on:
AUDITPOL /SET /CATEGORY:* /SUCCESS:ENABLE /FAILURE:ENABLE

### References
1. https://attack.mitre.org/tactics/TA0005/
2. https://attack.mitre.org/techniques/T1070/
3. https://attack.mitre.org/techniques/T1070/001/
4. https://attack.mitre.org/techniques/T1562/
5. https://attack.mitre.org/techniques/T1562/002/
6. https://attack.mitre.org/techniques/T1562/003/

# KQL:
```kql
let DisableLogging = @'(?i)(.*)(((auditpol)(.+)(\/clear|\/remove|(:disable(.*):disable))|(Stop-Service(.*)-Name(.*)EventLog)|(del )?\s\(Get-PSReadlineOption\)\.HistorySavePath))(.*)'
;
SecurityEvent
| where EventID == 4688
| where CommandLine matches regex DisableLogging
| project-reorder CommandLine
```
