## Private or Public IP:
```
let PrivateIPregex = @'^127\.|^10\.|^172\.1[6-9]\.|^172\.2[0-9]\.|^172\.3[0-1]\.|^192\.168\.';
| extend SourceIPType = iff(SourceIP matches regex PrivateIPregex, "private", "public")
| where SourceIPType == "public"
```
