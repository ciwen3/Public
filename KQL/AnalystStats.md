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























