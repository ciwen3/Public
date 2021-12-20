```
let threshold = 30;
let PasswordChanges = SecurityEvent
| where TimeGenerated > ago(24h)
| where EventID == 4723
| project TimeGenerated, Account, AccountType, SubjectUserName, AccountCustomEntity = trim("@domain.com", TargetUserName), Computer, EventID, Activity
| distinct AccountCustomEntity;
let FailedLogins = SecurityEvent
| where TimeGenerated > ago(10m)
| where EventID == 4625
| where AccountType =~ "User"
| where SubStatus !='0xc0000064' and Account !in ('\\', '-\\-')
// SubStatus '0xc0000064' signifies 'Account name does not exist'
| extend ResourceId = column_ifexists("_ResourceId", _ResourceId), SourceComputerId = column_ifexists("SourceComputerId", SourceComputerId)
| extend Reason = case(
SubStatus =~ '0xC000005E', 'There are currently no logon servers available to service the logon request.',
SubStatus =~ '0xC0000064', 'User logon with misspelled or bad user account',
SubStatus =~ '0xC000006A', 'User logon with misspelled or bad password',
SubStatus =~ '0xC000006D', 'Bad user name or password',
SubStatus =~ '0xC000006E', 'Unknown user name or bad password',
SubStatus =~ '0xC000006F', 'User logon outside authorized hours',
SubStatus =~ '0xC0000070', 'User logon from unauthorized workstation',
SubStatus =~ '0xC0000071', 'User logon with expired password',
SubStatus =~ '0xC0000072', 'User logon to account disabled by administrator',
SubStatus =~ '0xC00000DC', 'Indicates the Sam Server was in the wrong state to perform the desired operation',
SubStatus =~ '0xC0000133', 'Clocks between DC and other computer too far out of sync',
SubStatus =~ '0xC000015B', 'The user has not been granted the requested logon type (aka logon right) at this machine',
SubStatus =~ '0xC000018C', 'The logon request failed because the trust relationship between the primary domain and the trusted domain failed',
SubStatus =~ '0xC0000192', 'An attempt was made to logon, but the Netlogon service was not started',
SubStatus =~ '0xC0000193', 'User logon with expired account',
SubStatus =~ '0xC0000224', 'User is required to change password at next logon',
SubStatus =~ '0xC0000225', 'Evidently a bug in Windows and not a risk',
SubStatus =~ '0xC0000234', 'User logon with account locked',
SubStatus =~ '0xC00002EE', 'Failure Reason: An Error occurred during Logon',
SubStatus =~ '0xC0000413', 'Logon Failure: The machine you are logging onto is protected by an authentication firewall. The specified account is not allowed to authenticate to the machine',
strcat('Unknown reason substatus: ', SubStatus))
| summarize StartTime = min(TimeGenerated), EndTime = max(TimeGenerated), FailedLogonCount = count() by EventID,
Activity, Computer, Account, TargetAccount, TargetUserName, TargetDomainName,
LogonType, LogonTypeName, LogonProcessName, Status, SubStatus, Reason, ResourceId, SourceComputerId, WorkstationName, IpAddress
| where FailedLogonCount >= threshold
| extend timestamp = StartTime, AccountCustomEntity = trim("@domain.com", TargetUserName), HostCustomEntity = Computer, IPCustomEntity = IpAddress;
FailedLogins
| where AccountCustomEntity !in (PasswordChanges)
```


```
//Search for bruteforce attemtps
//exclude accounts with recent (past 24 hours) password changes as those are probably from an automatic login like a phone checking emails.
//
//set threshold
let threshold = 30;
//
//look for password changes in the last 24 hours
let PasswordChanges = SecurityEvent
| where TimeGenerated > ago(24h)
| where EventID == 4723
//clean up TargetUserName (sometimes it has the domain sometimes it doesn't)
| project Test = trim("@domain.com", TargetUserName)
//clean up duplicates
| distinct Test;
//
//look for failed logins that exceed threshold in last 10 minutes
let FailedLogins = SecurityEvent
| where TimeGenerated > ago(10m)
| where EventID == 4625
| where TargetUserName !in (PasswordChanges)
| where AccountType =~ "User"
// SubStatus '0xc0000064' signifies 'Account name does not exist'
| where SubStatus !='0xc0000064' and Account !in ('\\', '-\\-')
| summarize FailedLogonCount = count() by EventID, TargetUserName
| where FailedLogonCount >= threshold
| project Test = trim("@domain.com", TargetUserName);
//
//show bruteforce attempts for account that have not had password changes in the last 24 hours
FailedLogins
| where Test !in (PasswordChanges)
| distinct Test
```

```
//Search for bruteforce attemtps
//exclude accounts with recent (past 24 hours) password changes as those are probably from an automatic login like a phone checking emails.
//
//set failed login attempt threshold
let threshold = 30;
//
//look for password changes in the last 24 hours
let PasswordChanges = SecurityEvent
| where TimeGenerated > ago(24h)
| where EventID == 4723
//clean up TargetUserName (sometimes it has the domain sometimes it doesn't)
| project Test = trim("@domain.com", TargetUserName)
//clean up duplicates
| distinct Test;
//
//look for failed logins that exceed threshold in last 10 minutes
let FailedLogins = SecurityEvent
| where TimeGenerated > ago(10m)
| where EventID == 4625
//| where TargetUserName !in (PasswordChanges) //this line doesn't seem to be needed. 
| where AccountType =~ "User"
// SubStatus '0xc0000064' signifies 'Account name does not exist'
| where SubStatus !='0xc0000064' and Account !in ('\\', '-\\-')
| summarize FailedLogonCount = count() by EventID, TargetUserName
| where FailedLogonCount >= threshold
| project Test = trim("@domain.com", TargetUserName);
//
//show bruteforce attempts for account that have not had password changes in the last 24 hours
FailedLogins
| where Test !in (PasswordChanges)
| distinct Test
```


Not sure why but this one feels better to me. 
```
//Search for bruteforce attemtps
//exclude accounts with recent (past 24 hours) password changes as those are probably from an automatic login like a phone checking emails.
//
//set failed login attempt threshold
let threshold = 30;
//
//look for password changes in the last 24 hours
let PasswordChanges = SecurityEvent
| where TimeGenerated > ago(24h)
| where EventID == 4723
//clean up TargetUserName (sometimes it has the domain sometimes it doesn't)
| project Test = trim("@domain.com", TargetUserName)
//clean up duplicates
| distinct Test;
//
//look for failed logins that exceed threshold in last 10 minutes
let FailedLogins = SecurityEvent
| where TimeGenerated > ago(10m)
| where EventID == 4625
//| where TargetUserName !in (PasswordChanges) //this line doesn't seem to be needed. 
| where AccountType =~ "User"
// SubStatus '0xc0000064' signifies 'Account name does not exist'
| where SubStatus !='0xc0000064' and Account !in ('\\', '-\\-')
| project Test = trim("@domain.com", TargetUserName)
| summarize FailedLogonCount = count() by EventID, Test
| where FailedLogonCount >= threshold;
//
//show bruteforce attempts for account that have not had password changes in the last 24 hours
FailedLogins
| where Test !in (PasswordChanges)
| distinct Test
```
