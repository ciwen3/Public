# Potential Web Shell Process Execution
Web shells are internet-accessible malicious files implanted in a victim's web server (or endpoint) file system to maintain persistent access and facilitate remote code execution. Web shells range from simple single commands to advanced multi-staged attacks, allowing the adversary actor to proceed with the same user account privileges as the exploited user or web application. For example, if an application has administrator access, the adversary could use a web shell to access sensitive databases or systems with admin privileges. Detecting and removing web shells immediately is critical to prevent consistent access, harvesting, and exfiltration of sensitive data and credentials. Microsoft has identified increased web shell attacks by various APTs (e.g., China Chopper, Deep Panda, Tropic Trooper, Volt Typhoon, Gallium Group, and Lazarus Group) targeting private and public organizations to gain a foothold into the target networks. Adversaries often leave web shells on public facing web servers (or endpoints) with simple or non-existent authentication mechanisms for persistent attacks. Once a web shell is successfully implanted, an attacker's goal will likely be to execute malicious commands and steal data. Unmitigated web shells provide attackers with persistence in the network, risking the organization's security posture by pivoting and escalating to compromise other hosts and data, even if it's not externally accessible.

### Scenario:
Look for suspicious process that IIS worker process (w3wp.exe), nginx, Apache HTTP server processes (httpd.exe, visualsvnserver.exe), etc. do not typically initiate (e.g., cmd.exe, powershell.exe and /bin/bash)

### Scenario:
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