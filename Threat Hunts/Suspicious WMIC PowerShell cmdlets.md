# Suspicious WMIC PowerShell cmdlets
This analytic will look for Potential WMIC Abuse. Windows Management Instrumentation Command retrieves a huge range of information about local or remote computers. It makes configuration changes to multiple remote machines. The WMIC is a deprecated tool as of 2021. While it is unlikely to stop working for a few years, no new features will be added and it may eventually be removed. WMIC is a Feature on Demand (FoD) that's preinstalled by default in Windows 11. 

- For decoding a command see: https://gchq.github.io/CyberChef/
- For better understanding of the WMIC command see: https://ss64.com/nt/wmic.html

### Things of Note: 
    - /NODE: which is used to connect to remote devices. this can show up in any of the scenarios. 
    - /FORMAT: Executes JScript or VBScript embedded in the target remote XSL stylesheet.

There are numerous default PowerShell cmdlets that allow administrators to leverage WMI via PowerShell. Both adversaries and administrators use these cmdlets to query the operating system or execute commands, either locally or remotely. Cmdlets like Get-WMIObject are often used for reconnaissance. It may require tuning to prevent high volumes of false positives.

This query looks for Powershell to run 'invoke-wmimethod', 'invoke-cimmethod', 'get-wmiobject', 'get-ciminstance', or 'wmiclass'. This requires understanding the command. using co pilot might help to get a summary of what the command is doing. 

### Red Flags: 
1. reaching out to the internet 
    - can ignore internal IP address or loopback IP (127.0.0.1)
2. obfuscated code (base64, rot13, etc) https://gchq.github.io/CyberChef/
3. any kind of encryption taking place on the device

# KQL: 
```kql
//Suspicious PowerShell cmdlets
let psList = dynamic(['invoke-wmimethod', 'invoke-cimmethod', 'get-wmiobject', 'get-ciminstance', 'wmiclass'])
;
let DEvents = DeviceEvents
| where InitiatingProcessFileName contains "powershell" and ProcessCommandLine has_any (psList)
;
let DPEvents = DeviceProcessEvents
| where InitiatingProcessFileName contains "powershell" and ProcessCommandLine has_any (psList)
;
DEvents
| join kind=fullouter (DPEvents) on TimeGenerated
| extend InitiatingProcessCommandLine = coalesce(InitiatingProcessCommandLine, InitiatingProcessCommandLine1)
| extend ProcessCommandLine = coalesce(ProcessCommandLine, ProcessCommandLine1)
| extend TimeGenerated = coalesce(TimeGenerated, TimeGenerated1)
| extend DeviceName = coalesce(DeviceName, DeviceName1)
| extend AccountName = coalesce(AccountName, AccountName1)
| extend InitiatingProcessAccountName = coalesce(InitiatingProcessAccountName, InitiatingProcessAccountName1)
| extend InitiatingProcessAccountUpn = coalesce(InitiatingProcessAccountUpn, InitiatingProcessAccountUpn1)
```
