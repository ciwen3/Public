# Seach For IP Addresses. 
In Sentinel Logs search for all Log Types that contain a certain IP Address. 

```
search "<IP-Address>"
```

```
find "<IP-Address>"
```

```
find "<IP-Address>"
| distinct $table
```

```
find "<IP-Address>"
| distinct source_
```