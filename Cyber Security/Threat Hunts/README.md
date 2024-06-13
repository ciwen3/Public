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
2. https://www.eicar.org/download-anti-malware-testfile/
3. https://ss64.com/
4. https://www.reliaquest.com/blog/double-extortion-attack-analysis/
5. https://www.cyborgsecurity.com/blog/50-threat-hunting-hypothesis-examples/
6. https://attack.mitre.org/tactics/enterprise/
7. https://attack.mitre.org/techniques/enterprise/
8. https://research.splunk.com/detections/#endpoint
9. https://hijacklibs.net/
10. https://www.wicar.org/
11. https://www.kqlsearch.com/
12. https://github.com/infosecB/LOOBins
13. https://www.loobins.io/
14. https://gtfobins.github.io/
15. https://lolbas-project.github.io/
16. https://redcanary.com/threat-detection-report/
17. https://wtfbins.wtf/
18. https://research.splunk.com/stories/living_off_the_land/
19. https://research.splunk.com/stories/



