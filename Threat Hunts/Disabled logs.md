# Disabled logs
Windows Event Logs are a record of a computer's alerts and notifications. Clearing and disabling logs is a common tactic of threat actors to hide their activities from alerting tools like a SIEM (ex. Sentinel, Taegis, etc) that would use these logs for detections and audits. This data is used by security tools and analysts to generate detections. Disabling logging usually happens early on to prevent the system from alerting. Clearing the logs will happen after some identifiable activity to hide the malicious activity. This type of activity has been seen in use by many threat actors, from normal hacking groups like Charming Kitten to government-grade commercial surveillance spyware like FinFisher. For instance, APT29 (aka. NOBELIUM or Cozy Bear) used these tactics in the infamous SolarWinds compromise.

# KQL:
```kql
let DisableLogging = @'(?i)(.*)(((auditpol)(.+)(\/clear|\/remove|(:disable(.*):disable))|(Stop-Service(.*)-Name(.*)EventLog)|(del )?\s\(Get-PSReadlineOption\)\.HistorySavePath))(.*)'
;
SecurityEvent
| where EventID == 4688
| where CommandLine matches regex DisableLogging
| project-reorder CommandLine
```