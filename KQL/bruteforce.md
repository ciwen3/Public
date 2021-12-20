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
| where TargetUserName !in (PasswordChanges)
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
