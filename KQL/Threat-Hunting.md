## lots of examples:
1. https://github.com/jangeisbauer/AdvancedHunting
2. https://github.com/ashwin-patil/blue-teaming-with-kql
3. https://github.com/Cyb3r-Monk/Threat-Hunting-and-Detection


## threat hunting 
https://twitter.com/rpargman/status/1406017062359560193
```
SecurityEvent
| where EventID in (4720, 4741, 4742, 4722, 4724, 4728, 4732, 4799)
| project TimeGenerated, EventID, Activity, CallerProcessName, EventData
| extend EventDetail = parse_xml(EventData)["EventData"]["Data"]
```











## PrintNightmare KQL
https://gist.github.com/olafhartong/af523adcd7df7706bae527af8fee1700

```
let serverlist=DeviceInfo
| where DeviceType != "Workstation"
| distinct DeviceId;
let suspiciousdrivers=DeviceImageLoadEvents
| where DeviceId in (serverlist)
| where FolderPath startswith @"c:\windows\system32\spool\drivers"
| distinct SHA1
| invoke FileProfile(SHA1, 1000) 
| where GlobalPrevalence < 50 and IsRootSignerMicrosoft != 1 and SignatureState != "SignedValid";
suspiciousdrivers
| join kind=inner (DeviceImageLoadEvents
| where DeviceId in (serverlist)
| where FolderPath startswith @"c:\windows\system32\spool\drivers") on SHA1
| where InitiatingProcessFileName != "ccmexec.exe"
// Optionally filter for only the print spooler to load the driver to make it specific to this attack
//| where InitiatingProcessFileName == "spoolsv.exe"
```

## Defender Exclusions modification
https://gist.github.com/alexverboon/f2f52279a8a38583bca0589fdf88f9d9
```
// T1562.001 - Impair Defenses: Disable or Modify Tools
DeviceRegistryEvents 
| where ActionType == "RegistryValueSet"
| where RegistryKey startswith 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows Defender\\Exclusions' 


// T1562.001 - Impair Defenses: Disable or Modify Tools - Defender Alerts
AlertInfo
| where Title == "Suspicious Microsoft Defender Antivirus exclusion"
| join  AlertEvidence on $left. AlertId ==  $right.AlertId
| project-reorder Timestamp, AlertId, DetectionSource, EntityType, EvidenceRole, FileName, FolderPath, RegistryKey, RegistryValueName, RegistryValueData
Category
```
you can add this to include ASC Exlusions"
```
| where RegistryKey startswith ("HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Exclusions") or RegistryKey startswith ("HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Windows Defender Exploit Guard\ASR\ASROnlyExclusions")
```

## MDE KQL to identify apps from Edge WDAC policy
https://gist.github.com/nathanmcnulty/90bef7f5f2f7416fde2d0facdb1dfca4#file-edgewdac-mdekql-txt

```
DeviceProcessEvents
| where FileName in ("AT.EXE","bash.exe","BitLockerWizard.exe","BitLockerWizardElev.exe","Bubbles","calc.exe","CDB.Exe","CertUtil.exe","charmap.exe","CLEANMGR.DLL","ClientConsole.EXE","Cmd.Exe","CMDL32.EXE","colorcpl.exe","ComputerDefaults.EXE","CONTROL.EXE","Credwiz.exe","CryptExt.dll","Csc.Exe","cscript.exe","csi.Exe","dccw.exe","DeviceEject.EXE","DeviceParing.exe","DeviceParing.exe","DeviceProperties.exe","dfshim.dll","DIALER.EXE","DISKPERF.EXE","dnx.Exe","DOSKEY.EXE","dsquery.dll","dvdplay","eventvwr.exe","expand","FC.EXE","FIND.EXE","FINDSTR.EXE","finger.exe","FONTVIEW.EXE","forfiles.exe","format.com","fsi.exe","FXSSVC.EXE","gprslt.exe","GPSCRIPT.EXE","GPUpdate.exe","Help.Exe","HH.exe","HWRREG.EXE","iexplore.exe","infdefaultinstall.exe","irftp.exe","iscsicli.exe","iscsicpl.exe","ISOBURN.EXE","Journal.exe","kd.Exe","LaunchTM.exe","lxrun.exe","lxssmanager.dll","lxssmanager.exe","manage-bde.exe","mip.exe","mmc.exe","mobsync.exe","MORE.COM","MSBuild.Exe","msconfig.EXE","msdt.exe","mshta.exe","msiexec.exe","mspaint.exe","msra.exe","MSRATING.DLL","mstsc.exe","Mystify","nbtinfo.exe","NETPLWIZ.EXE","netstat.exe","nslookup.exe","ntprint.exe","ntsd.Exe","odbcad32.exe","odbcconf.exe","OneDriveSetup.exe","OpenWith.exe","OptionalFeatures.EXE","pcalua.exe","pcaui.exe","pcwrun.exe","phoneactivate.exe","PhotoScreensaver.scr.mui","PhotoViewer.dll","ping.exe","PnPutil.exe","PowerCfg.exe","powershell.exe","powershellcustomhost.exe","powershell_ise.exe","PresentationHost.exe","Print.Exe","PrintBrmUi.exe","printui.exe","proquota.exe","psr.exe","Pwcreator.exe","Pwlauncher.exe","qappsrv.exe","qprocess.exe","query.exe","QuickAssist.exe","quser.exe","qwinsta.exe","RASDIAL.EXE","rasdlui.exe","raserver.exe","rasphone.exe","rcsi.Exe","regedit.exe","regedt32.exe","regini.exe","REPLACE.EXE","reset.exe","resmon.exe","Ribbons","robocopy.exe","route.exe","RpcPing.exe","rrinstaller.exe","RUNAS.EXE","RunLegacyCPLElevated.EXE","RUNONCE.EXE","runscripthelper.exe","samlock.exe","schtasks.exe","ScriptRunner.exe","scrnsave","sdbinst.exe","sdchange.exe","sdclt.exe","SessionMsg.exe","SetupPrep.exe","shrpubw.exe","SndVol.exe","SnippingTool.exe","SpaceAgent.exe","SSystemPropertiesProtection.EXE","StikyNot.exe","SystemPropertiesAdvanced.EXE","SystemPropertiesComputerName.EXE","SystemPropertiesDataExecutionPrevention.EXE","SystemPropertiesHardware.EXE","SystemPropertiesPerformance.EXE","SystemPropertiesRemote.EXE","Taskmgr.exe","TCMSETUP.EXE","Text3D","unregmp2.exe","WAB.EXE","wbemtest.exe","WIAACMGR.EXE","windbg.Exe","WINHLP32.EXE","WinSAT.exe","wksprt.exe","WmiApSrv.exe","wmic.exe","wmicookr.dll","wmplayer.exe","WorkFolders.exe","WpcMon.exe","write","wscript.exe","wsl.exe","wslconfig.exe","wslhost.exe","XCOPY.EXE","xpsrchvw.exe")
| summarize  count() by FileName
| sort by count_
```

## BazaCall 
https://www.microsoft.com/security/blog/2021/07/29/bazacall-phony-call-centers-lead-to-exfiltration-and-ransomware/
https://aka.ms/BazaCall

### To look for malicious emails matching the patterns of the BazaCall campaign, run this query.
```
EmailEvents
| where Subject matches regex @"[A-Z]{1,3}\d{9,15}"
and Subject has_any('trial', 'free', 'demo', 'membership', 'premium', 'gold',
'notification', 'notice', 'claim', 'order', 'license', 'licenses')
```
### BazaCall Excel file delivery

To look for signs of web file delivery behavior matching the patterns of the BazaCall campaign, run this query.
```
DeviceFileEvents
| where FileOriginUrl has "/cancel.php" and FileOriginReferrerUrl has "/account"
or FileOriginUrl has "/download.php" and FileOriginReferrerUrl has "/case"
```
### BazaCall Excel file execution

To surface the execution of malicious Excel files associated with BazaCall, run this query.
```
DeviceProcessEvents
| where InitiatingProcessFileName =~ "excel.exe"
and ProcessCommandLine has_all('mkdir', '&& copy', 'certutil.exe')
```
### BazaCall Excel file download domain pattern

To look for malicious Excel files downloaded from .XYZ domains, run this query.
```
DeviceNetworkEvents
| where RemoteUrl matches regex @".{14}\.xyz/config\.php"
```
### BazaCall dropping payload via certutil

To look for the copy of certutil.exe that was used to download the BazaLoader payload, run this query.
```
DeviceFileEvents
| where InitiatingProcessFileName !~ "certutil.exe"
| where InitiatingProcessFileName !~ "cmd.exe"
| where InitiatingProcessCommandLine has_all("-urlcache", "split", "http")
```
### NTDS theft

To look for theft of Active Directory in paths used by this threat, run this query.
```
DeviceProcessEvents
| where FileName =~ "ntdsutil.exe"
| where ProcessCommandLine has_any("full", "fu")
| where ProcessCommandLine has_any ("temp", "perflogs", "programdata")
// Exclusion
| where ProcessCommandLine !contains @"Backup"
```
### Renamed Rclone data exfiltration

To look for data exfiltration using renamed Rclone, run this query.
```
DeviceProcessEvents
| where ProcessVersionInfoProductName has "rclone" and not(FileName has "rclone")
```
### RunDLL Suspicious Network Connections

To look for RunDLL making suspicious network connections, run this query.
```
DeviceNetworkEvents
| where InitiatingProcessFileName =~ 'rundll32.exe' and InitiatingProcessCommandLine has ",GlobalOut"
```



## Hunting for Phishing Links Using Sysmon and KQL
https://posts.bluraven.io/hunting-for-phishing-links-using-sysmon-and-kql-e87d1118ce5e

### get the events of URL clicks:
```
let lookback = 3d;
Event
| where TimeGenerated > ago(3d)
| where Source == "Microsoft-Windows-Sysmon" and EventID == 1
// Get only the relevant events to improve the query performance during parsing
| where RenderedDescription has_any ("http://", "https://")
| where RenderedDescription has_any ("msedge.exe", "chrome.exe", "firefox.exe")
```

### extract the URLs from the process command line:
```
// Extract URL and URLHost 
| extend URL = extract("((http|https):\\/\\/.*)\\s?",1,tostring(CommandLine))
| extend URLHost = tostring(parse_url(URL).Host)
```

### perform frequency analysis based on the URL, or URLHost information:
```
PotentialPhishingLinks // parsed sysmon events
| summarize dcount(Computer) by URL, ParentImage
| where dcount_Computer <= 5
//// Get event details back. ////
| join kind=inner PotentialPhishingLinks on URL // URLHost
// Filter only the last 1 day of events (if you perform analysis everyday)
| where TimeGenerated > ago(1d)
| project-reorder TimeGenerated, dcount_Computer, Computer, ParentImage, OriginalFileName , URL, CommandLine
```



## Password in FTP Command Line
https://twitter.com/16yashpatel/status/1403779222225653760/photo/1
```
DeviceNetworkEvents
| where RemotePort == 21
| where InitiatingProcessCommandLine contains "@ftp"
```

## detect if WD Real Time Protection is Off on Windows 10 
https://twitter.com/SecGuru_OTX/status/1401941560917381121/photo/1
```
DeviceTvmSecureConfigurationAssessment
| where ConfigurationId == 'scid-2012' and OSPlatform contains "Windows10"
| extend IsRealTimeProtection-iif(ConfigurationId == "scid-2012" and IsCompliant==1, 1, 0)
| summarize DeviceName=any(DeviceName), RealTimeProtectionEnabled=iif(max(IsRealTimeProtection) == 1, "On", "Off") by DeviceId
| where RealTimeProtectionEnabled == "Off"
```














