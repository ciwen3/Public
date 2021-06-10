# Helpful for creating Sentinel WorkBooks
### Find tables in Sentinel Logs that you can pull data from
```
union withsource=_TableName *
| summarize Count=count() by _TableName

// Pull all table Names showing up in Sentinel
union withsource=_TableName *
| summarize Count=count() by _TableName
| render barchart
```

### Combined Search
```
search in (SecurityEvent,SecurityAlert,A*) "err"
```

### Combine Workspaces
```
union workspace('name1-SOC').OfficeActivity, workspace('name2-SOC').OfficeActivity
```



### Visualization: 
```
areachart
barchart
columnchart
piechart
scatterchart
timechart
```

#### Example:
```
SecurityEvent 
| summarize count() by Account
| render barchart
```

```
alerts??
incidents??
AuditLogs
AzureActivity
BehaviorAnalytics
DeviceEvents
DeviceFileCertificateInfo
DeviceFileEvents
DeviceImageLoadEvents
DeviceInfo
DeviceLogonEvents
DeviceNetworkEvents
DeviceNetworkInfo
DeviceProcessEvents
DeviceRegistryEvents
Heartbeat
McasShadowItReporting
OfficeActivity
Okta_CL
Operation
Perf
SecurityAlert
SecurityEvent
SecurityIncident
SigninLogs
Syslog
Usage
```


### Okta: 
```
// Okta logins by Region
Okta_CL
| where isnotempty(client_geographicalContext_state_s)
| summarize Count=count() by client_geographicalContext_state_s
| render barchart
```


### Syslog:
```
// Log Collector Syslog 
Syslog
| where Computer contains "LC"
| extend Collector = Computer
| extend LogType = Facility
| project EventTime, Collector, SeverityLevel, LogType, ProcessName, SyslogMessage
| order by EventTime desc 


// Log Collector Syslog SeverityLevel
Syslog
| where Computer contains "LC"
| extend Collector = Computer
| extend LogType = Facility
| project EventTime, Collector, SeverityLevel, LogType, ProcessName, SyslogMessage
| summarize Count=count() by SeverityLevel
| render piechart 


// Log Collector Syslog High SeverityLevel
Syslog
| where Computer contains "LC"
| where SeverityLevel == "emerg" or SeverityLevel == "alert" or SeverityLevel == "crit" or SeverityLevel == "err"
| extend Collector = Computer
| extend LogType = Facility
| project EventTime, Collector, SeverityLevel, LogType, ProcessName, SyslogMessage
| summarize Count=count() by SeverityLevel
| render piechart 


// Log Collector Syslog LogType
Syslog
| where Computer contains "LC"
| extend Collector = Computer
| extend LogType = Facility
| project EventTime, Collector, SeverityLevel, LogType, ProcessName, SyslogMessage
| order by EventTime desc 
| summarize Count=count() by LogType
| render piechart 


// Log Collector Syslog ProcessName
Syslog
| where Computer contains "LC"
| extend Collector = Computer
| extend LogType = Facility
| project EventTime, Collector, SeverityLevel, LogType, ProcessName, SyslogMessage
| order by EventTime desc 
| summarize Count=count() by ProcessName
| render piechart 


// Log Collector Syslog High Severity
Syslog
| where Computer contains "LC"
| where SeverityLevel == "emerg" or SeverityLevel == "alert" or SeverityLevel == "crit" or SeverityLevel == "err"
| extend Collector = Computer
| extend LogType = Facility
| project EventTime, Collector, SeverityLevel, LogType, ProcessName, SyslogMessage
| order by EventTime desc 
```


### Sentinel:
```
// Sentinel Incident Title piechart
SecurityIncident
| summarize arg_max(LastModifiedTime, *) by IncidentNumber
| summarize count() by Title
| render piechart 


// Sentinel Incident Severity piechart
SecurityIncident
| summarize arg_max(LastModifiedTime, *) by IncidentNumber
| where Classification != ""
| summarize count() by Severity
| render piechart 


// Sentinel Incident Status (New/Closed)
SecurityIncident
| summarize arg_max(LastModifiedTime, *) by IncidentNumber
| summarize count() by Status
| render piechart 


// Sentinel Incident Closed Classification piechart
SecurityIncident
| summarize arg_max(LastModifiedTime, *) by IncidentNumber
| where Classification != ""
| summarize count() by Classification
| render piechart 


// Sentinel Time to close Incidents
SecurityIncident
| summarize arg_max(TimeGenerated,*) by IncidentNumber 
| extend TimeToClosure =  (ClosedTime - CreatedTime)/1h
| project TimeToClosure


// Sentinel Security Incidents 
SecurityIncident


// Sentinel Data Usage
Usage
| summarize count() by DataType
```



### VeloCloud:
```
// VeloCloud Syslog for the last hour
let Query1 = view () {
Syslog
| where SyslogMessage contains "SPT" and SyslogMessage contains "APPLICATION"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work = tostring(n.[9])
| extend Application = replace(@'DURATION_SECS', @' ', work)
| extend work2 = tostring(n.[13])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend work3 = tostring(n.[14])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[15])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, Application, DEST, Domain, SyslogMessage
};
let Query2 = view () {
Syslog
| where SyslogMessage !contains "SPT" and SyslogMessage contains "APPLICATION"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work = tostring(n.[7])
| extend Application = replace(@'DURATION_SECS', @' ', work)
| extend work2 = tostring(n.[11])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend DEST = tostring(n.[12])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, DST, VLAN, Application, DEST, SyslogMessage
};
let Query3 = view () {
Syslog
| where SyslogMessage contains "SPT" and SyslogMessage !contains "APPLICATION" and SyslogMessage contains "REASON"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work2 = tostring(n.[9])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend work3 = tostring(n.[10])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[11])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
};
let Query4 = view () {
Syslog
| where SyslogMessage contains "SPT" and SyslogMessage !contains "APPLICATION" and SyslogMessage !contains "REASON"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work3 = tostring(n.[9])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[10])
| project TimeGenerated, Firewall, Protocol, Status, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
};
union withsource="Velocloud" Query1, Query2, Query3, Query4
| order by TimeGenerated desc 



// VeloCloud Network Traffic Domains
let Query1 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage contains "APPLICATION"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work = tostring(n.[9])
| extend Application = replace(@'DURATION_SECS', @' ', work)
| extend work2 = tostring(n.[13])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend work3 = tostring(n.[14])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[15])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, Application, DEST, Domain, SyslogMessage
};
let Query2 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage !contains "SPT" and SyslogMessage contains "APPLICATION"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work = tostring(n.[7])
| extend Application = replace(@'DURATION_SECS', @' ', work)
| extend work2 = tostring(n.[11])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend DEST = tostring(n.[12])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, DST, VLAN, Application, DEST, SyslogMessage
};
let Query3 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage !contains "APPLICATION" and SyslogMessage contains "REASON"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work2 = tostring(n.[9])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend work3 = tostring(n.[10])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[11])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
};
let Query4 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage !contains "APPLICATION" and SyslogMessage !contains "REASON"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work3 = tostring(n.[9])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[10])
| project TimeGenerated, Firewall, Protocol, Status, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
};
//union withsource="Velocloud" Query1, Query2, Query3, Query4
union withsource="Velocloud" Query1, Query2, Query3 , Query4
| where isnotempty(Domain)
| where Domain != "N/A"
| summarize Count=count() by Domain
| render piechart



// VeloCloud Network Traffic Destination
let Query1 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage contains "APPLICATION"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work = tostring(n.[9])
| extend Application = replace(@'DURATION_SECS', @' ', work)
| extend work2 = tostring(n.[13])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend work3 = tostring(n.[14])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[15])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, Application, DEST, Domain, SyslogMessage
};
let Query2 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage !contains "SPT" and SyslogMessage contains "APPLICATION"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work = tostring(n.[7])
| extend Application = replace(@'DURATION_SECS', @' ', work)
| extend work2 = tostring(n.[11])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend DEST = tostring(n.[12])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, DST, VLAN, Application, DEST, SyslogMessage
};
let Query3 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage !contains "APPLICATION" and SyslogMessage contains "REASON"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work2 = tostring(n.[9])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend work3 = tostring(n.[10])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[11])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
};
let Query4 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage !contains "APPLICATION" and SyslogMessage !contains "REASON"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work3 = tostring(n.[9])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[10])
| project TimeGenerated, Firewall, Protocol, Status, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
};
//union withsource="Velocloud" Query1, Query2, Query3, Query4
union withsource="Velocloud" Query4, Query1, Query3, Query2
| summarize Count=count() by DST



// VeloCloud Network Traffic Source
let Query1 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage contains "APPLICATION"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work = tostring(n.[9])
| extend Application = replace(@'DURATION_SECS', @' ', work)
| extend work2 = tostring(n.[13])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend work3 = tostring(n.[14])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[15])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, Application, DEST, Domain, SyslogMessage
};
let Query2 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage !contains "SPT" and SyslogMessage contains "APPLICATION"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work = tostring(n.[7])
| extend Application = replace(@'DURATION_SECS', @' ', work)
| extend work2 = tostring(n.[11])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend DEST = tostring(n.[12])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, DST, VLAN, Application, DEST, SyslogMessage
};
let Query3 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage !contains "APPLICATION" and SyslogMessage contains "REASON"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work2 = tostring(n.[9])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend work3 = tostring(n.[10])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[11])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
};
let Query4 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage !contains "APPLICATION" and SyslogMessage !contains "REASON"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work3 = tostring(n.[9])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[10])
| project TimeGenerated, Firewall, Protocol, Status, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
};
//union withsource="Velocloud" Query1, Query2, Query3, Query4
union withsource="Velocloud" Query4, Query1, Query3, Query2
| summarize Count=count() by SRC



// VeloCloud Firewall Traffic
let Query1 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage contains "APPLICATION"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work = tostring(n.[9])
| extend Application = replace(@'DURATION_SECS', @' ', work)
| extend work2 = tostring(n.[13])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend work3 = tostring(n.[14])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[15])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, Application, DEST, Domain, SyslogMessage
};
let Query2 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage !contains "SPT" and SyslogMessage contains "APPLICATION"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work = tostring(n.[7])
| extend Application = replace(@'DURATION_SECS', @' ', work)
| extend work2 = tostring(n.[11])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend DEST = tostring(n.[12])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, DST, VLAN, Application, DEST, SyslogMessage
};
let Query3 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage !contains "APPLICATION" and SyslogMessage contains "REASON"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work2 = tostring(n.[9])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend work3 = tostring(n.[10])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[11])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
};
let Query4 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage !contains "APPLICATION" and SyslogMessage !contains "REASON"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work3 = tostring(n.[9])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[10])
| project TimeGenerated, Firewall, Protocol, Status, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
};
//union withsource="Velocloud" Query1, Query2, Query3, Query4
union withsource="Velocloud" Query4, Query1, Query3, Query2
| summarize Count=count() by Firewall




// VeloCloud Network Traffic by Protocol
let Query1 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage contains "APPLICATION"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work = tostring(n.[9])
| extend Application = replace(@'DURATION_SECS', @' ', work)
| extend work2 = tostring(n.[13])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend work3 = tostring(n.[14])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[15])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, Application, DEST, Domain, SyslogMessage
};
let Query2 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage !contains "SPT" and SyslogMessage contains "APPLICATION"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work = tostring(n.[7])
| extend Application = replace(@'DURATION_SECS', @' ', work)
| extend work2 = tostring(n.[11])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend DEST = tostring(n.[12])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, DST, VLAN, Application, DEST, SyslogMessage
};
let Query3 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage !contains "APPLICATION" and SyslogMessage contains "REASON"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work2 = tostring(n.[9])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend work3 = tostring(n.[10])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[11])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
};
let Query4 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage !contains "APPLICATION" and SyslogMessage !contains "REASON"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work3 = tostring(n.[9])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[10])
| project TimeGenerated, Firewall, Protocol, Status, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
};
union withsource="Velocloud" Query1, Query2, Query3, Query4
//| where Status == "Open"
//| order by TimeGenerated desc 
| where isnotempty(Protocol)
| summarize Count=count() by Protocol



// VeloCloud Network Traffic Status
let Query1 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage contains "APPLICATION"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work = tostring(n.[9])
| extend Application = replace(@'DURATION_SECS', @' ', work)
| extend work2 = tostring(n.[13])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend work3 = tostring(n.[14])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[15])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, Application, DEST, Domain, SyslogMessage
};
let Query2 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage !contains "SPT" and SyslogMessage contains "APPLICATION"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work = tostring(n.[7])
| extend Application = replace(@'DURATION_SECS', @' ', work)
| extend work2 = tostring(n.[11])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend DEST = tostring(n.[12])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, DST, VLAN, Application, DEST, SyslogMessage
};
let Query3 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage !contains "APPLICATION" and SyslogMessage contains "REASON"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work2 = tostring(n.[9])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend work3 = tostring(n.[10])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[11])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
};
let Query4 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage !contains "APPLICATION" and SyslogMessage !contains "REASON"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work3 = tostring(n.[9])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[10])
| project TimeGenerated, Firewall, Protocol, Status, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
};
union withsource="Velocloud" Query1, Query2, Query3, Query4
//| order by TimeGenerated desc 
| summarize Count=count() by Status



// VeloCloud Network Traffic Close Reason
let Query1 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage contains "APPLICATION"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work = tostring(n.[9])
| extend Application = replace(@'DURATION_SECS', @' ', work)
| extend work2 = tostring(n.[13])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend work3 = tostring(n.[14])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[15])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, Application, DEST, Domain, SyslogMessage
};
let Query2 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage !contains "SPT" and SyslogMessage contains "APPLICATION"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work = tostring(n.[7])
| extend Application = replace(@'DURATION_SECS', @' ', work)
| extend work2 = tostring(n.[11])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend DEST = tostring(n.[12])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, DST, VLAN, Application, DEST, SyslogMessage
};
let Query3 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage !contains "APPLICATION" and SyslogMessage contains "REASON"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work2 = tostring(n.[9])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend work3 = tostring(n.[10])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[11])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
};
let Query4 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage !contains "APPLICATION" and SyslogMessage !contains "REASON"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work3 = tostring(n.[9])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[10])
| project TimeGenerated, Firewall, Protocol, Status, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
};
union withsource="Velocloud" Query1, Query2, Query3, Query4
//| order by TimeGenerated desc 
| where Status == "Close"
| where isnotempty(Reason)
| summarize Count=count() by Reason



// VeloCloud Network Traffic Deny Reason
let Query1 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage contains "APPLICATION"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work = tostring(n.[9])
| extend Application = replace(@'DURATION_SECS', @' ', work)
| extend work2 = tostring(n.[13])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend work3 = tostring(n.[14])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[15])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, Application, DEST, Domain, SyslogMessage
};
let Query2 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage !contains "SPT" and SyslogMessage contains "APPLICATION"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work = tostring(n.[7])
| extend Application = replace(@'DURATION_SECS', @' ', work)
| extend work2 = tostring(n.[11])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend DEST = tostring(n.[12])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, DST, VLAN, Application, DEST, SyslogMessage
};
let Query3 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage !contains "APPLICATION" and SyslogMessage contains "REASON"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work2 = tostring(n.[9])
| extend Reason = replace(@'DEST_NAME', @' ', work2)
| extend work3 = tostring(n.[10])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[11])
| project TimeGenerated, Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
};
let Query4 = view () {
Syslog
| where SyslogMessage contains "VC" and SyslogMessage contains "SPT" and SyslogMessage !contains "APPLICATION" and SyslogMessage !contains "REASON"
| extend Firewall = Computer
| extend p = split(SyslogMessage, " ")
| extend n = split(SyslogMessage, "=")
| extend Status = tostring(p.[1])
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend work3 = tostring(n.[9])
| extend DEST = replace(@'DEST_DOMAIN', @' ', work3)
| extend Domain = tostring(n.[10])
| project TimeGenerated, Firewall, Protocol, Status, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
};
union withsource="Velocloud" Query1, Query2, Query3, Query4
//| order by TimeGenerated desc 
| where Status == "Deny"
| where isnotempty(Reason)
| summarize Count=count() by Reason
```

