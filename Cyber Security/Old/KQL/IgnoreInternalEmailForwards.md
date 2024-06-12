### built to ignore email forwards setup for internal email addresses. 
```
OfficeActivity
| where Operation in~ ( "Add-MailboxPermission", "Add-MailboxFolderPermission", "Set-Mailbox", "New-ManagementRoleAssignment")
and not(UserId has_any ('NT AUTHORITY\\SYSTEM (Microsoft.Exchange.ServiceHost)', 'NT AUTHORITY\\SYSTEM (w3wp)','devilfish-applicationaccount') and Operation in~ ( "Add-MailboxPermission", "Set-Mailbox"))
// Allow alerts that don't relate to forwarding emails
// Allow alerts that are forwarding emails so long as they aren't to internal accounts
| where Parameters !contains "ForwardingSmtpAddress" or (Parameters contains "ForwardingSmtpAddress" and Parameters !contains "@Domain.com")
// Ignore removing of email forwards because that is not alert worthy
| where Parameters !contains '{"Name":"ForwardingSmtpAddress","Value":""}'
| extend timestamp = TimeGenerated, AccountCustomEntity = UserId, IPCustomEntity = ClientIP
```
