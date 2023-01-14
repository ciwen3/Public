# find and base64 decode commands
```kql
let r2 = "(?i)(-en?c?o?d?e?d?C?o?m?m?a?n?d? |\\[(System\\.)*Text\\.Encoding\\]::\\w{4,}\\.GetString\\(\\[(System\\.)*Convert\\]::FromBase64String\\(|\\[(System\\.)*Convert\\]::FromBase64String\\(\\[Text\\.Encoding\\]::\\w{4,}\\.GetBytes\\()"
;
Event
| where RenderedDescription matches regex (r2)
| extend p1 = split(RenderedDescription, " -EncodedCommand ")
| extend p2 = split(p1[1], " ")
| extend b64 = tostring(p2.[0])
| extend b64d = base64_decode_tostring(b64)
| project-away p1, p2, b64
| summarize count() by b64d
```
