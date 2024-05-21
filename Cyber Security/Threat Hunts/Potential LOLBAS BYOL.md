# Potential LOLBAS BYOL (Bring-Your-Own-Land)
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
