# Bruteforce custom exclude
look for bruteforce attempts on accounts who have not recently changed their passwords. 
find all bruteforce attempts, exclude anyone who recently changed their password (this could be a phone automatically trying to connect to email every 5 min). 

```
let threshold = 30;
let PasswordChanges = SecurityEvent
| where TimeGenerated > ago(24h)
| where EventID == 4723
| project TimeGenerated, Account, AccountType, SubjectUserName, TargetAccount = trim("@domain.com", TargetUserName), Computer, EventID, Activity
| distinct TargetAccount;
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
| extend timestamp = StartTime, AccountCustomEntity = Account, HostCustomEntity = Computer, IPCustomEntity = IpAddress, TargetAccount = trim("@domain.com", TargetUserName);
FailedLogins
| where TargetAccount !in (PasswordChanges)
```



```
let threshold = 30;
let PasswordChanges = SecurityEvent
| where TimeGenerated > ago(7d)
| where EventID == 4723
| project TimeGenerated, Account, AccountType, SubjectUserName, Test = trim("@domain.com", TargetUserName), Computer, EventID, Activity
| distinct Test;
let FailedLogins = SecurityEvent
| where TimeGenerated > ago(7d)
| where EventID == 4625
| where TargetUserName !in (PasswordChanges)
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
| extend timestamp = StartTime, AccountCustomEntity = Account, HostCustomEntity = Computer, IPCustomEntity = IpAddress, Test = trim("@domain.com", TargetUserName);
FailedLogins
| where Test !in (PasswordChanges)
| distinct Test
```
