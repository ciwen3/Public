# Find Duplicates:
```
SecurityAlert
| summarize AlertIds=make_set(SystemAlertId) by AlertName, Entities // make an array of SystemAlertIds that have the same AlertName and Entities
| extend AlertCount = array_length(AlertIds) // Count number of SystemAlertIds in the array
| where AlertCount > 1 // only show me duplicates
```

## Check to make sure all have the same Entities and AlertName:
```
//Example:
SecurityAlert
| where SystemAlertId in("00000000-0000-0000-0000-000000000000","00000000-0000-0000-0000-000000000000","00000000-0000-0000-0000-000000000000")
// replace the SystemAlertId's with the ones you want to check.
```
