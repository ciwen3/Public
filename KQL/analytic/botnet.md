# look for connections from or to known botnets that didn't get disconnected. 
```
// look for connections from or to known botnets that didn't get disconnected. 
// create list of known botnet connections that were closed
let ClosedConnection = CommonSecurityLog
| where DeviceVendor == "SonicWall"
| where IndicatorThreatType == "Botnet"
| where Activity == "Connection Closed"
| project TimeGenerated, LogSeverity, ThreatSeverity, ThreatConfidence, DeviceProduct, DeviceVersion, Activity, AdditionalExtensions, ApplicationProtocol, EventCount, DeviceInboundInterface, ReceivedBytes, SentBytes, Protocol, Computer, MaliciousIP, MaliciousIPCountry, SourceIP, SourcePort, DestinationIP, DestinationPort;
//| distinct MaliciousIP;
// create list of known botnet connections that were opened
let OpenedConnection = CommonSecurityLog
| where DeviceVendor == "SonicWall"
| where IndicatorThreatType == "Botnet"
| where Activity == "Connection Opened"
| project TimeGenerated, LogSeverity, ThreatSeverity, ThreatConfidence, DeviceProduct, DeviceVersion, Activity, AdditionalExtensions, ApplicationProtocol, EventCount, DeviceInboundInterface, ReceivedBytes, SentBytes, Protocol, Computer, MaliciousIP, MaliciousIPCountry, SourceIP, SourcePort, DestinationIP, DestinationPort;
// compare to make sure that the Malicous IP has been dropped
OpenedConnection
| where MaliciousIP !in (ClosedConnection)
```
