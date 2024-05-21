# Disabling Windows Recovery Environment (WinRE)
### EXECUTIVE SUMMARY
Windows Recovery Environment (WinRE) is a recovery environment that can repair common causes of unbootable operating systems. WinRE comes with Automatic Repair and System Image Recovery tools as well as other troubleshooting and diagnostic tools. By default, WinRE is preloaded into Windows 10, Windows 11, Windows Server 2016, and later installations. By disabling WinRE a threat actor can prevent you from having access to the repair and recovery features that might allow you to circumvent their malicious actions. Many ransomware families will disable this mode to make recovery harder. Recovery mode is accessed when booting the system, this is disabled by editing the boot configuration settings using reagentc.exe or the bcdedit utility. This feature can commonly be seen in many families such as REvil, Clop, BlackCat, Phobos, WannaCry, and Cerber.

### HYPOTHESIS
Using known tactics, techniques, and procedures (TTPs) for threat actors disabling Windows Recovery Environment, we can locate and track the malicious activity allowing us to alert the needed team. 

## MITRE ATT&CK
### Tactics:
- Impact https://attack.mitre.org/tactics/TA0040/
- Defense Evasion https://attack.mitre.org/tactics/TA0005/

### Techniques:
- Inhibit System Recovery https://attack.mitre.org/techniques/T1490/
- Impair Defenses: Disable or Modify Tools https://attack.mitre.org/techniques/T1562/001/

## TECHNICAL SUMMARY
### OVERVIEW
Threat actors may delete, remove, or turn off built-in services designed to aid in the recovery of a corrupted system to prevent recovery. This may deny access to available backups and recovery options or augment the effects of Data Destruction and Data Encrypted for Impact.

### THREAT DESCRIPTION
The disabling of WinRe can be done via command line with either the bcdedit.exe or reagentc.exe tool. 

It can also be disabled via a registry edit to
```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager
```

### MITIGATION RECOMMENDATIONS
1. Consider implementing IT disaster recovery plans that include taking regular data backups and verifying data can be restored from those backups. Ensure backups are stored off system to prevent them from being deleted or corrupted by a threat actor on that system. Limit the user accounts that have access to backups to only those required. 
2. To check Windows Recovery Environment Status use the following command: reagentc /info
3. To ensure that WinRE is enabled using the following command: reagentc /enable

### Enable Windows Recovery Environment via Registry Editor:
1.	Open the Registry Editor 
2.	Navigate to: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager
3.	On the right side of the window, find and open the BootExecute string value. 
4.	Enter the text “autocheck autochk *” under the Value data field 
5.	Click OK

### References:
1.	https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-recovery-environment--windows-re--technical-reference?view=windows-10 
2.	https://hatching.io/blog/ransomware-part1/ 
3.	https://keys.direct/blogs/blog/how-to-stop-automatic-repair-windows-10 
4.	https://www.windowscentral.com/how-disable-automatic-repair-windows-10 
5.	https://www.group-ib.com/blog/bablock-ransomware/ 
6.	https://www.partitionwizard.com/news/enable-or-disable-windows-recovey-environment.html 
7.	https://appuals.com/disable-or-enable-recovery-environment/

# KQL:
```kql
// threat huhnt for Disabling WinRe
let DisableWinRe = @'(?i)(.*)(((bcdedit.*\/set.*recoveryenabled no)|(reagentc.*\/disable))|(REG DELETE(.*)HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager(.*)\/v(.*)BootExecute))(.*)'
; 
let SEvent = SecurityEvent
| where CommandLine matches regex DisableWinRe
;
let DEvent = DeviceEvents
| where InitiatingProcessCommandLine matches regex DisableWinRe or ProcessCommandLine matches regex DisableWinRe 
;
let DPEvent = DeviceProcessEvents
| where InitiatingProcessCommandLine matches regex DisableWinRe or ProcessCommandLine matches regex DisableWinRe 
;
let DFEvent = DeviceFileEvents
| where InitiatingProcessCommandLine matches regex DisableWinRe 
;
let DREvent = DeviceRegistryEvents
| where InitiatingProcessCommandLine matches regex DisableWinRe 
;
let SLog = Syslog
| where SyslogMessage matches regex DisableWinRe
; 
SEvent
| join kind=fullouter (SLog) on TimeGenerated
| join kind=fullouter (DPEvent) on TimeGenerated
| join kind=fullouter (DFEvent) on TimeGenerated
| join kind=fullouter (DREvent) on TimeGenerated
| join kind=fullouter (DEvent) on TimeGenerated
| extend InitiatingProcessCommandLine = coalesce(InitiatingProcessCommandLine, InitiatingProcessCommandLine1, InitiatingProcessCommandLine2, InitiatingProcessCommandLine3)
| extend ProcessCommandLine = coalesce(ProcessCommandLine, ProcessCommandLine1)
| extend TimeGenerated = coalesce(TimeGenerated, TimeGenerated1, TimeGenerated2, TimeGenerated3, TimeGenerated4, TimeGenerated5)
| extend DeviceName = coalesce(DeviceName, DeviceName1, DeviceName2, DeviceName3, Computer, Computer1)
| extend AccountName = coalesce(AccountName, AccountName1, AccountName2)
| extend InitiatingProcessAccountName = coalesce(InitiatingProcessAccountName, InitiatingProcessAccountName1, InitiatingProcessAccountName2)
| extend InitiatingProcessAccountUpn = coalesce(InitiatingProcessAccountUpn, InitiatingProcessAccountUpn1, InitiatingProcessAccountUpn2)
```
