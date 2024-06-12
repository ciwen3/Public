# SonicWall finding Botnet Connections that haven't been dropped by Firewall
```
//for analytics
CommonSecurityLog
| where DeviceVendor == "SonicWall"
| where IndicatorThreatType == "Botnet"
| where Activity == "Connection Opened" or Activity == "Connection Closed"
| summarize Connection=make_set(Activity) by Computer, MaliciousIPCountry, SourceIP, SourcePort, DestinationIP, DestinationPort, Protocol, ThreatSeverity, ThreatConfidence
| where Connection !contains "Connection Closed"
```
```
//for runbook
CommonSecurityLog
| where DeviceVendor == "SonicWall"
| where IndicatorThreatType == "Botnet"
| where Activity == "Connection Opened" or Activity == "Connection Closed"
| where Computer == "<Computer Name>" and SourceIP == "<Malicious IP>"
```
