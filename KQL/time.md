```
AzureActivity
| where isnotempty(Time)
```
```
AzureDiagnostics
| where TimeGenerated <= ago(3h)
| project format_datetime(TimeGenerated, 'MM-dd-yyyy')
| take 1 
```
