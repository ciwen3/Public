

## Summary of Insecure Protocols
```
// 1 month period not including this month
let StartofMonth = startofmonth(datetime(now), -1);
let EndofMonth = endofmonth(datetime(now), -1);
let scEvents = dynamic([5827, 5828, 5829, 5830, 5831]);
let legacyAuth = SigninLogs
| where TimeGenerated between(StartofMonth ..(EndofMonth))
| where ResultType == 0
| where ClientAppUsed !contains "Browser" and ClientAppUsed !contains "Mobile Apps and Desktop clients"
| summarize Count=count() by Protocol="AAD Legacy Auth";
SecurityEvent
| where TimeGenerated between(StartofMonth ..(EndofMonth))
| parse EventData with * '"TicketEncryptionType">' TicketEncryptionType '<' *
| union Event
| where (EventID == 2889) or (EventID == 3000 and EventLog == 'Microsoft-Windows-SMBServer/Audit') or (EventID == 4624 and AuthenticationPackageName == 'NTLM' and LmPackageName == 'NTLM V1' and Account !contains 'ANONYMOUS LOGON') or ((EventID == 4624 or EventID == 4776) and Level == 8 and PackageName contains 'WDigest') or (EventID == 4768 or EventID == 4769) and Level == 8 and (TicketEncryptionType != "0x12" and TicketEncryptionType != "0x11") or ((EventLog =~ "System" and Source =~ "NETLOGON") and EventID in (scEvents))
| summarize Count=count() by bin(TimeGenerated, 1d), tostring(EventID)
//| extend Protocol=replace(tostring(4776), 'WDigest', replace(tostring(4768), 'Kerberos weak cipher', replace(tostring(4769), 'Kerberos weak cipher', replace(tostring(2889), 'Insecure LDAP', replace(tostring(4624), 'NTLM v1', replace(tostring(3000), 'SMB v1', tostring(EventID)))))))
| extend Protocol = case(EventID == 4776, "WDigest", EventID == 4768 or EventID == 4769, "Weak Kerberos Cipher", EventID == 2889, "Insecure LDAP", EventID == 4624, "NTLM v1", EventID == 3000, "SMBv1", EventID in (scEvents), "Vulnerable Secure Channel", "Unknown")
| project Protocol, Count
| union legacyAuth
| sort by Count desc
```

```
// 1 month period not including this month
let StartofMonth = startofmonth(datetime(now), -1);
let EndofMonth = endofmonth(datetime(now), -1);
let scEvents = dynamic([5827, 5828, 5829, 5830, 5831]);
let legacyAuth = SigninLogs
| where TimeGenerated between(StartofMonth ..(EndofMonth))
| where ResultType == 0
| where ClientAppUsed !contains "Browser" and ClientAppUsed !contains "Mobile Apps and Desktop clients"
| summarize Count=count() by bin(TimeGenerated, 1d), Protocol="AAD Legacy Auth";
SecurityEvent
| where TimeGenerated between(StartofMonth ..(EndofMonth))
| parse EventData with * '"TicketEncryptionType">' TicketEncryptionType '<' *
| union Event
| where (EventID == 2889) or (EventID == 3000 and EventLog == 'Microsoft-Windows-SMBServer/Audit') or (EventID == 4624 and AuthenticationPackageName == 'NTLM' and LmPackageName == 'NTLM V1' and Account !contains 'ANONYMOUS LOGON') or ((EventID == 4624 or EventID == 4776) and Level == 8 and PackageName contains 'WDigest') or (EventID == 4768 or EventID == 4769) and Level == 8 and (TicketEncryptionType != "0x12" and TicketEncryptionType != "0x11") or ((EventLog =~ "System" and Source =~ "NETLOGON") and EventID in (scEvents))
| summarize Count=count() by bin(TimeGenerated, 1d), tostring(EventID)
//| extend Protocol=replace(tostring(4776), 'WDigest', replace(tostring(4768), 'Kerberos weak cipher', replace(tostring(4769), 'Kerberos weak cipher', replace(tostring(2889), 'Insecure LDAP', replace(tostring(4624), 'NTLM v1', replace(tostring(3000), 'SMB v1', tostring(EventID)))))))
| extend Protocol = case(EventID == 4776, "WDigest", EventID == 4768 or EventID == 4769, "Weak Kerberos Cipher", EventID == 2889, "Insecure LDAP", EventID == 4624, "NTLM v1", EventID == 3000, "SMBv1", EventID in (scEvents), "Vulnerable Secure Channel", "Unknown")
| project Protocol, Count, TimeGenerated
| union legacyAuth
| sort by Count desc
```

```
// 1 month period not including this month
let StartofMonth = startofmonth(datetime(now), -1);
let EndofMonth = endofmonth(datetime(now), -1);
let scEvents = dynamic([5827, 5828, 5829, 5830, 5831]);
let legacyAuth = SigninLogs
| where TimeGenerated between(StartofMonth ..(EndofMonth))
| where ResultType == 0
| where ClientAppUsed !contains "Browser" and ClientAppUsed !contains "Mobile Apps and Desktop clients"
| summarize FirstOccurance=min(TimeGenerated), LastOccurance=max(TimeGenerated), Count=count() by Protocol="AAD Legacy Auth";
SecurityEvent
| where TimeGenerated between(StartofMonth ..(EndofMonth))
| parse EventData with * '"TicketEncryptionType">' TicketEncryptionType '<' *
| union Event
| where (EventID == 2889) or (EventID == 3000 and EventLog == 'Microsoft-Windows-SMBServer/Audit') or (EventID == 4624 and AuthenticationPackageName == 'NTLM' and LmPackageName == 'NTLM V1' and Account !contains 'ANONYMOUS LOGON') or ((EventID == 4624 or EventID == 4776) and Level == 8 and PackageName contains 'WDigest') or (EventID == 4768 or EventID == 4769) and Level == 8 and (TicketEncryptionType != "0x12" and TicketEncryptionType != "0x11") or ((EventLog =~ "System" and Source =~ "NETLOGON") and EventID in (scEvents))
| summarize FirstOccurance=min(TimeGenerated), LastOccurance=max(TimeGenerated), Count=count() by tostring(EventID)
//| extend Protocol=replace(tostring(4776), 'WDigest', replace(tostring(4768), 'Kerberos weak cipher', replace(tostring(4769), 'Kerberos weak cipher', replace(tostring(2889), 'Insecure LDAP', replace(tostring(4624), 'NTLM v1', replace(tostring(3000), 'SMB v1', tostring(EventID)))))))
| extend Protocol = case(EventID == 4776, "WDigest", EventID == 4768 or EventID == 4769, "Weak Kerberos Cipher", EventID == 2889, "Insecure LDAP", EventID == 4624, "NTLM v1", EventID == 3000, "SMBv1", EventID in (scEvents), "Vulnerable Secure Channel", "Unknown")
| summarize FirstOccurance=min(FirstOccurance), LastOccurance=max(LastOccurance), Count=sum(Count) by Protocol
| union legacyAuth
| sort by Count desc
```


## 4720: A user account was created
```
// 1 month period not including this month
let StartofMonth = startofmonth(datetime(now), -1);
let EndofMonth = endofmonth(datetime(now), -1);
SecurityEvent
| where TimeGenerated between(StartofMonth ..(EndofMonth))
| where EventID == "4720"
| project TimeGenerated, Account=(AccountType), AdminAccount=(SubjectAccount), Computer
```

## 4738: A user account was changed
```
// 1 month period not including this month
let StartofMonth = startofmonth(datetime(now), -1);
let EndofMonth = endofmonth(datetime(now), -1);
SecurityEvent
| where TimeGenerated between(StartofMonth ..(EndofMonth))
| where EventID == "4738"
| where AccountType != "Machine"
| project TimeGenerated, Admin=(SubjectAccount), Computer, TargetUser=(TargetUserName), PasswordLastSet
| take 250
```

## Logons With Clear Text Password
```
// 1 month period not including this month
let StartofMonth = startofmonth(datetime(now), -1);
let EndofMonth = endofmonth(datetime(now), -1);
// Logons With Clear Text Password 
// Logons with clear text password by target account. 
SecurityEvent
| where TimeGenerated between(StartofMonth ..(EndofMonth))
| where EventID == 4624 and LogonType == 8
| summarize count() by TargetAccount
| take 250
```

## Admin Accounts created in Azure
```
// Looks for the creation of Admin account in Azure
// 1 month period not including this month
let StartofMonth = startofmonth(datetime(now), -1);
let EndofMonth = endofmonth(datetime(now), -1);
let PrivilegedGroups = dynamic(["UserAccountAdmins", "PrivilegedRoleAdmins", "TenantAdmins"]); 
AuditLogs 
| where TimeGenerated between(StartofMonth..EndofMonth)
| where Category =~ "RoleManagement" 
| where OperationName contains "Add member to role"
| mv-expand TargetResources 
| extend modifiedProperties = parse_json(TargetResources).modifiedProperties 
| mv-expand modifiedProperties 
| extend DisplayName = tostring(parse_json(modifiedProperties).displayName), GroupName = trim(@'"', tostring(parse_json(modifiedProperties).newValue)) 
| extend AppId = tostring(parse_json(parse_json(InitiatedBy).app).appId), InitiatedByDisplayName = tostring(parse_json(parse_json(InitiatedBy).app).displayName), ServicePrincipalId = tostring(parse_json(parse_json(InitiatedBy).app).servicePrincipalId), ServicePrincipalName = tostring(parse_json(parse_json(InitiatedBy).app).servicePrincipalName) 
| where GroupName in~ (PrivilegedGroups) 
| project TimeGenerated, AADOperationType, Category, OperationName, GroupName, ["Initiated By"] = InitiatedBy.user.userPrincipalName, ["Targeted User"] = TargetResources.userPrincipalName 
```


## Security-Enabled Group Creation
```
// look for security-enabled group creation
// 1 month period not including this month
let StartofMonth = startofmonth(datetime(now), -1);
let EndofMonth = endofmonth(datetime(now), -1);
let ID = dynamic(["4727", "4731", "4754"]); 
// 4727: A security-enabled global group was created.
// 4731: A security-enabled local group was created.
// 4754: A security-enabled universal group was created.
SecurityEvent
| where TimeGenerated between(StartofMonth ..(EndofMonth))
| where EventID in~ (ID)
| project TimeGenerated, Activity, AdminAccount=(SubjectAccount), Computer, TargetAccount
```



## A member was added to a security-enabled group
```
// A member was added to a security-enabled group.
// 1 month period not including this month
let StartofMonth = startofmonth(datetime(now), -1);
let EndofMonth = endofmonth(datetime(now), -1);
let ID = dynamic(["4728", "4732", "4756"]); 
// 4728: A member was added to a security-enabled global group.
// 4732: A member was added to a security-enabled local group.
// 4756: A member was added to a security-enabled universal group.
SecurityEvent
| where TimeGenerated between(StartofMonth ..(EndofMonth))
| where EventID in~ (ID)
| project TimeGenerated, Activity, AccountType, AdminAccount=(SubjectAccount), Computer, TargetAccount
| limit 250
```


























# Needs sorting
```

*****
let PrivilegedGroups = dynamic(["UserAccountAdmins", "PrivilegedRoleAdmins", "TenantAdmins"]); 
AuditLogs 
| where Category =~ "RoleManagement" 
| where OperationName contains "Add member to role"
| mv-expand TargetResources 
| extend modifiedProperties = parse_json(TargetResources).modifiedProperties 
| mv-expand modifiedProperties 
| extend DisplayName = tostring(parse_json(modifiedProperties).displayName), GroupName = trim(@'"', tostring(parse_json(modifiedProperties).newValue)) 
| extend AppId = tostring(parse_json(parse_json(InitiatedBy).app).appId), InitiatedByDisplayName = tostring(parse_json(parse_json(InitiatedBy).app).displayName), ServicePrincipalId = tostring(parse_json(parse_json(InitiatedBy).app).servicePrincipalId), ServicePrincipalName = tostring(parse_json(parse_json(InitiatedBy).app).servicePrincipalName) 
| where GroupName in~ (PrivilegedGroups) 
| project TimeGenerated, AADOperationType, Category, OperationName, GroupName, ["Initiated By"] = InitiatedBy.user.userPrincipalName, ["Targeted User"] = TargetResources.userPrincipalName 


// 1 month period not including this month
let StartofMonth = startofmonth(datetime(now), -1);
let EndofMonth = endofmonth(datetime(now), -1);
let lookback = StartofMonth - 14d;
let historicalActivity = OfficeActivity
| where TimeGenerated between(lookback..StartofMonth)
| where RecordType=="ExchangeAdmin" and UserType in ("Admin","DcAdmin")
| summarize historicalCount=count() by UserId;
let recentActivity = OfficeActivity
| where TimeGenerated between(StartofMonth..EndofMonth)
| where UserType in ("Admin","DcAdmin")
| summarize recentCount=count() by UserId;
recentActivity | join kind = leftanti (historicalActivity) on UserId
| project UserId,recentCount
| order by recentCount asc, UserId
| join kind = rightsemi(OfficeActivity
| where TimeGenerated between(StartofMonth..EndofMonth)
| where RecordType == "ExchangeAdmin" | where UserType in ("Admin","DcAdmin")) on UserId
| summarize StartTime = max(TimeGenerated), EndTime = min(TimeGenerated), count() by RecordType, Operation, UserType, UserId, OriginatingServer, ResultStatus
| extend timestamp = StartTime, AccountCustomEntity = UserId


SecurityEvent
//| where TimeGenerated between(StartofMonth ..(EndofMonth))
| where EventID == "4672" 
//4672: Special privileges assigned to new logon
| project Activity, Computer, Account, SubjectAccount, PrivilegeList
//| summarize count() by PrivilegeList

This event lets you know whenever an account assigned any "administrator equivalent" user rights logs on.  For instance you will see event 4672 in close proximity to logon events (4624) for administrators since administrators have most of these admin-equivalent rights. 



// 1 month period not including this month
let StartofMonth = startofmonth(datetime(now), -1);
let EndofMonth = endofmonth(datetime(now), -1);
let ID = dynamic(["4727", "4728", "4731", "4732"]); 
// 4727: A security-enabled global group was created.
// 4728: A member was added to a security-enabled global group.
// 4731: A security-enabled local group was created.
// 4732: A member was added to a security-enabled local group.
SecurityEvent
| where TimeGenerated between(StartofMonth ..(EndofMonth))
| where EventID in~ (ID)
| project TimeGenerated, Account=(AccountType), AdminAccount=(SubjectAccount), Computer


//let StartofMonth = startofmonth(datetime(now), -1);
//let EndofMonth = endofmonth(datetime(now), -1);
SecurityEvent
//| where TimeGenerated between(StartofMonth ..(EndofMonth))
| where EventID == "4717" 
//| where OperationType == "Object Access"
| extend p = split(EventData, " ")
| extend Name1 = tostring(p.[19])
| extend p2 = split(Name1, ">")
| extend Name2 = tostring(p2.[1])
| extend p3 = split(Name2, "<")
| extend Name3 = tostring(p3.[0])
//| extend AccessGranted = tostring(Name3.[0])
| project Activity, SubjectAccount, ['Acces Granted'] = Name3







From Hunting > New Admin Account activity
let starttime = todatetime('{{StartTimeISO}}');
let endtime = todatetime('{{EndTimeISO}}');
let lookback = starttime - 14d;
let historicalActivity=
OfficeActivity
| where TimeGenerated between(lookback..starttime)
| where RecordType=="ExchangeAdmin" and UserType in ("Admin","DcAdmin")
| summarize historicalCount=count() by UserId;
let recentActivity = OfficeActivity
| where TimeGenerated between(starttime..endtime)
| where UserType in ("Admin","DcAdmin")
| summarize recentCount=count() by UserId;
recentActivity | join kind = leftanti (
   historicalActivity
) on UserId
| project UserId,recentCount
| order by recentCount asc, UserId
| join kind = rightsemi
(OfficeActivity
| where TimeGenerated between(starttime..endtime)
| where RecordType == "ExchangeAdmin" | where UserType in ("Admin","DcAdmin"))
on UserId
| summarize StartTime = max(TimeGenerated), EndTime = min(TimeGenerated), count() by RecordType, Operation, UserType, UserId, OriginatingServer, ResultStatus
| extend timestamp = StartTime, AccountCustomEntity = UserId


OfficeActivity
| where RecordType == "ExchangeAdmin" 
| where UserType in ("Admin","DcAdmin")
| project RecordType, Operation, UserType, UserId, OriginatingServer, ResultStatus






Group added to Built in Domain Local or Global Group
let StartofMonth = startofmonth(datetime(now), -1);
let EndofMonth = endofmonth(datetime(now), -1);
let lookback = StartofMonth - 7d;
// For AD SID mappings - https://docs.microsoft.com/windows/security/identity-protection/access-control/active-directory-security-groups
let WellKnownLocalSID = "S-1-5-32-5[0-9][0-9]$";
// The SIDs for DnsAdmins and DnsUpdateProxy can be different than *-1102 and -*1103. Check these SIDs in your domain before running the query
let WellKnownGroupSID = "S-1-5-21-[0-9]*-[0-9]*-[0-9]*-5[0-9][0-9]$|S-1-5-21-[0-9]*-[0-9]*-[0-9]*-1102$|S-1-5-21-[0-9]*-[0-9]*-[0-9]*-1103$";
let GroupAddition = SecurityEvent
| where TimeGenerated between(lookback..StartofMonth)
// 4728 - A member was added to a security-enabled global group
// 4732 - A member was added to a security-enabled local group
// 4756 - A member was added to a security-enabled universal group
| where EventID in ("4728", "4732", "4756")
| where AccountType == "User" and MemberName == "-"
// Exclude Remote Desktop Users group: S-1-5-32-555
| where TargetSid !in ("S-1-5-32-555")
| where TargetSid matches regex WellKnownLocalSID or TargetSid matches regex WellKnownGroupSID
| project GroupAddTime = TimeGenerated, GroupAddEventID = EventID, GroupAddActivity = Activity, GroupAddComputer = Computer,
GroupAddTargetUserName = TargetUserName, GroupAddTargetDomainName = TargetDomainName, GroupAddTargetSid = TargetSid,
GroupAddSubjectUserName = SubjectUserName, GroupAddSubjectUserSid = SubjectUserSid, GroupSid = MemberSid, Account, Computer
| extend AccountCustomEntity = Account, HostCustomEntity = Computer;
let GroupCreated = SecurityEvent
| where TimeGenerated between(StartofMonth..EndofMonth)
// 4727 - A security-enabled global group was created
// 4731 - A security-enabled local group was created
// 4754 - A security-enabled universal group was created
| where EventID in ("4727", "4731", "4754")
| where AccountType == "User"
| project GroupCreateTime = TimeGenerated, GroupCreateEventID = EventID, GroupCreateActivity = Activity, GroupCreateComputer = Computer, GroupCreateTargetUserName = TargetUserName, GroupCreateTargetDomainName = TargetDomainName, GroupCreateSubjectUserName = SubjectUserName, GroupCreateSubjectDomainName = SubjectDomainName, GroupCreateSubjectUserSid = SubjectUserSid, GroupSid = TargetSid, Account, Computer;
GroupCreated
| join (GroupAddition) on GroupSid
| extend timestamp = GroupCreateTime, AccountCustomEntity = Account, HostCustomEntity = Computer





User Account added to Built in Domain Local or Global Group
// For AD SID mappings - https://docs.microsoft.com/windows/security/identity-protection/access-control/active-directory-security-groups
let WellKnownLocalSID = "S-1-5-32-5[0-9][0-9]$";
let WellKnownGroupSID = "S-1-5-21-[0-9]*-[0-9]*-[0-9]*-5[0-9][0-9]$|S-1-5-21-[0-9]*-[0-9]*-[0-9]*-1102$|S-1-5-21-[0-9]*-[0-9]*-[0-9]*-1103$";
SecurityEvent 
| where AccountType == "User"
// 4728 - A member was added to a security-enabled global group
// 4732 - A member was added to a security-enabled local group
// 4756 - A member was added to a security-enabled universal group
| where EventID in ("4728", "4732", "4756")   
| where TargetSid matches regex WellKnownLocalSID or TargetSid matches regex WellKnownGroupSID
// Exclude Remote Desktop Users group: S-1-5-32-555
| where TargetSid !in ("S-1-5-32-555")
| project StartTimeUtc = TimeGenerated, EventID, Activity, Computer, TargetUserName, TargetDomainName, TargetSid, UserPrincipalName, SubjectUserName, SubjectUserSid 
| extend timestamp = StartTimeUtc, HostCustomEntity = Computer, AccountCustomEntity = UserPrincipalName












https://dirteam.com/sander/2020/07/22/howto-set-an-alert-to-notify-when-an-additional-person-is-assigned-the-azure-ad-global-administrator-role/

AuditLogs
| where OperationName contains "Add member to role" and TargetResources contains "Company Administrator"


https://www.verboon.info/2020/09/hunting-for-local-group-membership-changes/

DeviceEvents
| where ActionType == "UserAccountAddedToLocalGroup"
| extend AddedAccountSID = tostring(parse_json(AdditionalFields).MemberSid)
| extend LocalGroup = AccountName
| extend LocalGroupSID = AccountSid
| extend Actor = trim(@"[^\w]+",InitiatingProcessAccountName)
| project Timestamp , DeviceName, AddedAccountSID , LocalGroup , LocalGroupSID , Actor


https://github.com/Azure/Azure-Sentinel/blob/master/Tools/RuleMigration/AnalyticsUseCases.md

Data sources: Azure AD and Windows Security Events. KQL Query:
let timeframe = 10m;let lookback = 1d;let account_created =SecurityEvent
 | where TimeGenerated > ago(lookback+timeframe)| where EventID == "4720"
 // A user account was created| where AccountType =~ "User"
| project creationTime = TimeGenerated, CreateEventID =
EventID,Activity, Computer, TargetUserName, UserPrincipalName,
 AccountUsedToCreate = SubjectUserName, TargetSid,
 SubjectUserSid;account_created | join kind= inner (account_deleted)
 on Computer, TargetUserName| where deletionTime - creationTime
 < lookback| where tolong(deletionTime - creationTime)
 >= 0|extend timestamp = creationTime, AccountCustomEntity
 = AccountUsedToCreate, HostCustomEntity = Computer*


https://github.com/Azure/Azure-Sentinel/issues/1795

//let timeframe = 1h; 
let OperationList = dynamic(["Add member to role", "Add member to role in PIM requested (permanent)"]); 
let PrivilegedGroups = dynamic(["UserAccountAdmins", "PrivilegedRoleAdmins", "TenantAdmins"]); 
AuditLogs 
//| where TimeGenerated >= ago(timeframe) 
| where LoggedByService =~ "Core Directory" 
| where Category =~ "RoleManagement" 
| where OperationName in~ (OperationList) 
| mv-expand TargetResources 
| extend modifiedProperties = parse_json(TargetResources).modifiedProperties 
| mv-expand modifiedProperties 
| extend DisplayName = tostring(parse_json(modifiedProperties).displayName), GroupName = trim(@'"', tostring(parse_json(modifiedProperties).newValue)) 
| extend AppId = tostring(parse_json(parse_json(InitiatedBy).app).appId), InitiatedByDisplayName = tostring(parse_json(parse_json(InitiatedBy).app).displayName), ServicePrincipalId = tostring(parse_json(parse_json(InitiatedBy).app).servicePrincipalId), ServicePrincipalName = tostring(parse_json(parse_json(InitiatedBy).app).servicePrincipalName) 
//| where DisplayName =~ "Role.WellKnownObjectName" 
| where GroupName in~ (PrivilegedGroups) // If you want to still alert for operations from PIM, remove below filtering for MS-PIM. 
| where InitiatedByDisplayName != "MS-PIM" 
| project TimeGenerated, AADOperationType, Category, OperationName, AADTenantId, AppId, InitiatedByDisplayName, ServicePrincipalId, ServicePrincipalName, DisplayName, GroupName 
| extend timestamp = TimeGenerated, AccountCustomEntity = ServicePrincipalName




OfficeActivity
//| where TimeGenerated between(starttime..endtime)
| where UserType contains "admin"
//| summarize count() by RecordType, Operation, UserType, UserId, OriginatingServer, ResultStatus
| summarize count() by UserType
```
