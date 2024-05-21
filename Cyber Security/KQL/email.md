Extract Email address
```
SecurityAlert
| where AlertName contains "SharePointFileOperation via previously unseen IPs"
| extend email = extract(@"(urn:spo:guest#\w+@\w+\.\w+)", 1, Entities)
| summarize count() by email
```



