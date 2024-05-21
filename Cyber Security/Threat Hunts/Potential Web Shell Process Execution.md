# Potential Web Shell Process Execution
### EXECUTIVE SUMMARY
Web shells are internet-accessible malicious files implanted in a victim's web server (or endpoint) file system to maintain persistent access and facilitate remote code execution. Web shells range from simple single commands to advanced multi-staged attacks, allowing the adversary actor to proceed with the same user account privileges as the exploited user or web application. For example, if an application has administrator access, the adversary could use a web shell to access sensitive databases or systems with admin privileges. Detecting and removing web shells immediately is critical to prevent consistent access, harvesting, and exfiltration of sensitive data and credentials.

Microsoft has identified increased web shell attacks by various APTs (e.g., China Chopper, Deep Panda, Tropic Trooper, Volt Typhoon, Gallium Group, and Lazarus Group) targeting private and public organizations to gain a foothold into the target networks. Adversaries often leave web shells on public-facing web servers (or endpoints) with simple or non-existent authentication mechanisms for persistent attacks. Once a web shell is successfully implanted, an attacker's goal will likely be to execute malicious commands and steal data. Unmitigated web shells provide attackers with persistence in the network, risking the organization's security posture by pivoting and escalating to compromise other hosts and data, even if it's not externally accessible.

### Hypothesis
We can identify web shell activity that aligns with known threat actor methods by searching for indicators within process logs. If a web shell was dropped on a server it would inherit the permissions of the user or tool it is abusing. For this Threat hunt we will be looking for unexpected processes spawned by the web server. 

## MITRE ATT&CK
### Tactics:
    • Persistence https://attack.mitre.org/tactics/TA0003/ 

### Techniques:
    • Server Software Component https://attack.mitre.org/techniques/T1505/ 
    • Server Software Component: Web Shell https://attack.mitre.org/techniques/T1505/003/ 

## TECHNICAL SUMMARY
### Overview
Attackers install web shells on servers by taking advantage of security gaps, typically vulnerabilities in web applications, in internet-facing servers. These attackers scan the internet, often using public scanning interfaces like shodan.io, to locate servers to target. They may use previously fixed vulnerabilities that unfortunately remain unpatched in many servers, but they are also known to quickly take advantage of newly disclosed vulnerabilities.

Threat actors first penetrate a system or network and then install a web shell. From this point onwards, they use it as a permanent backdoor into the targeted web applications and any connected systems. The Web Shell always comes after another vulnerability has been exploited. This makes installing a Web Shell on a compromised system a secondary stage of the attack also known as post-exploitation activity.

A web shell is a shell-like interface that enables a web server to be remotely accessed. A web shell is unique in that a web browser is used to interact with it. A web shell could be programmed in any programming language that is supported on the victim server. Web shells are mostly written in PHP due to the widespread usage of PHP for web applications. Though Active Server Pages, ASP.NET, Python, Perl, Ruby, and Unix shell scripts are also used.

Many web application programming languages implement functions such as exec(), eval(), system(), and os(), which can be used to execute system commands. Threat groups abuse this functionality by smuggling these default functions and commands via web shells, allowing for remote tasking and code execution. The scope and breadth of code execution are arbitrary and only limited by the capabilities of the underlying victim server operating system shell.

### Threat Description 
An attacker can use a web shell on a web server to issue shell commands, perform privilege escalation, modify (upload, download, and delete) files, and execute malware. The threat actor can then host malware on the server as a "watering hole" for lateral scanning and infection within the network.

Unlike other forms of persistent remote access, web shells can be difficult to detect because they do not initiate connections. The footprint of the web shell on the server may be small and innocuous-looking, but there are multiple ways to look for it. In this threat hunt, we will be focusing on process creation. 

### Prevention Recommendations
    • Disable or Remove Feature or Program: Consider disabling functions from web technologies such as PHP’s evaI() that may be abused for web shells.
    • User Account Management: Enforce the principle of least privilege by limiting privileges of user accounts so only authorized accounts can modify the web directory.
    • Web Application Permissions: When defining permissions for web applications, it is important to employ the least privilege concept. The main principle behind this concept is to provide users with the bare minimum of privileges required to perform their role. The goal is to ensure that each user does not have privileges they should not have and that compromised accounts are restricted in their actions. The least privilege principle can help prevent threat actors from uploading a web shell to vulnerable applications. You can set it by not enabling web applications to directly write to a web-accessible directory or modify web-accessible code. This way, the server blocks the actor from accessing the web-accessible directory.
    • Web application firewalls (WAF) protect against threats by filtering, monitoring, and blocking HTTP traffic flowing to and from web services.
    • Keep system and software patched and up to date, to prevent web shells from being dropped at all. 
    • If you cannot patch your web applications, consider creating IIS rewrite rules, disabling Unified Messaging services, and disabling multiple Internet Information Services (IIS) application pools. These stopgap measures may affect the internal and external availability of your applications, depending on which products your organization uses.

### Mitigation Recommendations
    • If Malicious web shell is identified, the file should be removed immediately. The server should be analyzed to understand when the file was created or added and how it got there. The file could have been added in many ways from XSS, command injection, or software vulnerability so attribution might not be possible. 
    • If there are logs that show the web shells activity use that to determine the scope and severity of the hack. If there aren’t any logs then start checking all networks, devices, and users that could be reached or connected to this server for suspicious activity. 
    • If possible, quarantine or take the server offline. Consider starting a new server or restoring it from a known clean backup before the web shell was dropped. 

### References 
    1. https://attack.mitre.org/techniques/T1505/003/ 
    2. https://attack.mitre.org/techniques/T1505/ 
    3. https://www.imperva.com/learn/application-security/web-shell/ 
    4. https://redcanary.com/threat-detection-report/trends/webshells/ 

### Scenario 1:
Look for suspicious process that IIS worker process (w3wp.exe), nginx, Apache HTTP server processes (httpd.exe, visualsvnserver.exe), etc. do not typically initiate (e.g., cmd.exe, powershell.exe and /bin/bash)

### Scenario 2:
Look for suspicious web shell execution, this can identify processes that are associated with remote execution and reconnaissance activity (example: “arp”, “certutil”, “cmd”, “echo”, “ipconfig”, “gpresult”, “hostname”, “net”, “netstat”, “nltest”, “nslookup”, “ping”, “powershell”, “psexec”, “qwinsta”, “route”, “systeminfo”, “tasklist”, “wget”, “whoami”, “wmic”, etc.)

# KQL:
```kql
let webservers = dynamic(["beasvc.exe", "coldfusion.exe", "httpd.exe", "owstimer.exe", "visualsvnserver.exe", "w3wp.exe", "tomcat", "apache2", "nginx"]);
let linuxShells = dynamic(["/bin/bash", "/bin/sh", "python", "python3"]);
let windowsShells = dynamic(["powershell.exe", "powershell_ise.exe", "cmd.exe", "net.exe"]);
let exclusions = dynamic(["csc.exe", "php-cgi.exe", "vbc.exe", "conhost.exe", "print.exe"]);
DeviceProcessEvents
| where (InitiatingProcessParentFileName in~(webservers) or InitiatingProcessCommandLine in~(webservers))
| where (InitiatingProcessFileName in~(windowsShells) or InitiatingProcessCommandLine has_any(linuxShells))
| where FileName !in~ (exclusions)
| extend Reason = iff(InitiatingProcessParentFileName in~ (webservers), "Suspicious web shell execution", "Suspicious webserver process")
```