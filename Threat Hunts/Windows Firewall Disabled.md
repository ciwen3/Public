# Windows Firewall Disabled
### EXECUTIVE SUMMARY
Windows Firewall is a host-based firewall that is included with every version of the operating system from Windows XP SP2 and is enabled by default on all Windows editions. Microsoft recommends you keep the built in Firewall on, even if you already have another firewall on. The firewall helps protect you from unauthorized access. Because of this threat actors may disable or modify the Firewall to prevent it from blocking connections to a command-and-control (C2) server or to download further instructions or exfiltrate data. Common protocols that get allowed through include by threat actors SSH, RDP, FTP, and anything that can help facilitate their malicious activity. In the past we have seen threat actors like Conti, Magic Hound, carbanak, and SolarWinds attack modify the firewall rules to allow their actions to continue unimpeded. There is also a history of groups like H1N1, ZxShell, DarkComet, and the Lazarus Group disabling the firewall altogether.

### HYPOTHESIS
Using a combination of built-in event ids and looking for commands the specific commands that can turn it off, we are able to monitor when the firewall is disabled or manipulated. Using this to alert will give us a possible indicator of malicious activity. This combined with other alerts and using Sentinels Fusion technology would let us know of when there are multiple indicators for the same account or device and elevate the severity level so that the alerts are given more scrutiny.

## MITRE ATT&CK 
### Tactics:
• Defense Evasion https://attack.mitre.org/tactics/TA0005/

### Techniques:
• Impair Defenses: Disable or Modify System Firewall https://attack.mitre.org/techniques/T1562/004/
• Impair Defenses: Disable or Modify Cloud Firewall https://attack.mitre.org/techniques/T1562/007/

## TECHNICAL SUMMARY
### OVERVIEW
Windows Firewall is a security feature that helps to protect your device by filtering network traffic that enters and exits your device. This traffic can be filtered based on several criteria, including source and destination IP, protocol, or source and destination port number. Windows Firewall can be configured to block or allow network traffic based on the services and applications that are installed on your device. This allows you to restrict network traffic to only those applications and services that are explicitly allowed to communicate on the network.
Windows Firewall also works with Network Location Awareness so that it can apply security settings appropriate to the types of networks to which the device is connected. For example, Windows Firewall can apply the public network profile when the device is connected to a coffee shop wi-fi, and the private network profile when the device is connected to the home network. This allows you to apply more restrictive settings to public networks to help keep your device secure.

### THREAT DESCRIPTION
The firewall helps protect you from unauthorized access. Because of this threat actors may disable or modify the Firewall to prevent it from blocking connections to a command-and-control (C2) server or to download further instructions or exfiltrate data.

### PREVENTION RECOMMENDATIONS
• Audit - Routinely check account role permissions to ensure only expected users and roles have permission to modify system firewalls.
• Restrict File and Directory Permissions - Ensure proper process and file permissions are in place to prevent adversaries from disabling or modifying firewall settings.
• Restrict Registry Permissions - Ensure proper Registry permissions are in place to prevent adversaries from disabling or modifying firewall settings.
• User Account Management - Ensure proper user permissions are in place to prevent adversaries from disabling or modifying firewall settings.

### MITIGATION RECOMMENDATIONS
If these actions were not authorized or expected, you should investigate the user that performed the actions. Was it a service account or a user? If a user took the actions, then you should check with them to see why and take appropriate actions. If it was a service account, I would first check to see if it happened during installation of software. Some software may need to add rules to work properly. If you have ruled out normal user activity and expected service account actions, then I would assume the computer has been breached. At that point you should isolate the device and user related to the malicious activity. The users account should be locked, a password reset, any active sessions logged out, and if possible, MFA setup. If you aren't 100% sure all malware was removed with a scan or if this were a mission critical device, I would consider reinstalling the OS and setting up the device from scratch.

# KQL:
```kql
//registry
let DisableFirewallreg = @'(?i)(.*)Set-ItemProperty -Path (")?registry::(HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\mpssvc|HKLM\\SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\StandardProfile)(")? -Name (Start -Value 4|EnableFirewall -Value 0)(.*)'
;
//netsh commands
let DisableFirewallnetsh = @'(?i)(.*)NetSh(.exe")?(\s)+(Adv)?firewall set (allprofiles |currentprofile |domainprofile |privateprofile |opmode DISABLE|opmode mode=disable)(state off|firewallpolicy allowinbound,allowoutbound)?(.*)'
;
// net and sc commands
let DisableFirewallsc = @'(?i)(.*)(sc|net)(.exe")?\s+(config |stop )mpssvc( start=(\s)?disabled)?(.*)'
;
//NetFirewallProfile
let DisableFirewallps = @'(?i)(.*)Set-NetFirewallProfile -(\D+) -Enabled False(.*)'
;
let SEvent = SecurityEvent
| where CommandLine matches regex DisableFirewallreg or CommandLine matches regex DisableFirewallnetsh or CommandLine matches regex DisableFirewallsc or CommandLine matches regex DisableFirewallps
;
let DEvent = DeviceEvents
| where InitiatingProcessCommandLine matches regex DisableFirewallreg or InitiatingProcessCommandLine matches regex DisableFirewallnetsh or InitiatingProcessCommandLine matches regex DisableFirewallsc or InitiatingProcessCommandLine matches regex DisableFirewallps
| where ProcessCommandLine matches regex DisableFirewallreg or ProcessCommandLine matches regex DisableFirewallnetsh or ProcessCommandLine matches regex DisableFirewallsc or ProcessCommandLine matches regex DisableFirewallps
;
let DPEvent = DeviceProcessEvents
| where InitiatingProcessCommandLine matches regex DisableFirewallreg or InitiatingProcessCommandLine matches regex DisableFirewallnetsh or InitiatingProcessCommandLine matches regex DisableFirewallsc or InitiatingProcessCommandLine matches regex DisableFirewallps
| where ProcessCommandLine matches regex DisableFirewallreg or ProcessCommandLine matches regex DisableFirewallnetsh or ProcessCommandLine matches regex DisableFirewallsc or ProcessCommandLine matches regex DisableFirewallps
;
let DFEvent = DeviceFileEvents
| where InitiatingProcessCommandLine matches regex DisableFirewallreg or InitiatingProcessCommandLine matches regex DisableFirewallnetsh or InitiatingProcessCommandLine matches regex DisableFirewallsc or InitiatingProcessCommandLine matches regex DisableFirewallps
;
let DREvent = DeviceRegistryEvents
| where InitiatingProcessCommandLine matches regex DisableFirewallreg or InitiatingProcessCommandLine matches regex DisableFirewallnetsh or InitiatingProcessCommandLine matches regex DisableFirewallsc or InitiatingProcessCommandLine matches regex DisableFirewallps
;
let SLog = Syslog
| where SyslogMessage matches regex DisableFirewallreg or SyslogMessage matches regex DisableFirewallnetsh or SyslogMessage matches regex DisableFirewallsc or SyslogMessage matches regex DisableFirewallps
;
SEvent
| join kind=fullouter (SLog) on TimeGenerated
| join kind=fullouter (DPEvent) on TimeGenerated
| join kind=fullouter (DFEvent) on TimeGenerated
| join kind=fullouter (DREvent) on TimeGenerated
| join kind=fullouter (DEvent) on TimeGenerated
| extend InitiatingProcessCommandLine = coalesce(InitiatingProcessCommandLine, InitiatingProcessCommandLine1, InitiatingProcessCommandLine2, InitiatingProcessCommandLine3)
| extend ProcessCommandLine = coalesce(ProcessCommandLine, ProcessCommandLine1, SyslogMessage)
| extend TimeGenerated = coalesce(TimeGenerated, TimeGenerated1, TimeGenerated2, TimeGenerated3, TimeGenerated4, TimeGenerated5)
| extend DeviceName = coalesce(DeviceName, DeviceName1, DeviceName2, DeviceName3, Computer, Computer1)
| extend AccountName = coalesce(AccountName, AccountName1, AccountName2)
| extend InitiatingProcessAccountName = coalesce(InitiatingProcessAccountName, InitiatingProcessAccountName1, InitiatingProcessAccountName2)
| extend InitiatingProcessAccountUpn = coalesce(InitiatingProcessAccountUpn, InitiatingProcessAccountUpn1, InitiatingProcessAccountUpn2)
```