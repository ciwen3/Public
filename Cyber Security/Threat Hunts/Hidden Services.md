# Hidden Services
Microsoft Windows Services is a feature built into Windows that enables users to create processes and run executable applications in independent sessions. The intent is to specify services that can automatically launch, persist through machine reboots, run independently of user accounts, and do not require a user's interaction or knowledge of the service. Threat actors target Windows Services for its access and persistence on victims' machines. Threat actors can exploit a compromised host by utilizing and concealing Windows Services to install malware, establish a reverse shell to a C2, and execute commands. While many legitimate processes operate through Windows Services, any hidden processes should be thoroughly examined and investigated for potential malicious activity. Antivirus scans and security patches may not mitigate hidden Windows Service compromises. Detecting and investigating hidden services that could allow the threat actor to regain access once the service restarts upon the next boot is critical.

The objective of this threat hunt is to uncover and audit the legitimacy of hidden services that could allow unauthorized access in the environment that has not been detected.

### References:
1.	https://www.sans.org/blog/red-team-tactics-hiding-windows-services/ 
2.	https://medium.com/@mahdihatami.k/attack-and-hunting-lateral-movement-with-service-control-manager-svcctl-6424d3d41a0a 
3.	https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1569.002/T1569.002.md 
4.	https://www.ired.team/offensive-security/persistence/t1035-service-execution 
5.	https://pentestlab.blog/2023/03/20/persistence-service-control-manager/ 
6.	https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/ 
7.	https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/convertfrom-sddlstring?view=powershell-7.4 
8.	https://nettools.net/sddl-viewer/ 
9.	https://itconnect.uw.edu/tools-services-support/it-systems-infrastructure/msinf/other-help/understanding-sddl-syntax/

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
