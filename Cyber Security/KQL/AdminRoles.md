Look up who has admin roles. 
```
// Admin roles
IdentityInfo
| mv-expand AssignedRoles
| where AssignedRoles matches regex 'Admin'
| summarize Roles = make_list(AssignedRoles) by AccountUPN = tolower(AccountUPN)
```
