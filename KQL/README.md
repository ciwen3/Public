https://learn.microsoft.com/en-us/training/cloud-games

# unpack entitiies
```kql
| extend Entities = iff(isempty(Entities), todynamic('[{"dummy" : ""}]'), todynamic(Entities)) 
| mvexpand Entities
| evaluate bag_unpack(Entities)
```
### example: 
```kql
SecurityAlert
| project-away DisplayName, Type
| extend Entities = iff(isempty(Entities), todynamic('[{"dummy" : ""}]'), todynamic(Entities)) 
| mvexpand Entities
| evaluate bag_unpack(Entities)
```
# remove duplicates
```kql
AzureActivity 
| where OperationName == 'Delete website' and ActivityStatus == 'Succeeded' and ResourceProvider == 'Azure Web Sites' 
| summarize arg_max(TimeGenerated, *) by CorrelationId
```

# use variables
```kql
let f = (a:int){
	case(
	a==1,"January", 
	a==2,"February", 
	a==3,"March",
	a==4,"April",
	a==5,"May",
	a==6,"June"
	a==7,"July"
	a==8,"August"
	a==9,"September"
	a==10,"October"
	a==11,"November"
	a==12,"December"
	)
};
search *
| extend month = f(getmonth(startofmonth(datetime(now),-1)))
| summarize arg_min(TimeGenerated, *) by month
| project month
```

# billable size per table, change timeframes as needed.
```kql
let StartofMonth = startofmonth(datetime(now), -1);
let EndofMonth = endofmonth(datetime(now), -1);
union withsource= table *
| where TimeGenerated between(StartofMonth ..(EndofMonth))
| where _IsBillable == True
| summarize TotalGBytes =todecimal(round(sum(_BilledSize/(1024*1024*1024)),2)) by table, Date = bin(TimeGenerated, 1d)
| render timechart
```
```kql
Event
| summarize count() by Computer, Data = bin(TimeGenerated, 1d)
| render timechart
```

# Online Practice:
requires a free Microsoft email address
1. https://portal.azure.com/#blade/Microsoft_Azure_Monitoring_Logs/DemoLogsBlade
2. https://docs.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference
3. https://docs.microsoft.com/en-us/learn/browse/?products=azure-logic-apps
4. https://docs.microsoft.com/en-us/azure/data-explorer/kql-quick-reference
https://docs.microsoft.com/en-us/azure/data-explorer/kusto/query/make-seriesoperator

# References:
## Sentinel Community Addon:
1. https://github.com/BlueTeamLabs/sentinel-attack

## KQL:
1. https://github.com/reprise99/Sentinel-Queries
2. https://github.com/rod-trent/SentinelKQL
3. https://github.com/reprise99/awesome-kql-sentinel
4. https://github.com/FalconForceTeam/FalconFriday

# Kusto Query Language Examples:
I have either come across these or created these. I try to credit the source when I remember too. 

## searching multiple workspaces: 
```
union workspace('<WorkspaceName1>').SecurityAlert, workspace('<WorkspaceName2>').SecurityAlert
```

# Sentinel Logs:
```
Alert
AppCenterError
AuditLogs 
ComputerGroup
Heartbeat
Operation
SecurityAlert
SecurityEvent
SigninLogs
Syslog
Usage

https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/advanced-hunting-schema-reference?view=o365-worldwide
DeviceFileEvents
DeviceProcessEvents
DeviceEvents
DeviceRegistryEvents
DeviceNetworkEvents
DeviceImageLoadEvents
DeviceLogonEvents

McasShadowItReporting

https://docs.microsoft.com/en-us/azure/sentinel/data-source-schema-reference
https://docs.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-schema
OfficeActivity

Event
EmailEvents
EmailAttachmentInfo
EmailUrlInfo
EmailPostDeliveryEvents
```
### Velocloud Syslog
```
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
| project Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, Application, DEST, Domain, SyslogMessage
```

```
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
| project Firewall, Protocol, Status, Reason, SRC, DST, VLAN, Application, DEST, SyslogMessage
```

```
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
| project Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
```

```
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
| project Firewall, Protocol, Status, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
```

```
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
| project Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, Application, DEST, Domain, SyslogMessage
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
| project Firewall, Protocol, Status, Reason, SRC, DST, VLAN, Application, DEST, SyslogMessage
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
| project Firewall, Protocol, Status, Reason, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
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
| project Firewall, Protocol, Status, SRC, SPRT, DST, DPRT, VLAN, DEST, Domain, SyslogMessage
};
union withsource="Velocloud" Query1, Query2, Query3, Query4
```

### Search for Chrome use
```
DeviceEvents
| where InitiatingProcessCommandLine contains "chrome"
```

### look for connection between two specific devices
```
DeviceNetworkEvents
| where RemoteIP == "8.8.8.8"
| where RemotePort == "443"
| where LocalIP == "127.0.0.1"
| where LocalPort == "54521"
```



### find files that have had a name change by searching for the previous or current hash 
```
DeviceFileEvents
| where InitiatingProcessSHA1 == "<SHA1-HASH>" or SHA1 == "<SHA1-HASH>"
```

### search for changed file based on initial or known file name
```
DeviceFileEvents
| where PreviousFileName contains "<File-Name>"
```

### search for changed file name based on initial or known file hash (sha1)
```
DeviceFileEvents
| where InitiatingProcessSHA1 == "<SHA1-HASH>" or SHA1 == "<SHA1-HASH>"
| where PreviousFileName != ""
| project PreviousFileName, FileName, InitiatingProcessSHA1, SHA1 
```

### On Exchange:
```
//track email attachments in Exchange
OfficeActivity
| where RecordType == "ExchangeItem"
| where Item contains "<File-Name>"
```

### On Sharepoint:
```
//track file in sharepoint
OfficeActivity
| where RecordType contains "SharePoint"
| where OfficeObjectId contains "<File-Name>"
```

### search for changed file based on initial or known file hash (sha256)
```
DeviceFileEvents
| where InitiatingProcessSHA256 == "<SHA256-Hash>" or SHA256 == "<SHA256-Hash>"
```

### search for changed file name based on initial or known file hash (sha256)
```
DeviceFileEvents
| where InitiatingProcessSHA256 == "<SHA256-Hash>" or SHA256 == "<SHA256-Hash>"
| where PreviousFileName != ""
| project PreviousFileName, FileName, InitiatingProcessSHA256, SHA256 
```

### Find devices by uptime
```
Perf
| where ObjectName == "System"
| where CounterName == "System Up Time" or CounterName == "Uptime"
| extend UpTime = CounterValue * 1s
| project TimeGenerated, Computer, UpTime, InstanceName
| summarize arg_max(TimeGenerated, *) by Computer
| order by UpTime desc
```




### search for port scanners
```
//in this case looking for 500 unique IPs or Ports on an IP
//requires WindowsFirewall connector installed 
//https://techcommunity.microsoft.com/t5/azure-sentinel/kql-rule-to-detect-scanning-activty/m-p/1533888
WindowsFirewall
| summarize dcount(DestinationIP), dcount(DestinationPort) by Computer
| where dcount_DestinationIP > 500 or dcount_DestinationPort > 500
```

```
Syslog | where SyslogMessage contains "<IP-Address>"
| extend p = split(SyslogMessage, " ")
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend APP1 = tostring(p.[11])
| extend p6 = split(APP1, "=")
| extend APP = tostring(p6.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend DEST1 = tostring(p.[16])
| extend p8 = split(DEST1, "=")
| extend DEST = tostring(p8.[1])
| extend NAT1 = tostring(p.[17])
| extend p9 = split(NAT1, "=")
| extend NAT = tostring(p9.[1])
| extend NPRT1 = tostring(p.[18])
| extend p10 = split(NPRT1, "=")
| extend NPRT = tostring(p10.[1])
| project Facility, Computer, Protocol, SRC, SPRT, DST, DPRT, APP, VLAN, NAT, NPRT, DEST
```


```
Syslog | where SyslogMessage contains "<Syslog-Msg-Keyword>"
| extend p = split(SyslogMessage, " ")
| extend SRC1 = tostring(p.[6])
| extend p3 = split(SRC1, "=")
| extend SRCIP = tostring(p3.[1])
| extend DSTIP1 = tostring(p.[7])
| extend p2 = split(DSTIP1, "=")
| extend DSTIP = tostring(p2.[1])
| extend DST1 = tostring(p.[16])
| extend p4 = split(DST1, "=")
| extend DPRT = tostring(p4.[1])
| project DPRT, DSTIP, SRCIP
```

```
SecurityAlert
| summarize arg_max(TimeGenerated, *) by SystemAlertId
| where SystemAlertId in("<System-Alert-Id-From-Sentinel>") 
| extend McasAlertID = tostring(parse_json(ExtendedLinks)[1].Href)
| extend Mcas2AlertID = split (McasAlertID, "/", 5)
| extend Mcas2AlertID= tostring(Mcas2AlertID[0])
| extend McasAlertID3 = split (McasAlertID, "/", 2)
| extend McasAlertID3 = tostring(McasAlertID3[0])
| project McasAlertID, Mcas2AlertID, McasAlertID3
```

```
SecurityAlert
| summarize arg_max(TimeGenerated, *) by SystemAlertId
| where SystemAlertId in("<System-Alert-Id-From-Sentinel>")
| project SystemAlertId, Entities 
| extend Entities = iff(isempty(Entities), todynamic('[{"dummy" : ""}]'), todynamic(Entities)) 
| mvexpand Entities
| evaluate bag_unpack(Entities)
| extend Type = columnifexists("Type", "") 
```


### search for exchange takeover https://www.eshlomo.us/hunting-mail-forwarding-with-kusto-on-azure-sentinel/
```
OfficeActivity
| where OfficeWorkload == "Exchange" and Operation == "Set-Mailbox" 
```

### search for exchange takeover https://www.eshlomo.us/hunting-mail-forwarding-with-kusto-on-azure-sentinel/
```
OfficeActivity
| where OfficeWorkload == "Exchange" and Operation == "Set-Mailbox" and Parameters has "DeliverToMailboxAndForward"
| extend Email = tostring(parse_json(Parameters)[1].Value)
| project TimeGenerated, OfficeWorkload, UserId, OfficeObjectId, Email
```

### Find Mouse move installations on this device
```
let fileName = "move mouse.exe";
let fileSha1 = "<Move-Mouse-SHA1-Hash>";
search in (DeviceFileEvents, EmailAttachmentInfo, AppFileEvents)
FileName == fileName
or SHA1 == fileSha1
or InitiatingProcessSHA1 == fileSha1
```


```
SecurityEvent
| summarize count() by EventID, Activity
```
```
SecurityEvent
| summarize count() by EventID
```

### Azure Active Directory Identity Protection:
```
SecurityAlert | where ProductName == "Azure Active Directory Identity Protection" ​| summarize arg_max(TimeGenerated, *) by SystemAlertId
| sort by TimeGenerated
```
```
SecurityAlert | where ProductName == "Azure Active Directory Identity Protection" ​| summarize arg_max(TimeGenerated, *) by SystemAlertId
| summarize count() by AlertSeverity
```


### Azure Active Directory:
```
SigninLogs
| take 1000
| sort by TimeGenerated
```
```
AuditLogs
| summarize count() by bin(TimeGenerated, 1h)
| sort by TimeGenerated
```

### Azure Activity:
```
AzureActivity 
| take 1000
```
```
AzureActivity
| summarize count() by bin(TimeGenerated, 1h)
| sort by TimeGenerated
```

### Microsoft 365 Defender (Preview):
```
DeviceRegistryEvents
| where ActionType == "RegistryValueSet"
| where RegistryValueName == "DefaultPassword"
| where RegistryKey has @"SOFTWAREMicrosoftWindows NTCurrentVersionWinlogon"
| project Timestamp, DeviceName, RegistryKey
| top 100 by Timestamp
```
```
union DeviceProcessEvents, DeviceNetworkEvents
| where Timestamp > ago(7d)
| where FileName in~ ("powershell.exe", "powershell_ise.exe")
| where ProcessCommandLine has_any("WebClient",
"DownloadFile",
"DownloadData",
"DownloadString",
"WebRequest",
"Shellcode",
"http",
"https")
| project Timestamp, DeviceName, InitiatingProcessFileName,
InitiatingProcessCommandLine,
FileName, ProcessCommandLine, RemoteIP, RemoteUrl, RemotePort, RemoteIPType
```
```
DeviceProcessEvents
| where Timestamp > ago(14d)
| where ProcessCommandLine contains ".decode('base64')"
or ProcessCommandLine contains "base64 --decode"
or ProcessCommandLine contains ".decode64("
| project Timestamp , DeviceName , FileName , FolderPath , ProcessCommandLine ,
InitiatingProcessCommandLine
| top 100 by Timestamp
```


### Microsoft Cloud App Security:
```
SecurityAlert​ | where ProductName == "Microsoft Cloud App Security"​ ​| summarize arg_max(TimeGenerated, *) by SystemAlertId
| sort by TimeGenerated
```
```
SecurityAlert​ | where ProductName == "Microsoft Cloud App Security"​ ​| summarize arg_max(TimeGenerated, *) by SystemAlertId
| summarize count() by AlertSeverity
```
```
McasShadowItReporting​
| sort by TimeGenerated
```


### Microsoft Defender for Endpoint:
```
SecurityAlert | where ProviderName == "MDATP"
| sort by TimeGenerated
```

### Microsoft Defender for Identity (Preview):
```
SecurityAlert | where ProductName == "Azure Advanced Threat Protection" ​| summarize arg_max(TimeGenerated, *) by SystemAlertId
| sort by TimeGenerated
```
```
SecurityAlert | where ProductName == "Azure Advanced Threat Protection" ​| summarize arg_max(TimeGenerated, *) by SystemAlertId
| summarize count() by TimeGenerated
| sort by TimeGenerated
```

### Microsoft Defender for Office 365 (Preview):
```
SecurityAlert
| where ProviderName == "OATP"
| sort by TimeGenerated
```

### Office 365: 
```
OfficeActivity
| where OfficeWorkload == "SharePoint" or OfficeWorkload == "OneDrive"
| sort by TimeGenerated
```
```
OfficeActivity
| where OfficeWorkload == "Exchange"
| sort by TimeGenerated
```
```
OfficeActivity
| where OfficeWorkload == "MicrosoftTeams"
| sort by TimeGenerated
```

### Qualys Vulnerability Management (Preview):
```
QualysHostDetection_CL
| mv-expand todynamic(Detections_s)
| extend Vulnerability = tostring(Detections_s.Results)
| summarize count() by Vulnerability
| top 10 by count_
```

### Security Events:
```
SecurityEvent
| sort by TimeGenerated
```

### Syslog:
```
Syslog | where SyslogMessage contains "<Syslog-Msg-Keyword>"
| extend p = split(SyslogMessage, " ")
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend APP1 = tostring(p.[11])
| extend p6 = split(APP1, "=")
| extend APP = tostring(p6.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend DEST1 = tostring(p.[16])
| extend p8 = split(DEST1, "=")
| extend DEST = tostring(p8.[1])
| extend NAT1 = tostring(p.[17])
| extend p9 = split(NAT1, "=")
| extend NAT = tostring(p9.[1])
| extend NPRT1 = tostring(p.[18])
| extend p10 = split(NPRT1, "=")
| extend NPRT = tostring(p10.[1])
| project Facility, Computer, Protocol, SRC, SPRT, DST, DPRT, APP, VLAN, NAT, NPRT, DEST
```


```
Syslog | where SyslogMessage contains "dns"
| extend p = split(SyslogMessage, " ")
| extend Protocol1 = tostring(p.[6])
| extend p1 = split(Protocol1, "=")
| extend Protocol = tostring(p1.[1])
| extend SRC1 = tostring(p.[7])
| extend p2 = split(SRC1, "=")
| extend SRC = tostring(p2.[1])
| extend SPRT1 = tostring(p.[9])
| extend p3 = split(SPRT1, "=")
| extend SPRT = tostring(p3.[1])
| extend DST1 = tostring(p.[8])
| extend p4 = split(DST1, "=")
| extend DST = tostring(p4.[1])
| extend DPRT1 = tostring(p.[10])
| extend p5 = split(DPRT1, "=")
| extend DPRT = tostring(p5.[1])
| extend APP1 = tostring(p.[11])
| extend p6 = split(APP1, "=")
| extend APP = tostring(p6.[1])
| extend VLAN1 = tostring(p.[5])
| extend p7 = split(VLAN1, "=")
| extend VLAN = tostring(p7.[1])
| extend DEST1 = tostring(p.[16])
| extend p8 = split(DEST1, "=")
| extend DEST = tostring(p8.[1])
| extend NAT1 = tostring(p.[17])
| extend p9 = split(NAT1, "=")
| extend NAT = tostring(p9.[1])
| extend NPRT1 = tostring(p.[18])
| extend p10 = split(NPRT1, "=")
| extend NPRT = tostring(p10.[1])
| project Facility, Computer, Protocol, SRC, SPRT, DST, DPRT, APP, VLAN, NAT, NPRT, DEST)
```

```
Syslog | where SyslogMessage contains "aws"
| extend p = split(SyslogMessage, " ") 
| extend Protocol = tostring(p.[6])
| extend SRC = tostring(p.[7])
| extend SPRT = tostring(p.[9])
| extend DST = tostring(p.[8])
| extend DPRT = tostring(p.[10])
| extend APP = tostring(p.[11])
| extend VLAN = tostring(p.[5])
| extend DEST = tostring(p.[16])
| extend NAT = tostring(p.[17])
| extend NPRT = tostring(p.[18])
| project Facility, Computer, Protocol, SRC, SPRT, DST, DPRT, APP, VLAN, NAT, NPRT, DEST
```

```
Syslog
| where TimeGenerated >= ago(timeframe)
| where Facility in ("auth","authpriv")
| where SyslogMessage has_any (pWord) and SyslogMessage has_any (action)
| extend AccountType = iif(SyslogMessage contains "root", "Root", "Non-Root")
| parse SyslogMessage with * "password changed for" Account
| project TimeGenerated, AccountType, Account, Computer = HostName, Type)
```


```
SecurityAlert 
| where DisplayName == "Unfamiliar sign-in properties"
| extend p = split(ExtendedProperties, ",") 
| extend IP = tostring(p.[2])
| project IP
```
```
SecurityAlert 
| where DisplayName == "Unfamiliar sign-in properties"
| extend p = split(ExtendedProperties, ",") 
| extend IPS = tostring(p.[2])
| extend p2 = split(IPS, "\"") 
| extend IP = tostring(p2.[3])
| project IP
```
```
SecurityAlert | where CompromisedEntity contains "<username>"
```

### return any Azure Activity events that recorded a deleted resource
```
AzureActivity
  | where OperationName has 'delete'
  | where ActivityStatus == 'Accepted'
  | extend AccountCustomEntity = Caller
  | extend IPCustomEntity = CallerIpAddress
```

### return Azure Activity events that recorded a deleted VM
```
AzureActivity
  | where OperationName == 'Delete Virtual Machine'
  | where ActivityStatus == 'Accepted'
  | extend AccountCustomEntity = Caller
  | extend IPCustomEntity = CallerIpAddress
```

```
SecurityAlert
| where DisplayName == "Unfamiliar sign-in properties"
// testing
| extend Country = parse_json(Entities)[1]['Location']
//| extend CountryCode = parse_json(Country)[1]
| extend p = split(Country, "\"") 
| extend CountryCode = tostring(p.[3])
| project Country, CountryCode
```
```
SecurityAlert | summarize arg_max(TimeGenerated, *) by SystemAlertId | where SystemAlertId in("<System-Alert-Id-From-Sentinel>") 
| extend Name = parse_json(Entities)[0]['Upn']
| project Name
```
```
SecurityAlert | where SystemAlertId in("<System-Alert-Id-From-Sentinel>")
| extend Name = parse_json(Entities)[1]['HostName']
| project Name
```

### Get country code:
```
SecurityAlert | where SystemAlertId in("<System-Alert-Id-From-Sentinel>")
| extend CountryName = parse_json(Entities)[1]['Location']['CountryCode']
| project CountryName
```

### list ips that have the shown up in signinlogs
```
let TimeFrame = ago(30d); 
SigninLogs 
| where TimeGenerated > TimeFrame
| summarize FirstSeen = min(TimeGenerated), LastObserved = max(TimeGenerated), SuccessfullCount = count(ResultType = 0), FailureCount = count(ResultType != 0) 
by IPAddress
```


### Search logs for anyone else with this file name
```
let GetFilesHost = (v_File_Name: string) {
    SecurityEvent
    | where CommandLine contains v_File_Name or ServiceFileName contains v_File_Name or ServiceName contains v_File_Name
    | summarize min(TimeGenerated), max(TimeGenerated) by Computer
    | project min_TimeGenerated, max_TimeGenerated, Computer
    | project-rename Host_UnstructuredName=Computer, Host_Aux_min_TimeGenerated=min_TimeGenerated, Host_Aux_max_TimeGenerated=max_TimeGenerated
    | top 10 by Host_Aux_min_TimeGenerated desc nulls last
};
GetFilesHost(@'f_00ef65')
```

### search for any other files with the same sha1 hash value
```
let GetFileHashRelatedAlerts = (v_FileHash_Value: string) {
    SecurityAlert
    | summarize arg_max(TimeGenerated, *) by SystemAlertId
    | extend entities = todynamic(Entities) 
    | mv-expand entities
    | project-rename entity=entities
    | where entity['Type'] == 'filehash' and entity['Value'] =~ v_FileHash_Value
    | project-away entity
};
GetFileHashRelatedAlerts(@'6ae9edb440971148800b5180ca1df86a9550e130')
```

### process that the incident took before it was stopped 
```
let GetActiveProcessesOnHost = (v_Host_HostName: string) {
    SecurityEvent 
    | where EventID == 4688
    | where NewProcessName !contains ':\\Windows\\System32\\conhost.exe' and ParentProcessName !contains ':\\Windows\\System32\\conhost.exe'
        and NewProcessName !contains ':\\Windows\\Microsoft.NET\\Framework64\\v2.0.50727\\csc.exe' and ParentProcessName !contains ':\\Windows\\Microsoft.NET\\Framework64\\v2.0.50727\\csc.exe'
        and NewProcessName !contains ':\\Windows\\Microsoft.NET\\Framework64\\v2.0.50727\\cvtres.exe' and ParentProcessName !contains ':\\Windows\\Microsoft.NET\\Framework64\\v2.0.50727\\cvtres.exe'
        and NewProcessName !contains ':\\Program Files\\Microsoft Monitoring Agent\\Agent\\MonitoringHost.exe' and ParentProcessName !contains ':\\Program Files\\Microsoft Monitoring Agent\\Agent\\MonitoringHost.exe'
        and ParentProcessName !contains ':\\Windows\\CCM\\CcmExec.exe'
    | where (ParentProcessName !contains ':\\Windows\\System32\\svchost.exe' and (NewProcessName !contains ':\\Windows\\System32\\wbem\\WmiPrvSE.exe' or NewProcessName !contains ':\\Windows\\SysWOW64\\wbem\\WmiPrvSE.exe'))
    | where (ParentProcessName !contains ':\\Windows\\System32\\services.exe' and NewProcessName !contains ':\\Windows\\servicing\\TrustedInstaller.exe')
    | where toupper(Computer) contains v_Host_HostName or toupper(WorkstationName) contains v_Host_HostName
    | summarize Process_Aux_StartTime=min(TimeGenerated), Process_Aux_EndTime=max(TimeGenerated) by Computer, Account, NewProcessName, CommandLine, ProcessId, ParentProcessName
    | project Process_Aux_StartTime, Process_Aux_EndTime, Computer, Account, NewProcessName, CommandLine, ProcessId, Process_ParentProcess_ImageFile_FullPath=ParentProcessName
    | project-rename Process_Host_UnstructuredName=Computer, Process_Account_UnstructuredName=Account, Process_CommandLine=CommandLine, Process_ProcessId=ProcessId, Process_ImageFile_FullPath=NewProcessName
    | top 10 by Process_Aux_StartTime desc
};
GetActiveProcessesOnHost(@'desktop-bnl7h78')
```

### Checked for the most prevalent account on that IP address
```
let GetMostPrevUsersbyIP = (v_IP_Address: string) {
    SigninLogs
    | where IPAddress contains v_IP_Address
    | extend RemoteHost = tolower(tostring(parsejson(DeviceDetail['displayName'])))
    | extend OS = DeviceDetail.operatingSystem, Browser = DeviceDetail.browser
    | extend StatusCode = tostring(Status.errorCode), StatusDetails = tostring(Status.additionalDetails)
    | extend State = tostring(LocationDetails.state), City = tostring(LocationDetails.city)
    | extend info = pack('AppDisplayName', AppDisplayName, 'ClientAppUsed', ClientAppUsed, 'Browser', tostring(Browser), 'IPAddress', IPAddress, 'ResultType', ResultType, 'ResultDescription', ResultDescription, 'Location', Location, 'State', State, 'City', City, 'StatusCode', StatusCode, 'StatusDetails', StatusDetails)
    | summarize min(TimeGenerated), max(TimeGenerated), count(), Account_Aux_info = makeset(info) by RemoteHost, UserDisplayName, tostring(OS), UserPrincipalName, AADTenantId, UserId
    | top 10 by count_ desc nulls last 
    | project Account_Aux_StartTimeUtc = min_TimeGenerated, Account_Aux_EndTimeUtc = max_TimeGenerated, RemoteHost, UserDisplayName, OS, UserPrincipalName, AADTenantId, UserId, Account_Aux_info
    | project-rename Account_UnstructuredName=UserPrincipalName, Account_DisplayName=UserDisplayName, Account_AadTenantId=AADTenantId, Account_AadUserId=UserId, Account_Host_UnstructuredName=RemoteHost, Account_Host_OSVersion=OS
};
GetMostPrevUsersbyIP(@'45.62.182.59')
```




### show all successful logins in the Azure portal
```
SigninLogs
| where AppDisplayName == "Azure Portal"
    and ResultType == 0
```

### show all newly created users
```
AuditLogs
| where OperationName == "Add user"
// show all PIM requests
AuditLogs
| where OperationName == "Add member to role requested (PIM activation)"
     or OperationName == "Remove member from role completed (PIM deactivate)"
| extend Account = tostring(InitiatedBy.["user"].["userPrincipalName"])
| distinct TimeGenerated, Account, ResultDescription
```


### show all password resets on linux VMs
```
AzureActivity
| where Resource contains "VMAccessLinuxPasswordReset"
    and ActivityStatus == "Succeeded"
// Show all new Azure Role assignments
AzureActivity
| where ResourceProvider == "Microsoft.Authorization'
    and OperationNameValue == "Microsoft.Authorization/roleAssignments/write"
    and ActivityStatus == "Succeeded"
```


### Get all Exchange related events
```
OfficeActivity
| where OfficeWorkload == "Exchange"
```

### Get all SharePoint and OneDrive related events
```
OfficeActivity
| where OfficeWorkload == "SharePoint"
```

### Get all OneDrive related Events
```
OfficeActivity
| where OfficeWorkload == "SharePoint" or OfficeWorkload == "OneDrive"
| sort by TimeGenerated
```

### get all login events that are not produced by NT Authority\System
```
SecurityEvent
| where EventID == "4624"
    and Account <> "NT AUTHORITY\\SYSTEM"
```

### Get all logs from the cron deamon in linux
```
Syslog
| where ProcessName == "CRON"
```


### Get all alerts reported by Microsoft Cloud App Security
```
SecurityAlert
| where ProviderName == "MCAS"
```

### Get all alerts reported by Sentinel
```
SecurityAlert
| where ProviderName == "Azure Sentinel"
```


### Get all SQL successfull authentications
```
AzureDiagnostics
| where clientIP_s != ""
| where ResourceProvider == "MICROSOFT.SQL"
and action_name_s == "DATABASE AUTHENTICATION SUCCEEDED"
```


### Show a limited set of data that is in the threat intelligence table
```
ThreatIntelligenceIndicator
| limit 50
```





### list ips that have the shown up in signinlogs
```
let TimeFrame = ago(30d); 
SigninLogs 
| where TimeGenerated > TimeFrame
| summarize by IPAddress
```

```
let TimeFrame = ago(30d); 
SigninLogs 
| where TimeGenerated > TimeFrame
| where ResultType != "0"
```
```
let TimeFrame = ago(30d); 
SigninLogs 
| where TimeGenerated > TimeFrame
| where ResultType != "0"
| summarize by ResultDescription
```


### list ips that have the sown up in signinlogs
```
let TimeFrame = ago(30d); 
SigninLogs 
| where TimeGenerated > TimeFrame
| where 
| summarize FailureCount = count(ResultType != 0) 
by IPAddress
```
```
let TimeFrame = ago(30d); 
SigninLogs 
| where TimeGenerated > TimeFrame
| where ResultType != "0"
| summarize by ResultDescription, ResultType
```
```
let TimeFrame = ago(30d); 
SigninLogs 
| where TimeGenerated > TimeFrame
| where ResultType != "0"
| summarize IPcount = count(IPAddress)
by ResultDescription, ResultType, IPAddress
```



### The query_now parameter represents the time (in UTC) at which the scheduled analytics rule ran to produce this alert.
```
set query_now = datetime(<Current-Date&Time>);
let timeframe = 1d;
let PerUserThreshold = 5;
let TotalThreshold = 100;
let action = dynamic(["change", "changed", "reset"]);
let pWord = dynamic(["password", "credentials"]);
let PasswordResetMultiDataSource =
(union isfuzzy=true
(//Password reset events
//4723: An attempt was made to change an account's password
//4724: An attempt was made to reset an accounts password
SecurityEvent
| where TimeGenerated >= ago(timeframe)
| where EventID in ("4723","4724")
| project TimeGenerated, Computer, AccountType, Account, Type),
(//Azure Active Directory Password reset events
AuditLogs
| where TimeGenerated >= ago(timeframe)
| where OperationName has_any (pWord) and OperationName has_any (action)
| extend AccountType = tostring(TargetResources[0].type), Account = tostring(TargetResources[0].userPrincipalName), 
TargetResourceName = tolower(tostring(TargetResources[0].displayName))
| project TimeGenerated, AccountType, Account, Computer = TargetResourceName, Type),
(//OfficeActive ActiveDirectory Password reset events
OfficeActivity
| where TimeGenerated >= ago(timeframe)
| where OfficeWorkload == "AzureActiveDirectory" 
| where (ExtendedProperties has_any (pWord) or ModifiedProperties has_any (pWord)) and (ExtendedProperties has_any (action) or ModifiedProperties has_any (action))
| extend AccountType = UserType, Account = OfficeObjectId 
| project TimeGenerated, AccountType, Account, Type, Computer = ""),
(// Unix syslog password reset events
Syslog
| where TimeGenerated >= ago(timeframe)
| where Facility in ("auth","authpriv")
| where SyslogMessage has_any (pWord) and SyslogMessage has_any (action)
| extend AccountType = iif(SyslogMessage contains "root", "Root", "Non-Root")
| parse SyslogMessage with * "password changed for" Account
| project TimeGenerated, AccountType, Account, Computer = HostName, Type),
(SigninLogs
| where TimeGenerated >= ago(timeframe)
| where OperationName =~ "Sign-in activity" and ResultType has_any ("50125", "50133")
| project TimeGenerated, AccountType = AppDisplayName, Computer = IPAddress, Account = UserPrincipalName, Type
)
);
let pwrmd = PasswordResetMultiDataSource
| project TimeGenerated, Computer, AccountType, Account, Type;
(union isfuzzy=true  
(pwrmd
| summarize StartTimeUtc = min(TimeGenerated), EndTimeUtc = max(TimeGenerated), Computer = makeset(Computer), AccountType = makeset(AccountType), Total=count() by Account, Type
| where Total > PerUserThreshold
| extend ResetPivot = "PerUserReset"),  
(pwrmd
| summarize StartTimeUtc = min(TimeGenerated), EndTimeUtc = max(TimeGenerated), Computer = makeset(Computer), Account = tostring(makeset(Account)), AccountType = makeset(AccountType), Total=count() by Type
| where Total > TotalThreshold
| extend ResetPivot = "TotalUserReset")
)
| extend timestamp = StartTimeUtc, AccountCustomEntity = Account, HostCustomEntity = tostring(Computer)
```



### Search for the existence of cryptominers
```
Syslog
  | parse SyslogMessage with "type=" EventType " audit(" * "): " EventData
  | project TimeGenerated, EventType, Computer, EventData 
  // Extract AUOMS_EXECVE details from EventData
  | where EventType =~ "AUOMS_EXECVE"
  | parse EventData with * "syscall=" syscall " syscall_r=" * " success=" success " exit=" exit " a0" * " ppid=" ppid " pid=" pid " audit_user=" audit_user " auid=" auid " user=" user " uid=" uid " group=" group " gid=" gid "effective_user=" effective_user " euid=" euid " set_user=" set_user " suid=" suid " filesystem_user=" filesystem_user " fsuid=" fsuid " effective_group=" effective_group " egid=" egid " set_group=" set_group " sgid=" sgid " filesystem_group=" filesystem_group " fsgid=" fsgid " tty=" tty " ses=" ses " comm=\"" comm "\" exe=\"" exe "\"" * "cwd=\"" cwd "\"" * "name=\"" name "\"" * "cmdline=\"" cmdline "\" containerid=" containerid
  // Find wget and curl commands
  | where comm in ("wget", "curl")
  // Find command lines featuring known crypto currency miner names
  | where cmdline contains "nicehashminer" or cmdline contains "ethminer" or cmdline contains "equihash" or cmdline contains "NsCpuCNMiner64" or cmdline contains "minergate" or cmdline contains "minerd" or cmdline contains "cpuminer" or cmdline contains "xmr-stak-cpu" or cmdline contains "xmrig" or cmdline contains "stratum+tcp" or cmdline contains "cryptonight" or cmdline contains "monero" or cmdline contains "oceanhole" or cmdline contains "dockerminer" or cmdline contains "xmrdemo"
  | project TimeGenerated, Computer, audit_user, user, cmdline
  | extend AccountCustomEntity = user, HostCustomEntity = Computer, timestamp = TimeGenerated
  | sort by TimeGenerated desc
```


### Search for socket connections
```
Syslog
| where SyslogMessage contains "sock"
```

```
Heartbeat | where OSType == 'Linux' | summarize arg_max(TimeGenerated, *) by SourceComputerId | sort by Computer | render table
```
```
Heartbeat | where OSType == 'Linux' 
```
```
Operation | where Computer contains "SyslogRelay"
```
```
Alert | where Computer contains "Linux"
```
```
Syslog | where HostName contains "LinuxSyslogRelay" | sort by TimeGenerated desc
```

### Search for files with this <sha1-hash-value>
```
let GetFileHashRelatedAlerts = (v_FileHash_Value: string) {
    SecurityAlert
    | summarize arg_max(TimeGenerated, *) by SystemAlertId
    | extend entities = todynamic(Entities) 
    | mv-expand entities
    | project-rename entity=entities
    | where entity['Type'] == 'filehash' and entity['Value'] =~ v_FileHash_Value
    | project-away entity
};
GetFileHashRelatedAlerts(@'<sha1-hash-value>')
```


### Search logs for anyone else with this <file-name>
```
  let GetFilesHost = (v_File_Name: string) {
    SecurityEvent
    | where CommandLine contains v_File_Name or ServiceFileName contains v_File_Name or ServiceName contains v_File_Name
    | summarize min(TimeGenerated), max(TimeGenerated) by Computer
    | project min_TimeGenerated, max_TimeGenerated, Computer
    | project-rename Host_UnstructuredName=Computer, Host_Aux_min_TimeGenerated=min_TimeGenerated, Host_Aux_max_TimeGenerated=max_TimeGenerated
    | top 10 by Host_Aux_min_TimeGenerated desc nulls last
};
GetFilesHost(@'<file-name>')
```

```
SecurityAlert
| summarize arg_max(TimeGenerated, *) by SystemAlertId
| where DisplayName contains "Suspected DCSync attack"
| project StartTime
```
```
let timeRange = 1d;
let lookBack = 7d;
let threshold_Failed = 5;
let threshold_FailedwithSingleIP = 20;
let threshold_IPAddressCount = 2;
let azPortalSignins = SigninLogs
let isGUID = "[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}";
| extend Unresolved = iff(Identity matches regex isGUID, true, false);
let identityLookup = SigninLogs
| where TimeGenerated >= ago(lookBack)
| where not(Identity matches regex isGUID)
| summarize by UserId, lu_UserDisplayName = UserDisplayName, lu_UserPrincipalName = UserPrincipalName;
// Join resolved names to unresolved list from portal signins
let unresolvedNames = azPortalSignins | where Unresolved == true | join kind= inner ( identityLookup ) on UserId
| extend UserDisplayName = lu_UserDisplayName, UserPrincipalName = lu_UserPrincipalName
| project-away lu_UserDisplayName, lu_UserPrincipalName;
let u_azPortalSignins = azPortalSignins | where Unresolved == false | union unresolvedNames;
let failed_signins = (u_azPortalSignins
| extend Status = strcat(ResultType, ": ", ResultDescription), OS = tostring(DeviceDetail.operatingSystem), Browser = tostring(DeviceDetail.browser)
| extend FullLocation = strcat(Location,'|', LocationDetails.state, '|', LocationDetails.city)
| summarize TimeGenerated = makelist(TimeGenerated), Status = makelist(Status), IPAddresses = makelist(IPAddress), IPAddressCount = dcount(IPAddress), FailedLogonCount = count()
by UserPrincipalName, UserId, UserDisplayName, AppDisplayName, Browser, OS, FullLocation
| mvexpand TimeGenerated, IPAddresses, Status
| extend TimeGenerated = todatetime(tostring(TimeGenerated)), IPAddress = tostring(IPAddresses), Status = tostring(Status)
| project-away IPAddresses
| summarize StartTime = min(TimeGenerated), EndTime = max(TimeGenerated) by UserPrincipalName, UserId, UserDisplayName, Status, FailedLogonCount, IPAddress, IPAddressCount, AppDisplayName, Browser, OS, FullLocation
| where (IPAddressCount >= threshold_IPAddressCount and FailedLogonCount >= threshold_Failed) or FailedLogonCount >= threshold_FailedwithSingleIP
| project UserPrincipalName);
```


### Login Failures from: https://techcommunity.microsoft.com/t5/azure-sentinel/sentinel-query-question-w-r-t-to-login-failures/m-p/1130830
```
let timeframe = 1d;
SecurityEvent
| where TimeGenerated >= ago(timeframe)
| where AccountType == 'User' and EventID == 4625
| extend Reason = case(
SubStatus == '0xc000005e', 'No logon servers available to service the logon request',
SubStatus == '0xc0000062', 'Account name is not properly formatted',
SubStatus == '0xc0000064', 'Account name does not exist',
SubStatus == '0xc000006a', 'Incorrect password',    SubStatus == '0xc000006d', 'Bad user name or password',
SubStatus == '0xc000006f', 'User logon blocked by account restriction',
SubStatus == '0xc000006f', 'User logon outside of restricted logon hours',
SubStatus == '0xc0000070', 'User logon blocked by workstation restriction',
SubStatus == '0xc0000071', 'Password has expired',
SubStatus == '0xc0000072', 'Account is disabled',
SubStatus == '0xc0000133', 'Clocks between DC and other computer too far out of sync',
SubStatus == '0xc000015b', 'The user has not been granted the requested logon right at this machine',
SubStatus == '0xc0000193', 'Account has expirated',
SubStatus == '0xc0000224', 'User is required to change password at next logon',
SubStatus == '0xc0000234', 'Account is currently locked out',
strcat('Unknown reason substatus: ', SubStatus))
| summarize StartTimeUtc = min(TimeGenerated), EndTimeUtc = max(TimeGenerated), count() by Reason
| extend timestamp = StartTimeUtc
```

### Windows failed logins 
```
// Find reports of Windows accounts that failed to login. 
// To create an alert for this query, click '+ New alert rule'
SecurityEvent
| where EventID == 4625
| summarize count() by TargetAccount, Computer, _ResourceId // count the reported security events for each account
// This query requires the Security solution
```
```
SigninLogs
| where TimeGenerated > ago(7d)
| where ResultType != 0
| where name shows up 3 times or morewithin 1  hour 
| summarize by UserId, lu_UserDisplayName = UserDisplayName, lu_UserPrincipalName = UserPrincipalName;
```


### Signinlogs from: https://github.com/Azure/Azure-Sentinel/blob/master/Hunting%20Queries/SigninLogs/AnomalousUserAppSigninLocationIncreaseDetail.yaml
```
let timeRange = ago(14d);
SigninLogs 
// Forces Log Analytics to recognize that the query should be run over full time range
| where TimeGenerated >= timeRange
| extend locationString= strcat(tostring(LocationDetails["countryOrRegion"]), "/", 
    tostring(LocationDetails["state"]), "/", tostring(LocationDetails["city"]), ";") 
| project TimeGenerated, AppDisplayName, UserPrincipalName, locationString 
// Create time series 
| make-series dLocationCount = dcount(locationString)
    on TimeGenerated
    in range(timeRange, now(), 1d) 
    by UserPrincipalName, AppDisplayName 
// Compute best fit line for each entry 
| extend (RSquare, Slope, Variance, RVariance, Interception, LineFit)=series_fit_line(dLocationCount) 
// Chart the 3 most interesting lines  
// A 0-value slope corresponds to an account being completely stable over time for a given Azure Active Directory application
| top 3 by Slope desc  
// Extract the set of locations for each top user:
| join kind=inner (
    SigninLogs
    | where TimeGenerated >= timeRange
    | extend locationString= strcat(tostring(LocationDetails["countryOrRegion"]), "/", 
        tostring(LocationDetails["state"]), "/", tostring(LocationDetails["city"]), ";")
    | summarize locationList = makeset(locationString), threeDayWindowLocationCount=dcount(locationString)
        by AppDisplayName, UserPrincipalName, 
        timerange=bin(TimeGenerated, 3d))
    on AppDisplayName, UserPrincipalName
| order by UserPrincipalName, timerange asc
| project timerange, AppDisplayName, UserPrincipalName, threeDayWindowLocationCount, locationList 
| order by AppDisplayName, UserPrincipalName, timerange asc
| extend timestamp = timerange, AccountCustomEntity = UserPrincipalName
 ```



```
Syslog | where Computer contains "<Computer-Name>"
| where SyslogMessage contains "<Syslog-Msg-Keyword>" 
| extend p = split(SyslogMessage, ":") 
| extend MSG = tostring(p.[2])
| extend p2 = split(MSG, " ") 
| extend ip = tostring(p2.[1])
| extend pip = split(ip, "->")
| extend pip0 = tostring(pip.[0])
| extend pip1 = tostring(pip.[1])
| extend psrc = split(pip0, "/")
| extend sourceaddress = tostring(psrc.[0])
| extend sourceport = tostring(psrc.[1])
| extend pdst = split(pip1, "/")
| extend destinationaddress = tostring(pdst.[0])
| extend destinationport = tostring(pdst.[1])
| extend connectiontag = tostring(p2.[2])
| extend servicename = tostring(p2.[3])
| extend ip2 = tostring(p2.[4])
| extend pip2 = split(ip, "->")
| extend pip02 = tostring(pip.[0])
| extend pip12 = tostring(pip.[1])
| extend psrc2 = split(pip02, "/")
| extend natsourceaddress = tostring(psrc2.[0])
| extend natsourceport = tostring(psrc2.[1])
| extend pdst2 = split(pip12, "/")
| extend natdestinationaddress = tostring(pdst2.[0])
| extend natdestinationport = tostring(pdst2.[1])
| extend natconnectiontag = tostring(p2.[5])
| extend srcnatruletype =  tostring(p2.[6])
| extend srcnatrulename = tostring(p2.[7])
| extend dstnatruletype = tostring(p2.[8])
| extend dstnatrulename = tostring(p2.[9])
| extend protocolid = tostring(p2.[10])
| extend policyname = tostring(p2.[11])
| extend sourcezonename = tostring(p2.[12])
| extend destinationzonename = tostring(p2.[13])
| extend sessionid32 = tostring(p2.[14])
| extend packet = tostring(p2.[15])
| extend ppack = split(ip, "(")
| extend packetsfromclient = tostring(ppack.[0])
| extend bytesfromclient = tostring(ppack.[1]) 
| extend packet2 = tostring(p2.[16])
| extend ppack2 = split(ip, "(")
| extend packetsfromserver = tostring(ppack2.[0])
| extend bytesfromserver = tostring(ppack2.[1])
| extend elapsedtime = tostring(p2.[17])
| extend application = tostring(p2.[18])
| extend nestedapplication = tostring(p2.[19])
| extend user = tostring(p2.[20])
| extend puser = split(ip, "(")
| extend username = tostring(puser.[0])
| extend roles = tostring(puser.[1])
| extend packetincominginterface = tostring(p2.[21])
| extend encrypted = tostring(p2.[22])
| extend applicationcategory = tostring(p2.[23])
| extend applicationsubcategory = tostring(p2.[24])
| extend applicationrisk = tostring(p2.[25])
| extend applicationcharacteristics = tostring(p2.[26])
```

### MS Defender:
```
// Find all Netlogon exploit attempt alerts containing source devices 
let queryWindow = 3d;
AlertInfo
| where Timestamp > ago(queryWindow)
| where ServiceSource == "Azure ATP"
| where Title == "Suspected Netlogon privilege elevation attempt (CVE-2020-1472 exploitation)"
| join (AlertEvidence
    | where Timestamp > ago(queryWindow)
    | where EntityType == "Machine"
    | where EvidenceDirection == "Source"
    | where isnotempty(DeviceId)
) on AlertId
| summarize by AlertId, DeviceId, Timestamp
```

```
// https://github.com/microsoft/Microsoft-365-Defender-Hunting-Queries/blob/master/General%20queries/Machine%20info%20from%20IP%20address.txt
// Query #4: Get machines that have used a given IP address, looking up on both local and external addresses.
//           This includes IP addresses seen locally in their network adapters configuration or ones used to access the WDATP cloud.
//let pivotTimeParam = datetime(12/23/20 09:08:00);
let ipAddressParam = "10.100.101.14";
DeviceNetworkInfo
| where IPAddresses contains strcat("\"", ipAddressParam, "\"") and NetworkAdapterStatus == "Up"
//| project DeviceName, Timestamp, Source="NetworkAdapterInfo" 
//| union (DeviceInfo | where PublicIP == ipAddressParam | project DeviceName, Timestamp, Source="Public IP address")
| sort by DeviceName
```
```
// Get machines that have used a given IP address, looking up on both local and external addresses.
// This includes IP addresses seen locally in their network adapters configuration or ones used to access the WDATP cloud.
let ipAddressParam = "10.100.101.14";
DeviceNetworkInfo
| where IPAddresses contains strcat("\"", ipAddressParam, "\"") and NetworkAdapterStatus == "Up"
| sort by DeviceName
```


### Advanced threat hunting: https://github.com/microsoft/Microsoft-365-Defender-Hunting-Queries
### https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/advanced-hunting-query-language

```
// Finds PowerShell execution events that could involve a download
union DeviceProcessEvents, DeviceNetworkEvents
| where Timestamp > ago(7d)
// Pivoting on PowerShell processes
| where FileName in~ ("powershell.exe", "powershell_ise.exe")
// Suspicious commands
| where ProcessCommandLine has_any("WebClient",
    "DownloadFile",
    "DownloadData",
    "DownloadString",
    "WebRequest",
    "Shellcode",
    "http",
    "https")
| project Timestamp, DeviceName, InitiatingProcessFileName, InitiatingProcessCommandLine, 
FileName, ProcessCommandLine, RemoteIP, RemoteUrl, RemotePort, RemoteIPType
| top 100 by Timestamp
```




### Find use of WMIC 
```
// This can be changed to any exe program
DeviceProcessEvents
| where Timestamp > ago(7d)
| where FileName =~ "wmic.exe"
| project DeviceId, Timestamp, InitiatingProcessFileName, FileName,
ProcessCommandLine, InitiatingProcessIntegrityLevel, InitiatingProcessParentFileName
```

### Find use of WMIC 
```
// This can be changed to any exe program
// limit the output to just one device by DeviceName
DeviceProcessEvents
| where Timestamp > ago(7d)
| where DeviceName contains "<DeviceName>"
| where FileName =~ "wmic.exe"
| project DeviceId, Timestamp, InitiatingProcessFileName, FileName,
ProcessCommandLine, InitiatingProcessIntegrityLevel, InitiatingProcessParentFileName
```



### Find use of CMD
```
// This can be changed to any exe program
DeviceProcessEvents
| where Timestamp > ago(7d)
| where FileName =~ "cmd.exe"
| project DeviceId, Timestamp, InitiatingProcessFileName, FileName,
ProcessCommandLine, InitiatingProcessIntegrityLevel, InitiatingProcessParentFileName
```

### Find use of WMIC to delete backups before ransomware execution
```
DeviceProcessEvents
| where Timestamp > ago(7d)
| where FileName =~ "wmic.exe"
| where ProcessCommandLine has "shadowcopy" and ProcessCommandLine has "delete"
| project DeviceId, Timestamp, InitiatingProcessFileName, FileName,
ProcessCommandLine, InitiatingProcessIntegrityLevel, InitiatingProcessParentFileName
```
```
let relevant_computers=
DeviceInfo
| where MachineGroup == "My_MachineGroup" 
| summarize make_list(DeviceName);
let relevant_users=
AccountInfo
| where EmailAddress endswith "@allowed.users"
| summarize make_list(AccountName);
DeviceLogonEvents
| where Timestamp > ago(1d)
| where DeviceName in (relevant_computers)
| where AccountName !in (relevant_users)
| project DeviceName, AccountName
```



### go to MS defender Advanced Threat Hunting and do a Query depending on your needs: 
```
// Find use of WMIC 
// This can be changed to any exe program
// limit the output to just one device by DeviceName
DeviceProcessEvents
| where Timestamp > ago(7d)
| where DeviceName contains "<DeviceName>"
| where FileName =~ "wmic.exe"
| project DeviceId, Timestamp, InitiatingProcessFileName, FileName,
ProcessCommandLine, InitiatingProcessIntegrityLevel, InitiatingProcessParentFileName
```
This Query will look for any devices running WMIC commands and is reducing the output to information about just one machince based on DeviceName. This will make it faster to narrow down what happened. 





### O365:
```
let fileName = "<File-Name>";
let fileSha1 = "<SHA1-Hash>";
search in (DeviceFileEvents, EmailAttachmentInfo, AppFileEvents)
Timestamp between (ago(1d) .. now())
and FileName =~ fileName
// or InitiatingProcessFileName =~ fileName
// or SHA1 == fileSha1
// or InitiatingProcessSHA1 == fileSha1
```




