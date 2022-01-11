# Show the Current Date
for use in workbooks that will be printed to PDF for clients. this will auto fill the date (assuming the logs we are searching came in recently). 

```
AzureDiagnostics
| where TimeGenerated <= ago(3h)
| project format_datetime(TimeGenerated, 'MM-dd-yyyy')
| take 1 
```


