```kql
// Count of High Sevs per analyst
SecurityIncident
| where TimeGenerated >= ago(30d)
| where Status == "Closed"
| where Severity == "High"
| extend ResponseTime = (FirstModifiedTime - CreatedTime)
| extend Analyst = Owner.assignedTo
| where Analyst !in ("")
| summarize arg_max(TimeGenerated, *) by IncidentName
| summarize AvgResponseTime = avg(ResponseTime) by tostring(Analyst)
```
```kql
// Count of High Sevs per analyst
SecurityIncident
| where TimeGenerated >= ago(30d)
| where Status == "Closed"
| where Severity == "High"
| extend Analyst = Owner.assignedTo
| where Analyst !in ("")
| summarize arg_max(TimeGenerated, *) by IncidentName
| summarize Count = count() by tostring(Analyst)
```
```kql
// Count of High Sevs per analyst with response time
let AvgTime = SecurityIncident
| where TimeGenerated >= ago(30d)
| where Status == "Closed"
| where Severity == "High"
| extend ResponseTime = (FirstModifiedTime - CreatedTime)
| extend Analyst = Owner.assignedTo
| where Analyst !in ("")
| summarize arg_max(TimeGenerated, *) by IncidentName
| summarize AvgResponseTime = avg(ResponseTime) by tostring(Analyst)
;
let HighCount = SecurityIncident
| where TimeGenerated >= ago(30d)
| where Status == "Closed"
| where Severity == "High"
| extend Analyst = Owner.assignedTo
| where Analyst !in ("")
| summarize arg_max(TimeGenerated, *) by IncidentName
| summarize Count = count() by tostring(Analyst)
;
AvgTime
| join HighCount on Analyst
```
```kql
// Count by analyst and severity
SecurityIncident
| where TimeGenerated >= ago(30d)
| where Status == "Closed"
| extend Analyst = Owner.assignedTo
| where Analyst !contains "onmicrosoft.com"
| where Analyst !in ("null", "")
| summarize arg_max(TimeGenerated, *) by IncidentName
| summarize Count = count() by tostring(Analyst), Severity
```
```kql
// time chart analyst 30 day total incidents
SecurityIncident
| where TimeGenerated >= ago(30d)
| where Status == "Closed"
| extend Analyst = Owner.assignedTo
| where Analyst !contains "onmicrosoft.com"
| where Analyst !in ("null", "")
| summarize arg_max(TimeGenerated, *) by IncidentName
| summarize event_count = count() by Analyst, bin(TimeGenerated, 1d)
| render timechart
```
```kql
// analyst 30 day total incidents
SecurityIncident
| where TimeGenerated >= ago(30d)
| where Status == "Closed"
| extend Analyst = Owner.assignedTo
| where Analyst !contains "onmicrosoft.com"
| where Analyst !in ("null", "")
| summarize arg_max(TimeGenerated, *) by IncidentName
| summarize event_count = count() by Analyst, bin(TimeGenerated, 1d)
```
```kql
// CSV analyst 30 day total incidents by severity
// time chart analyst 30 day total incidents
SecurityIncident
| where TimeGenerated >= ago(30d)
| where Status == "Closed"
| extend Analyst = Owner.assignedTo
| where Analyst !contains "onmicrosoft.com"
| where Analyst !in ("null", "")
| summarize arg_max(TimeGenerated, *) by IncidentName
| summarize event_count = count() by Analyst, Severity, bin(TimeGenerated, 1d)
```
```kql
// last 24 hours
SecurityIncident
| where TimeGenerated >= ago(24h)
| where Status == "Closed"
| extend Owner = tostring(todynamic(Owner.assignedTo))
| summarize arg_max(TimeGenerated, *) by IncidentName
```
```kql
SecurityIncident
| where TimeGenerated >= ago(30d)
| where Severity == "High"
//| extend ResponseTime = (FirstModifiedTime - CreatedTime)
| extend Analyst = Owner.assignedTo
| where Analyst !in ("null", "")
| summarize arg_max(TimeGenerated, *) by IncidentName
| summarize Count = count() by tostring(Analyst)//, Severity
```
```kql
// how long on average from created till closed by analyst
SecurityIncident
| extend Tactics = todynamic(AdditionalData.tactics)
| extend Owner = todynamic(Owner.assignedTo)
| where Owner contains "<put name here>"
| extend Product = todynamic((parse_json(tostring(AdditionalData.alertProductNames))[0]))
| summarize arg_max(LastModifiedTime,*) by IncidentNumber
| extend TimeToClosure =  (ClosedTime - CreatedTime)/1h
| summarize 50th_Percentile=percentile(TimeToClosure, 50)
```
```kql
// how long on average from created till touched by analyst
SecurityIncident
| extend Tactics = todynamic(AdditionalData.tactics)
| extend Owner = todynamic(Owner.assignedTo)
| where Owner contains "<put name here>"
| extend Product = todynamic((parse_json(tostring(AdditionalData.alertProductNames))[0]))
| summarize arg_max(LastModifiedTime,*) by IncidentNumber
| extend TimeToTriage =  (FirstModifiedTime - CreatedTime)/1h
| summarize 50th_Percentile=percentile(TimeToTriage, 50)
```

```kql
// run in Sentinel Logs to see how many Incidents are being closed by each Analyst
SecurityIncident
//| where TimeGenerated >= ago(24h)
| where Status == "Closed"
| extend p = split(Owner, ":")
| extend m = tostring(p.[3])
| extend n = split(m, ",")
| extend o = tostring(n.[0])
| extend q = split(o, "\"")
| extend analyst = tostring(q.[1])
// Ignore Incidents closed without an assigned analyst
| where analyst != "null"
| where analyst != ""
| summarize Count=count() by analyst
| sort by Count desc 
```

### Improved version: 
```kql
SecurityIncident
| where TimeGenerated >= ago(30d)
| where Status == "Closed"
| extend Owner = tostring(todynamic(Owner.assignedTo))
| where Owner != "null"
| where Owner != ""
| summarize Count=count() by Owner
| sort by Count desc 
```

```kql
// Check across All workspaces
// This consumes a lot of resources and should be done with caution and only for short periods of time. 
union workspace('WorkspaceName').SecurityIncident, workspace('WorkspaceName').SecurityIncident, workspace('WorkspaceName').SecurityIncident // and so on based on the number of workspaces you want to search at once. 
| where TimeGenerated >= ago(1h)
| where Status == "Closed"
| extend p = split(Owner, ":")
| extend m = tostring(p.[3])
| extend n = split(m, ",")
| extend o = tostring(n.[0])
| extend q = split(o, "\"")
| extend analyst = tostring(q.[1])
// Ignore Incidents closed without an assigned analyst
| where analyst != "null"
| where analyst != ""
| summarize Count=count() by analyst
| sort by Count desc 
```

### Analyst/Owner by severity over 30 days
```kql
SecurityIncident
| where TimeGenerated >= ago(30d)
| where Status == "Closed"
| extend Owner = tostring(todynamic(Owner.assignedTo))
| where Owner != "null"
| where Owner != ""
| summarize Count=count() by Owner, Severity
| sort by Owner desc
```

### Analyst/Owner by severity over 30 days bin by day
```kql
SecurityIncident
| where TimeGenerated >= ago(30d)
| where Status == "Closed"
| extend Owner = tostring(todynamic(Owner.assignedTo))
| where Owner != "null"
| where Owner != ""
| summarize event_count = count() by Owner, bin(TimeGenerated, 1d)
```

### Time chart Analyst/Owner by severity over 30 days
```kql
SecurityIncident
| where TimeGenerated >= ago(30d)
| where Status == "Closed"
| extend Owner = tostring(todynamic(Owner.assignedTo))
| where Owner != "null"
| where Owner != ""
| summarize event_count = count() by Owner, bin(TimeGenerated, 1d)
| render timechart 
```

```kql
SecurityIncident
| where TimeGenerated >= ago(30d)
| where Status == "Closed"
| extend Owner = tostring(todynamic(Owner.assignedTo))
| where Owner !in("null", "")
| where Owner !contains "onmicrosoft.com"
| summarize event_count = count() by Owner, bin(TimeGenerated, 1d)
| render timechart 
```
### breakdown by hour
```kql
let High = SecurityIncident
| where TimeGenerated >= ago(7d)
| where Severity == "High"
| where Status == "Closed"
| extend Owner = tostring(todynamic(Owner.assignedTo))
| where Owner contains "Analyst Name Here"
| summarize arg_max(TimeGenerated, *) by IncidentName
| summarize AnalystHigh = count() by Severity, bin(TimeGenerated, 1h)
| project-away Severity
; 
let Low = SecurityIncident
| where TimeGenerated >= ago(7d)
| where Severity == "Low"
| where Status == "Closed"
| extend Owner = tostring(todynamic(Owner.assignedTo))
| where Owner contains "Analyst Name Here"
| summarize arg_max(TimeGenerated, *) by IncidentName
| summarize AnalystLow = count() by Severity, bin(TimeGenerated, 1h)
| project-away Severity
; 
let Medium = SecurityIncident
| where TimeGenerated >= ago(7d)
| where Severity == "Medium"
| where Status == "Closed"
| extend Owner = tostring(todynamic(Owner.assignedTo))
| where Owner contains "Analyst Name Here"
| summarize arg_max(TimeGenerated, *) by IncidentName
| summarize AnalystMedium = count() by Severity, bin(TimeGenerated, 1h)
| project-away Severity
; 
let AnalystTotal = SecurityIncident
| where TimeGenerated >= ago(7d)
| where Status == "Closed"
| extend Owner = tostring(todynamic(Owner.assignedTo))
| where Owner contains "Analyst Name Here"
| summarize arg_max(TimeGenerated, *) by IncidentName
| summarize AnalystTotal = count() by Status, bin(TimeGenerated, 1h)
| project-away Status
; 
let Total = SecurityIncident
| where TimeGenerated >= ago(7d)
| summarize arg_max(TimeGenerated, *) by IncidentName
| summarize Total = count() by Type, bin(TimeGenerated, 1h)
| project-away Type
;
Total 
| join kind=leftouter Low on TimeGenerated
| join kind=leftouter Medium on TimeGenerated
| join kind=leftouter High on TimeGenerated
| join kind=leftouter AnalystTotal on TimeGenerated
| extend Hour = TimeGenerated
| project Hour, Total, AnalystTotal, AnalystHigh, AnalystMedium, AnalystLow
```













