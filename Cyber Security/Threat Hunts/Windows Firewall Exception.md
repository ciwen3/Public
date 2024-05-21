# Windows Firewall Exception
This is informational because this activity happens a lot when installing applications. By capturing it as informational Fusion will combine it with any other potentially malicious activity to enhance our understanding of what might be happening. Not expected to be worked alone. 

### EXECUTIVE SUMMARY
Windows Firewall is a host-based firewall that is included with every version of the operating system from Windows XP SP2 and is enabled by default on all Windows editions. Microsoft recommends you keep the built in Firewall on, even if you already have another firewall on. The firewall helps protect you from unauthorized access. Because of this threat actors may disable or modify the Firewall to prevent it from blocking connections to a command-and-control (C2) server or to download further instructions or exfiltrate data. Common protocols that get allowed through include by threat actors SSH, RDP, FTP, and anything that can help facilitate their malicious activity. In the past we have seen threat actors like Conti, Magic Hound, carbanak, and SolarWinds attack modify the firewall rules to allow their actions to continue unimpeded. There is also a history of groups like H1N1, ZxShell, DarkComet, and the Lazarus Group disabling the firewall altogether.

### HYPOTHESIS
Using a combination of built-in event ids and looking for commands the specific commands that can turn it off, we are able to monitor when the firewall is disabled or manipulated. Using this to alert will give us a possible indicator of malicious activity. This combined with other alerts and using Sentinel's Fusion technology would let us know of when there are multiple indicators for the same account or device and elevate the severity level so that the alerts are given more scrutiny.

## MITRE ATT&CK 
###  Tactics:
• Defense Evasion https://attack.mitre.org/tactics/TA0005/

###  Techniques:
• Impair Defenses: Disable or Modify System Firewall https://attack.mitre.org/techniques/T1562/004/
• Impair Defenses: Disable or Modify Cloud Firewall https://attack.mitre.org/techniques/T1562/007/

## TECHNICAL SUMMARY
###  OVERVIEW
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
//4946: A change has been made to Windows Firewall exception list. A rule was added
//4947: A change has been made to Windows Firewall exception list. A rule was modified
//4950: A Windows Firewall setting has changed
let regtrim = @'(?i)(\["\[\\"{|}"\]|\["\[\\"|"\]|\[""\])'
;
let FirewallEventId = dynamic(["4946", "4947", "4950"])
;
SecurityEvent
| where EventID in (FirewallEventId)
| extend i = split(EventData, '<Data Name="RuleId">', 1)
| extend rule = split(i, '</Data>', 0)
| extend rulei = trim_start(regtrim, tostring(rule))
| extend RuleId = trim_end(regtrim, rulei)
| extend g = split(EventData, '<Data Name="RuleName">', 1)
| extend rulen = split(g, '</Data>', 0)
| extend rulena = trim_start(regtrim, tostring(rulen))
| extend RuleName = trim_end(regtrim, rulena)
| project TimeGenerated, RuleId, RuleName, EventID, Activity, EventData, Computer
```