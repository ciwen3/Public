# remove duplicates
```
AzureActivity 
| where OperationName == 'Delete website' and ActivityStatus == 'Succeeded' and ResourceProvider == 'Azure Web Sites' 
| summarize arg_max(TimeGenerated, *) by CorrelationId
```

# Find tables in Sentinel Logs that you can pull data from
```
SecurityEvents
| summarize count() by Computer, Data = bin(TimeGenerated, 1d)
| render timechart
```
```
//looking for data table by cost
let StartofMonth = startofmonth(datetime(now), -3);
let EndofMonth = endofmonth(datetime(now), -1);
union withsource= table *
| where TimeGenerated between(StartofMonth ..(EndofMonth))
| where IsBillable == True
| summarize TotalGBytes =todecimal(round(sum(_BilledSize/(1024*1024*1024)),2)) by table, Date = bin(TimeGenerated, 1d)
```

```
search "*" | summarize count() by $table | sort by count_ desc
```
```
search * | summarize count() by $table |sort by count_ 
```
```
union withsource=_TableName *
| summarize Count=count() by _TableName
```
```
// Pull all table Names showing up in Sentinel
union withsource=_TableName *
| summarize Count=count() by _TableName
| render barchart
```

# Alert (Log) Ingestion Increase/Decrease
```
//Alert (Log) Ingestion Increase/Decrease
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
// do math on data to determine how much of a change has happened
// if comparison is 100 = everything is normal, 80 = there has been a 20% decrease in alerts (logs), 120 = there has been a 20% increase in alerts (logs)
| extend Comparison = (RecentVolume/AvgVolume) * 100 
| project Comparison
```


# Found these online but haven't gotten them to work yet 
```
.show database [DB] cslschema
```
```
.show table MyTable cslschema
```
```
.show table * cslschema
```
```
union *
// Get the Workspace Name(s) from a parameter
| extend stringtoSplit = split("{WorkspaceIDguid}",",")
| mv-expand stringtoSplit
| where stringtoSplit has TenantId
| extend workSpacename = trim(@"[^\w]+",tostring(split(stringtoSplit,":").[1]))
// end of get workspace name section
| summarize count() by TableName = Type, workSpacename
| order by workSpacename asc, count_ desc
```






