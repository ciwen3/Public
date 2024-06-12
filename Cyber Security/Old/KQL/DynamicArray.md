```kql
SecurityAlert
| where TimeGenerated >= ago(90d)
| extend EntitiesDynamicArray=parse_json(Entities) | mvexpand EntitiesDynamicArray 
| extend Entitytype = tostring(parse_json(EntitiesDynamicArray).Type)
| where Entitytype == "url"
| extend URL = tostring(parse_json(EntitiesDynamicArray).Url)
| where URL !contains "sharepoint"
```

```kql
SecurityAlert
| where AlertName has "Alert Title"
| extend EntitiesDynamicArray = parse_json(Entities) 
| mv-expand EntitiesDynamicArray
| extend EntityAddress = tostring(EntitiesDynamicArray.Address), EntityHostName = tostring(EntitiesDynamicArray.HostName), EntityAccountName = tostring(EntitiesDynamicArray.Name)
| project TimeGenerated, EntityAccountName, EntityAddress, EntityHostName, SystemAlertId
```
