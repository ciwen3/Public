# Potential LOLBAS BYOL (Bring-Your-Own-Land)
### EXECUTIVE SUMMARY
Living Off the Land Binaries And Scripts (LOLBAS) have become an important set of tools for Advanced Persistent Threats (APTs) and other sophisticated hackers to use. This is because the tools are already in place, trusted, and have public shared knowledge on how to abuse those tools. An extension of this is Bring Your Own Land (BYOL), where the threat actor brings their own copy of the Microsoft approved and signed binary to hide malicious activity and bypass restrictions in place on the system.  The big indicator of this activity is that they exist in a place they are not expected to be. 

### Hypothesis
Using the data on https://lolbas-project.github.io/api/lolbas.csv we can craft queries to find malicious activity related to BYOL.  We will use these queries in Sentinels Log Analytics to hunt for possible malicious activity going back 90 days from the date on this document. If any possible malicious activity is found, we will follow up with an investigation.

## MITRE ATT&CK
There are no direct Bring Your Own Land Mitre Att&ck methods, but below are the kinds of activity it could be used for. 
    • Privilege Escalation
        ◦ Exploitation for Privilege Escalation
    • Defense Evasion
        ◦ Impair Defenses: Downgrade Attack

### Mitigation Recommendations
If Malicious activity is identified, an Incident Response Analyst should proceed to review the related activity and files to better understand the scope of what happened. For BYOL you would want to find out why the software is in an unexpected location and how it got there. You should also identify any commands that were run with the software in question. This can be done by searching the logs. 

### References 
    1. https://lolbas-project.github.io/api/lolbas.csv
    2. https://lolbas-project.github.io/
    3. https://attack.mitre.org/tactics/TA0004/
    4. https://attack.mitre.org/techniques/T1068/
    5. https://attack.mitre.org/tactics/TA0005/
    6. https://attack.mitre.org/techniques/T1562/010/


## Notes
Living Off the Land Binaries And Scripts are a type of activity that misuses tools and executables that are already there because they are part of the operating system. In this case, Certutil.exe is being run from the wrong location. This can be an indication of BYOL (Bringing Your Own Land), where a malicious actor installs approved binaries in unauthorized locations to bypass security protocols. This uses an updated list of LOLBAS from "https://lolbas-project.github.io/api/lolbas.csv" to determine if something that is known to be abused is running from the wrong location. 

### How to handle: 
ExpectedPaths are all the "known" paths that this program can be found. ProcessPath is where the program was actually found. check to see what the difference is between the two. If it seems really off then it might be a LOLBAS BYOL and requires further investigation or follow up with the client. An example of it being really off would be if it is expected in a programs folder but shows up in a users folder, downloads folder, or temp folder to name a few examples. 

### Note: If the only difference is a version number and the rest of the path is the same then it can be ignored. If the version issue comes up a lot, then please create an SR to have this tuned out or have LOLBAS repo updated with correct information. 

### Example of version number difference: 
ProcessPath = C:\Program Files (x86)\Microsoft\Edge\Application\117.0.2045.47\msedgewebview2.exe    
ProcessPath = C:\Program Files (x86)\Microsoft\Edge\Application\114.0.1823.43\msedgewebview2.exe

# KQL:
```kql
//Analytic query with some stuff being ignored that will cause lots of false positives. 
let binaries = externaldata(filename:string, description:string, author:string, loldate:datetime , command:string, commanddesc:string, commanduse:string, commandcat:string, commandprivs:string, mitre:string, os:string, paths:string, detections:string, resources:string, acknowledge:string, url:string)[@"https://lolbas-project.github.io/api/lolbas.csv"] with (format="csv", ignoreFirstRecord=true)
;
let lolbinexe = binaries
| summarize arg_max(filename, *) by filename // remove duplicates
| where filename !in ("Teams.exe", "AgentExecutor.exe", "MpCmdRun.exe") // teams should start with localappdata but it wasnt done to the same standard as all the other entries so far, AgentExecutor.exe doesn't have the app listed in the path. MpCmdRun.exe has bad path information in lolbas. 
| extend ParentProcess = filename
| extend NewProcess = filename
| where paths !startswith "%localappdata%" //localappdata will be a different file location on every system
| where paths !in ("No fixed path", "no default", "N/A") //dont look at things that have no known or set file location
| project ParentProcess, NewProcess, paths
;
let SEvent = SecurityEvent
| where ParentProcessName != ""
| extend NPN = split(NewProcessName, "\\")
| extend NewProcess = tostring(NPN.[-1])
| extend PPN = split(ParentProcessName, "\\")
| extend ParentProcess = tostring(PPN.[-1])
;
let Parent = lolbinexe
| join SEvent on ParentProcess
| where paths !contains ParentProcessName
| distinct ParentProcessName, paths, Account, Computer, Type
;
let Child = lolbinexe
| join SEvent on NewProcess
| where paths !contains NewProcessName
| distinct NewProcessName, paths, Account, Computer, Type
;
union Parent, Child
// If we need to whitelist files or folders. usually due to version numbers. 
//| where ParentProcessName !contains "C:\\ProgramData\\Microsoft\\Windows Defender\\platform\\" and ParentProcessName !contains "C:\\Program Files (x86)\\Microsoft\\EdgeWebView\\Application\\" 
//| where NewProcessName !contains "C:\\ProgramData\\Microsoft\\Windows Defender\\platform\\" and NewProcessName !contains "C:\\Program Files (x86)\\Microsoft\\EdgeWebView\\Application\\"
| extend ProcessPath = coalesce(ParentProcessName, NewProcessName)
| extend ExpectedPaths = paths
| where ProcessPath !contains "C:\\ProgramData\\Microsoft\\Windows Defender\\platform\\" and ProcessPath !contains "C:\\Program Files (x86)\\Microsoft\\EdgeWebView\\Application\\" and ProcessPath !contains "C:\\Windows\\Microsoft.NET\\Framework\\" and ProcessPath !contains "C:\\Program Files (x86)\\Microsoft Silverlight\\"
| project-away ParentProcessName, NewProcessName, paths
```
