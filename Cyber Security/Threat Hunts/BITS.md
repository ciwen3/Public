# BITS
### EXECUTIVE SUMMARY 
BITS (Background Intelligent Transfer Service) is a command-line tool that is built into Microsoft Windows and used to transfer large files to and from remote hosts while monitoring the progress. BITS is used by Windows Update, SUS, SMS and many third-party packages. In addition, BITSAdmin supports transfer of files between remote machines using idle network bandwidth. It can be throttled preventing the degradation in Quality-of-Service experience on the network making it hard to detect. This makes BITS very appealing to threat actors, like Black Basta, that use this for Ingress tool transfer and lateral movement within the network.  

### Hypothesis 
The objective of this threat hunt is to do detection of BITS being used to download or upload files outside normal use.  

## MITRE ATT&CK 
### Tactics: 
Defense Evasion https://attack.mitre.org/tactics/TA0005/  
Persistence https://attack.mitre.org/tactics/TA0003/  
### Techniques: 
BITS Jobs https://attack.mitre.org/techniques/T1197/  

## TECHNICAL SUMMARY 
### Overview 
"Background Intelligent Transfer Service" (BITS) is a technology created by Microsoft to manage file uploads and downloads, to and from web servers and SMB shares, in a controlled and load balanced way. BITS can survive reboots and network connection issues. If the connection is dropped BITS will automatically resume the file transfers as soon as possible, this makes it ideal for threat actors to drop malicious files. In recent years, BITS has been increasingly used to exfiltrate data from compromised computers. BITS is deprecated in Windows 7 / 2008 R2 and above, it is superseded by the new PowerShell BITS commandlets.  

### Threat Description  
BITS uses the command line tool bitsadmin.exe to facilitate the download or upload of files across the network with some additional capabilities. This includes the ability to run in the background, continue if the user is logged out, and resume after a network outage or computer reboot. BITS can do the file transfers over the following protocols: SMB, HTTP, HTTPS.  

bitsadmin.exe doesn't handle the transfer itself. It will create the job to be handled by svchost.exe and then exit. svchost.exe will manage the network transfer. Because the use of bitsadmin.exe is rare we should be able to identify and alert on the command being run and rule out any legitimate uses.  

### Triage 
This information is here in case an investigation is needed on the breached computer. This will help track down the information to identify what malicious activity happened related to bitsadmin.exe. For Hard Disk Analysis - three important files have artefacts specific to BITS 

1. Queue Manager Artefacts Aka State Files - C:\ProgramData\Microsoft\Network\Downloader\qmgr0.dat  
2. Queue Manager Artefacts Aka State Files - C:\ProgramData\Microsoft\Network\Downloader\qmgr1.dat  
3. Windows Event Logs - C:\Windows\System32\Winevt\Logs\Microsoft-Windows-Bits-ClientOperational.evtx 

- Event ID 3: information about the job creation 
- Event ID 59: information about the start of the service, "Bytes Transferred" value is zero. 
- Event ID 60: status of the job 
- Event ID 61: download failed. 
- Event ID 4: completion of the job, "Bytes Transferred" value is downloaded file size. 

If you don't know what the file name and download location is, then you can use these logs to get file size and time of file creation and use that to search for the file in question. 

### Mitigation Recommendations 
- Any account displaying malicious activity should have the password changed and ensure MFA is enforced. 
- Look for any other devices the user has had contact with (logged into) since the known breach and investigate those devices for malicious activity and files. 
- Isolate the device from the network and investigate for other malicious activity or files. 

### References  
https://ss64.com/nt/bitsadmin.html  
https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin  
https://learn.microsoft.com/en-us/windows/win32/bits/bitsadmin-tool  
https://learn.microsoft.com/en-us/powershell/module/bitstransfer/start-bitstransfer?view=windowsserver2022-ps  
https://lolbas-project.github.io/lolbas/Binaries/Bitsadmin/  
https://www.slideshare.net/chrisgates/windows-attacks-at-is-the-new-black-26672679  
https://www.youtube.com/watch?v=_8xJaaQlpBo  
https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f  
https://github.com/redcanaryco/atomic-red-team/blob/8eb52117b748d378325f7719554a896e37bccec7/atomics/T1105/T1105.md#atomic-test-9---windows---bitsadmin-bits-download  
https://github.com/redcanaryco/atomic-red-team/blob/bc705cb7aaa5f26f2d96585fac8e4c7052df0ff9/atomics/T1197/T1197.md  
https://thedfirreport.com/2021/03/29/sodinokibi-aka-revil-ransomware/  

# KQL
```kql
let lookbacktime = 90d
;
let BITScmd = @'(.*)bitsadmin(.exe)?(.+)(download |upload )(.*)'
;
let BITSpwsh = @'(.*)Start-BitsTransfer(.+)(((destination |source ).+){2}|Asynchronous |TransferType )(.*)'
;
let ClearObf = @'(\^|(")+|\$|%|\+|("\+"))'
;
let SEvent = SecurityEvent
| where TimeGenerated >= ago(lookbacktime)
| extend Deobf_CommandLine=replace_regex(CommandLine, ClearObf, '')
| where Deobf_CommandLine matches regex BITScmd or Deobf_CommandLine matches regex BITSpwsh
; 
let DEvent = DeviceEvents
| where TimeGenerated >= ago(lookbacktime)
| extend InitiatingDeobf_CommandLine=replace_regex(InitiatingProcessCommandLine, ClearObf, '')
| extend Deobf_CommandLine=replace_regex(ProcessCommandLine, ClearObf, '')
| where InitiatingDeobf_CommandLine matches regex BITScmd or Deobf_CommandLine matches regex BITScmd or InitiatingDeobf_CommandLine matches regex BITSpwsh or Deobf_CommandLine matches regex BITSpwsh
;
let DPEvent = DeviceProcessEvents
| where TimeGenerated >= ago(lookbacktime)
| extend InitiatingDeobf_CommandLine=replace_regex(InitiatingProcessCommandLine, ClearObf, '')
| extend Deobf_CommandLine=replace_regex(ProcessCommandLine, ClearObf, '')
| where InitiatingDeobf_CommandLine matches regex BITScmd or Deobf_CommandLine matches regex BITScmd or InitiatingDeobf_CommandLine matches regex BITSpwsh or Deobf_CommandLine matches regex BITSpwsh
;
SEvent
| join kind=fullouter (DPEvent) on TimeGenerated
| join kind=fullouter (DEvent) on TimeGenerated
| extend ProcessCommandLine = coalesce(ProcessCommandLine, ProcessCommandLine1, ProcessCommandLine2)
| extend InitiatingProcessCommandLine = coalesce(InitiatingProcessCommandLine, InitiatingProcessCommandLine1)
| extend InitiatingDeobf_CommandLine = coalesce(InitiatingDeobf_CommandLine, InitiatingDeobf_CommandLine1)
| extend Deobf_CommandLine = coalesce(Deobf_CommandLine, Deobf_CommandLine1, Deobf_CommandLine2)
| extend TimeGenerated = coalesce(TimeGenerated, TimeGenerated1, TimeGenerated2)
| extend DeviceName = coalesce(DeviceName, DeviceName1, Computer)
| extend AccountName = coalesce(AccountName, AccountName1, AccountName2)
| extend InitiatingProcessAccountName = coalesce(InitiatingProcessAccountName, InitiatingProcessAccountName1)
| extend InitiatingProcessAccountUpn = coalesce(InitiatingProcessAccountUpn, InitiatingProcessAccountUpn1)
```

# KB
This Analytic is looking for files being uploaded or downloaded using bitsadmin.exe This technique is used by threat actors to download malware on the victim machine, export sensitive data from the breached network, or for lateral movement within a network. This means that the IP being used doesn't need to be external. 
If you get this alert analyze what is being done. you might have to do some pivoting in the logs to determine what other activity happened around the time of this alert. 

If Downloading:
- check what was downloaded and where from? 
- is there a file hash you can check? 
- is it known malicious file, IP, or URL on any of the OSINT tools/websites? 
- internal IP address doesn't mean harmless as this tool is often used for lateral movement within a network. 

If Uploading:
- Where is it uploading to (IP or URL)? is it known malicous? 
- how many files were uploaded? a large number of files could indicate malicious activity 
- what kind of files are being uploaded? is any of it sensitive files



