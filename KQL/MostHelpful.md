# Find tables in Sentinel Logs that you can pull data from
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
```
search "*" | summarize count() by $table | sort by count_ desc
```
```
search * | summarize count() by $table |sort by count_ 
```
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






