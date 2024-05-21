# Threat Hunt Process:
### Step 1: Do information gathering 
- read reports and look up information on line to determine what threat hunt to do

### Step 2: Create base documentation
- create Advisory explaining why we chose this as a threat hunt target
- create KB for analysts to follow highlighting what to look for and how to handle things

### Step 3: Create Hunt
- create KQL
- make sure it is not to agressive or not aggressive enough
- usually starts off very generic using searches to discover the proper log files
- refine until you are targetting just the threats

### Step 4: Do hunt and refine Query as you work 
- start hunting in every environment
- refine kql based on what you discover
- refine documentation based on what you discover

### Step 5: Create SRs and SIRs
- create SIRs for any suspicious activity found
- create an SR for ever client that the threat hunt was done in

### Step 6: Create analytic and SR to push analytic
- create analytic in operations environment
- create SR for engineering to validate and push the analytic to all workspaces

### Step 7: Update Threat Hunt Tracker
- update all tracking documentation 



References: 
1. https://arno0x0x.wordpress.com/2017/11/20/windows-oneliners-to-download-remote-payload-and-execute-arbitrary-code/
2. https://ss64.com/
3. https://www.reliaquest.com/blog/double-extortion-attack-analysis/
4. https://www.cyborgsecurity.com/blog/50-threat-hunting-hypothesis-examples/
5. https://attack.mitre.org/tactics/enterprise/
6. https://attack.mitre.org/techniques/enterprise/
7. https://research.splunk.com/detections/#endpoint
8. https://hijacklibs.net/
9. https://www.wicar.org/
10. https://www.kqlsearch.com/
11. https://github.com/infosecB/LOOBins
12. https://www.loobins.io/
13. https://gtfobins.github.io/
14. https://lolbas-project.github.io/
15. https://redcanary.com/threat-detection-report/



