to look for an increase or decrease in incoming logs (alerts) to sentinel. 

```
let Base = union withsource = _TableName *
| where 'All Tables' == 'All Tables' or _TableName == 'All Tables'
| where TimeGenerated > startofday(ago(30d)) and TimeGenerated < now(-1hour)
| summarize AvgVolume = avg(Quantity)
| project AvgVolume, MyKey = "Key";
// pull current data
let LastHour = union withsource = _TableName *
| where 'All Tables' == 'All Tables' or _TableName == 'All Tables'
| where TimeGenerated > now(-1hour)
| summarize RecentVolume = avg(Quantity)
| project RecentVolume, MyKey = "Key";
// join the baseline and the current data
Base | join LastHour on MyKey
// do math on data to determine how much of a change has happened and return a Difference Percentage
| extend ['Difference %'] = (RecentVolume/AvgVolume) * 100 - 100
| project ['Difference %'] < -10 //or ['Difference %'] > 10
```


```
//Log (alert) Ingestion Increase/Decrease
//compare alert ingestion from a week ago until 2 hours ago
//compare it against the last 2 hours
//if there is more than a 20% Increase or Decrease alert everyone to investigate. 
//
// establish a baseline to compare against 
let Base = CommonSecurityLog | union SecurityEvents_CL, AWSWAFLog_PCF_IE_CL, OfficeActivity, DHCP_CL, AWSCloudTrail, SigninLogs, BehaviorAnalytics, Okta_CL, Event_CL, AWSWAFLog_TWX_PROD_CL, AWSWAFLog_TWX_NONPROD_CL, AWSWAFLog_PCF_FW_CL, AuditLogs, Syslog, AzureActivity, AzureMetrics, Heartbeat, IdentityInfo, Usage, Operation, SecurityIncident, SecurityAlert, Anomalies, AzureDiagnostics
| where TimeGenerated > startofday(ago(7d)) and TimeGenerated < now(-2hour)
| summarize AvgVolume = avg(Quantity)
| project AvgVolume, MyKey = "Key";
// pull current data
let LastHour = CommonSecurityLog | union SecurityEvents_CL, AWSWAFLog_PCF_IE_CL, OfficeActivity, DHCP_CL, AWSCloudTrail, SigninLogs, BehaviorAnalytics, Okta_CL, Event_CL, AWSWAFLog_TWX_PROD_CL, AWSWAFLog_TWX_NONPROD_CL, AWSWAFLog_PCF_FW_CL, AuditLogs, Syslog, AzureActivity, AzureMetrics, Heartbeat, IdentityInfo, Usage, Operation, SecurityIncident, SecurityAlert, Anomalies, AzureDiagnostics
| where TimeGenerated > now(-2hour)
| summarize RecentVolume = avg(Quantity)
| project RecentVolume, MyKey = "Key";
// join the baseline and the current data
Base | join LastHour on MyKey  
// do math on data to determine how much of a change has happened and return a Difference Percentage
| extend ['Difference %'] = (RecentVolume/AvgVolume) * 100 - 100
```



# GENERIC:
```
//Log (alert) Ingestion Increase/Decrease
//compare alert ingestion from a week ago until 2 hours ago
//compare it against the last 2 hours
//if there is more than a 20% Increase or Decrease alert everyone to investigate. 
//
// establish a baseline to compare against 
let Base = search "*"
| where TimeGenerated > startofday(ago(7d)) and TimeGenerated < now(-2hour)
| summarize AvgVolume = avg(Quantity)
| project AvgVolume, MyKey = "Key";
// pull current data
let LastHour = search "*"
| where TimeGenerated > now(-2hour)
| summarize RecentVolume = avg(Quantity)
| project RecentVolume, MyKey = "Key";
// join the baseline and the current data
Base | join LastHour on MyKey  
// do math on data to determine how much of a change has happened and return a Difference Percentage
| extend ['Difference %'] = (RecentVolume/AvgVolume) * 100 - 100
```

## TO FIND ALL TABLES USE:
```
search "*" | summarize count() by $table | sort by count_ desc
```



# To do it per table:
this will tell us the difference as a percentage positive or negative. this is great for over all log ingestion but you may miss lesser used logs depending on how many are coming in. for instance if we flag on a 20% difference and one of the log collectors only makes up 5% of total logs collected then we would not notice it stop functioning. And after the initial baseline time has passed it would just seem normal. The only real solution for that would be to setup an alert on each individual log table like pseudo code below:

*** Dependant on search "*" working in logic app ***
for table in KQL: 

```
search "*" | summarize count() by $table | sort by count_ desc
```

run KQL:
```
// establish a baseline to compare against 
let Base = <table>
| where TimeGenerated > startofday(ago(7d)) and TimeGenerated < now(-2hour)
| summarize AvgVolume = avg(Quantity)
| project AvgVolume, MyKey = "Key";
// pull current data
let LastHour = <table>
| where TimeGenerated > now(-2hour)
| summarize RecentVolume = avg(Quantity)
| project RecentVolume, MyKey = "Key";
// join the baseline and the current data
Base | join LastHour on MyKey  
// do math on data to determine how much of a change has happened and return a Difference Percentage
| extend ['Difference %'] = (RecentVolume/AvgVolume) * 100 - 100
```
if "Difference %" is beyond allowable variance (20%?) 
create medium-high incident referencing <table> and <workspace> for Analyst to look at


### Note: 
```
let Base = union withsource = _TableName *
| where 'All Tables' == 'All Tables' or _TableName == 'All Tables'
```
can replace 
```
let Base = search "*"
```
