# SentinelOne Up? Check
For Analysts to check and make sure N-Able is up and functioning in case we don't see any logs coming in. 
- https://uptime.n-able.com/

List of IPs we can ping or check to see if N-Able Services are reachable by us. 
- https://usea1-swprd5.sentinelone.net/docs/en/services-and-ports.html#services-and-ports

# SentinelOne Analytic Rules: 
https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/SentinelOne/Analytic%20Rules

# SentinelOne Workbook:
https://github.com/Azure/Azure-Sentinel/blob/master/Solutions/SentinelOne/Workbooks/SentinelOne.json

# SentinelOne Threat Hunting:
https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/SentinelOne/Hunting%20Queries

# SentinelOne Connector:
Used the SentinelOne Connector Built into Azure Sentinel. 

# SentinelOne Function:
https://raw.githubusercontent.com/Azure/Azure-Sentinel/master/Parsers/SentinelOne/SentinelOne.txt
- Added in: ConfidenceLevel=column_ifexists('data_confidenceLevel_s', ''), to easily search for Malicious and Suspicious activity. 
- Added in: ThreatClassification=column_ifexists('data_threatClassification_s', ''),

```
// Usage Instruction : 
// Paste below query in log analytics, click on Save button and select as Function from drop down by specifying function name and alias (e.g. SentinelOne).
// Function usually takes 10-15 minutes to activate. You can then use function alias from any other queries (e.g. SentinelOne | take 10).
// References : 
// Using functions in Azure monitor log queries : https://docs.microsoft.com/azure/azure-monitor/log-query/functions
// Tech Community Blog on KQL Functions : https://techcommunity.microsoft.com/t5/Azure-Sentinel/Using-KQL-functions-to-speed-up-analysis-in-Azure-Sentinel/ba-p/712381
//
let SentinelOne_view  = view () { 
    SentinelOne_CL
    | extend 
                EventVendor="SentinelOne",
                EventProduct="SentinelOne",
                ConfidenceLevel=column_ifexists('data_confidenceLevel_s', ''),
                ThreatClassification=column_ifexists('data_threatClassification_s', ''),
                AccountId=column_ifexists('accountId_s', ''),
                AccountName=column_ifexists('accountName_s', ''),
                ActivityType=column_ifexists('activityType_d', ''),
                EventCreationTime=column_ifexists('createdAt_t', ''),
                DataAccountName=column_ifexists('data_accountName_s', ''),
                DataFullScopeDetails=column_ifexists('data_fullScopeDetails_s', ''),
                DataScopeLevel=column_ifexists('data_scopeLevel_s', ''),
                DataScopeName=column_ifexists('data_scopeName_s', ''),
                DataSiteId=column_ifexists('data_siteId_d', ''),
                DataSiteName=column_ifexists('data_siteName_s', ''),
                SrcUserName=column_ifexists('data_username_s', ''),
                EventId=column_ifexists('id_s', ''),
                EventOriginalMessage=column_ifexists('primaryDescription_s', ''),
                SiteId=column_ifexists('siteId_s', ''),
                SiteName=column_ifexists('siteName_s', ''),
                UpdatedAt=column_ifexists('updatedAt_t', ''),
                UserIdentity=column_ifexists('userId_s', ''),
                EventType=column_ifexists('event_name_s', ''),
                DataByUser=column_ifexists('data_byUser_s', ''),
                DataRole=column_ifexists('data_role_s', ''),
                DataUserScope=column_ifexists('data_userScope_s', ''),
                EventTypeDetailed=column_ifexists('description_s', ''),
                DataSource=column_ifexists('data_source_s', ''),
                DataExpiryDateStr=column_ifexists('data_expiryDateStr_s', ''),
                DataExpiryTime=column_ifexists('data_expiryTime_d', ''),
                DataNetworkquarantine=column_ifexists('data_networkquarantine_b', ''),
                DataRuleCreationTime=column_ifexists('data_ruleCreationTime_d', ''),
                DataRuleDescription=column_ifexists('data_ruleDescription_s', ''),
                DataRuleExpirationMode=column_ifexists('data_ruleExpirationMode_s', ''),
                DataRuleId=column_ifexists('data_ruleId_d', ''),
                DataRuleName=column_ifexists('data_ruleName_s', ''),
                DataRuleQueryDetails=column_ifexists('data_ruleQueryDetails_s', ''),
                DataRuleQueryType=column_ifexists('data_ruleQueryType_s', ''),
                DataRuleSeverity=column_ifexists('data_ruleSeverity_s', ''),
                DataScopeId=column_ifexists('data_scopeId_d', ''),
                DataStatus=column_ifexists('data_status_s', ''),
                DataSystemUser=column_ifexists('data_systemUser_d', ''),
                DataTreatasthreat=column_ifexists('data_treatasthreat_s', ''),
                DataUserId=column_ifexists('data_userId_d', ''),
                DataUserName=column_ifexists('data_userName_s', ''),
                EventSubStatus=column_ifexists('secondaryDescription_s', ''),
                AgentId=column_ifexists('agentId_s', ''),
                DataComputerName=column_ifexists('data_computerName_s', ''),
                DataExternalIp=column_ifexists('data_externalIp_s', ''),
                DataGroupName=column_ifexists('data_groupName_s', ''),
                DataSystem=column_ifexists('data_system_b', ''),
                DataUuid=column_ifexists('data_uuid_g', ''),
                GroupId=column_ifexists('groupId_s', ''),
                GroupName=column_ifexists('groupName_s', ''),
                DataGroup=column_ifexists('data_group_s', ''),
                DataOptionalGroups=column_ifexists('data_optionalGroups_s', ''),
                DataCreatedAt=column_ifexists('data_createdAt_t', ''),
                DataDownloadUrl=column_ifexists('data_downloadUrl_s', ''),
                DataFilePath=column_ifexists('data_filePath_s', ''),
                DataFilename=column_ifexists('data_filename_s', ''),
                DataUploadedFilename=column_ifexists('data_uploadedFilename_s', ''),
                Comments=column_ifexists('comments_s', ''),
                DataNewValue=column_ifexists('data_newValue_s', ''),
                DataPolicyId=column_ifexists('data_policy_id_s', ''),
                DataPolicyName=column_ifexists('data_policyName_s', ''),
                DataNewValueb=column_ifexists('data_newValue_b', ''),
                DataShouldReboot=column_ifexists('data_shouldReboot_b', ''),
                DataRoleName=column_ifexists('data_roleName_s', ''),
                DataScopeLevelName=column_ifexists('data_scopeLevelName_s', ''),
                ActiveDirectoryComputerDistinguishedName=column_ifexists('activeDirectory_computerDistinguishedName_s', ''),
                ActiveDirectoryComputerMemberOf=column_ifexists('activeDirectory_computerMemberOf_s', ''),
                ActiveDirectoryLastUserDistinguishedName=column_ifexists('activeDirectory_lastUserDistinguishedName_s', ''),
                ActiveDirectoryLastUserMemberOf=column_ifexists('activeDirectory_lastUserMemberOf_s', ''),
                ActiveThreats=column_ifexists('activeThreats_d', ''),
                AgentVersion=column_ifexists('agentVersion_s', ''),
                AllowRemoteShell=column_ifexists('allowRemoteShell_b', ''),
                AppsVulnerabilityStatus=column_ifexists('appsVulnerabilityStatus_s', ''),
                ComputerName=column_ifexists('computerName_s', ''),
                ConsoleMigrationStatus=column_ifexists('consoleMigrationStatus_s', ''),
                CoreCount=column_ifexists('coreCount_d', ''),
                CpuCount=column_ifexists('cpuCount_d', ''),
                CpuId=column_ifexists('cpuId_s', ''),
                SrcDvcDomain=column_ifexists('domain_s', ''),
                EncryptedApplications=column_ifexists('encryptedApplications_b', ''),
                ExternalId=column_ifexists('externalId_s', ''),
                ExternalIp=column_ifexists('externalIp_s', ''),
                FirewallEnabled=column_ifexists('firewallEnabled_b', ''),
                GroupIp=column_ifexists('groupIp_s', ''),
                InRemoteShellSession=column_ifexists('inRemoteShellSession_b', ''),
                Infected=column_ifexists('infected_b', ''),
                InstallerType=column_ifexists('installerType_s', ''),
                IsActive=column_ifexists('isActive_b', ''),
                IsDecommissioned=column_ifexists('isDecommissioned_b', ''),
                IsPendingUninstall=column_ifexists('isPendingUninstall_b', ''),
                IsUninstalled=column_ifexists('isUninstalled_b', ''),
                IsUpToDate=column_ifexists('isUpToDate_b', ''),
                LastActiveDate=column_ifexists('lastActiveDate_t', ''),
                LastIpToMgmt=column_ifexists('lastIpToMgmt_s', ''),
                LastLoggedInUserName=column_ifexists('lastLoggedInUserName_s', ''),
                LicenseKey=column_ifexists('licenseKey_s', ''),
                LocationEnabled=column_ifexists('locationEnabled_b', ''),
                LocationType=column_ifexists('locationType_s', ''),
                Locations=column_ifexists('locations_s', ''),
                MachineType=column_ifexists('machineType_s', ''),
                MitigationMode=column_ifexists('mitigationMode_s', ''),
                MitigationModeSuspicious=column_ifexists('mitigationModeSuspicious_s', ''),
                SrcDvcModelName=column_ifexists('modelName_s', ''),
                NetworkInterfaces=column_ifexists('networkInterfaces_s', ''),
                NetworkQuarantineEnabled=column_ifexists('networkQuarantineEnabled_b', ''),
                NetworkStatus=column_ifexists('networkStatus_s', ''),
                OperationalState=column_ifexists('operationalState_s', ''),
                OsArch=column_ifexists('osArch_s', ''),
                SrcDvcOs=column_ifexists('osName_s', ''),
                OsRevision=column_ifexists('osRevision_s', ''),
                OsStartTime=column_ifexists('osStartTime_t', ''),
                OsType=column_ifexists('osType_s', ''),
                RangerStatus=column_ifexists('rangerStatus_s', ''),
                RangerVersion=column_ifexists('rangerVersion_s', ''),
                RegisteredAt=column_ifexists('registeredAt_t', ''),
                RemoteProfilingState=column_ifexists('remoteProfilingState_s', ''),
                ScanFinishedAt=column_ifexists('scanFinishedAt_t', ''),
                ScanStartedAt=column_ifexists('scanStartedAt_t', ''),
                ScanStatus=column_ifexists('scanStatus_s', ''),
                ThreatRebootRequired=column_ifexists('threatRebootRequired_b', ''),
                TotalMemory=column_ifexists('totalMemory_d', ''),
                UserActionsNeeded=column_ifexists('userActionsNeeded_s', ''),
                Uuid=column_ifexists('uuid_g', ''),
                Creator=column_ifexists('creator_s', ''),
                CreatorId=column_ifexists('creatorId_s', ''),
                Inherits=column_ifexists('inherits_b', ''),
                IsDefault=column_ifexists('isDefault_b', ''),
                Name=column_ifexists('name_s', ''),
                RegistrationToken=column_ifexists('registrationToken_s', ''),
                TotalAgents=column_ifexists('totalAgents_d', ''),
                Type=column_ifexists('type_s', '')
    | project
                TimeGenerated, 
                ConfidenceLevel,
		ThreatClassification,
                EventVendor,
                EventProduct,
                AccountName,
                ActivityType,
                EventCreationTime,
                DataAccountName,
                DataFullScopeDetails,
                DataScopeLevel,
                DataScopeName,
                DataSiteId,
                DataSiteName,
                SrcUserName,
                EventId,
                EventOriginalMessage,
                SiteId,
                SiteName,
                UpdatedAt,
                UserIdentity,
                EventType,
                DataByUser,
                DataRole,
                DataUserScope,
                EventTypeDetailed,
                DataSource,
                DataExpiryDateStr,
                DataExpiryTime,
                DataNetworkquarantine,
                DataRuleCreationTime,
                DataRuleDescription,
                DataRuleExpirationMode,
                DataRuleId,
                DataRuleName,
                DataRuleQueryDetails,
                DataRuleQueryType,
                DataRuleSeverity,
                DataScopeId,
                DataStatus,
                DataSystemUser,
                DataTreatasthreat,
                DataUserId,
                DataUserName,
                EventSubStatus,
                AgentId,
                DataComputerName,
                DataExternalIp,
                DataGroupName,
                DataSystem,
                DataUuid,
                GroupId,
                GroupName,
                DataGroup,
                DataOptionalGroups,
                DataCreatedAt,
                DataDownloadUrl,
                DataFilePath,
                DataFilename,
                DataUploadedFilename,
                Comments,
                DataNewValue,
                DataPolicyId,
                DataPolicyName,
                DataNewValueb,
                DataShouldReboot,
                DataRoleName,
                DataScopeLevelName,
                ActiveDirectoryComputerDistinguishedName,
                ActiveDirectoryComputerMemberOf,
                ActiveDirectoryLastUserDistinguishedName,
                ActiveDirectoryLastUserMemberOf,
                ActiveThreats,
                AgentVersion,
                AllowRemoteShell,
                AppsVulnerabilityStatus,
                ComputerName,
                ConsoleMigrationStatus,
                CoreCount,
                CpuCount,
                CpuId,
                SrcDvcDomain,
                EncryptedApplications,
                ExternalId,
                ExternalIp,
                FirewallEnabled,
                GroupIp,
                InRemoteShellSession,
                Infected,
                InstallerType,
                IsActive,
                IsDecommissioned,
                IsPendingUninstall,
                IsUninstalled,
                IsUpToDate,
                LastActiveDate,
                LastIpToMgmt,
                LastLoggedInUserName,
                LicenseKey,
                LocationEnabled,
                LocationType,
                Locations,
                MachineType,
                MitigationMode,
                MitigationModeSuspicious,
                SrcDvcModelName,
                NetworkInterfaces,
                NetworkQuarantineEnabled,
                NetworkStatus,
                OperationalState,
                OsArch,
                SrcDvcOs,
                OsRevision,
                OsStartTime,
                OsType,
                RangerStatus,
                RangerVersion,
                RegisteredAt,
                RemoteProfilingState,
                ScanFinishedAt,
                ScanStartedAt,
                ScanStatus,
                ThreatRebootRequired,
                TotalMemory,
                UserActionsNeeded,
                Uuid,
                Creator,
                CreatorId,
                Inherits,
                IsDefault,
                Name,
                RegistrationToken,
                TotalAgents,
                Type
};
SentinelOne_view
```


# Log Ingestion Delay:
I see 21 minutes being the longest time between creation in S1 and ingestion into Azure Sentinel. If you search for SentinelOne in the Logs you can compare TimeGenerated (ingested into Azure Sentinel) and EventCreationTime (S1) to see what I mean. the analytics run every 5 min so WORST case scenario it takes 26 minutes for an alert/incident to show up in Azure Sentinel. KQL Query:
```
SentinelOne
| where EventCreationTime != ""
| extend difference = (TimeGenerated - EventCreationTime)
| project difference
| sort by difference desc
```

# SentinelOne suspicious file or action is found
Create custom analytic to alert when a known suspicious file or action is found. updated the SentinelOne Function so that it pulls ConfidenceLevel for this to work. May need to map entities. 
```
SentinelOne
| where ConfidenceLevel contains "suspicious"
```

# SentinelOne malicious file or action is found
Create custom analytic to alert when a known Malicious file is found. updated the SentinelOne Function so that it pulls ConfidenceLevel for this to work. May need to map entities. 
```
SentinelOne
//| where TimeGenerated >= now(-5min)
| where ConfidenceLevel contains "malicious"
```

# create monitor to alert if s1 logs are not received by Sentinel for 5 mins
```
SentinelOne_CL
| where TimeGenerated > now(-5min) 
//| where TimeGenerated > now(-6hour) 
| count 
| extend Boo = ( Count <= 0 )
| project Boo
// If Boo is True send alert
| where Boo == true
```

# 25% drop in logs from SentinelOne
```
let Base = SentinelOne_CL
// 30 days X 24 Hours = 720
| where TimeGenerated > now(-720hour) and TimeGenerated < now(-12hour)
| count
| extend rounded = round(Count, 2)
| extend AvgVolume = (rounded/708)
| project AvgVolume, MyKey = "Key";
let LastHour = SentinelOne_CL
| where TimeGenerated > now(-12hour)
| count
// make sure there are 2 decimal places with round
// then divide by the number of hours the count was taken
| extend average = (round(Count, 2) / 12) 
| project average, MyKey = "Key";
// join the baseline and the current data
Base | join LastHour on MyKey  
// do math on data to determine how much of a change has happened and return a Difference Percentage
| extend ['Difference %'] = (average/AvgVolume) * 100 - 100
//| where ['Difference %'] < -25
```

# Fill in Activity column with the full description of the activity.
```
// Fill in Activity column with the full description of the activity. 
SentinelOne
// will pull all "Activity Types", un-defined will list as "other"
// | where isnotempty(ActivityType) 
// will pull only the "Activity Types" we list 
| where ActivityType in (18, 19, 20, 21, 34, 76, 129, 221, 2016, 2021, 2022, 2023, 2024, 2025, 2028, 3201, 4001, 4002, 4003, 4011, 4104, 4105, 4106, 4107)
| extend Activity = case(ActivityType == 18, "18 - New Threat Mitigated", 
ActivityType == 19, "19 - New Malicious Threat Not Mitigated", 
ActivityType == 20, "20 - New Threat Preemptive Block", 
ActivityType == 21, "21 - Threat Resolved", 
ActivityType == 34, "34 - Threat Unresolved", 
ActivityType == 76, "76 - Anti Tampering Modified", 
ActivityType == 129, "129 - Allowed Domains change", 
ActivityType == 221, "221 - Threat Automatically Resolved", 
ActivityType == 2016, "2016 - User Marked Application As Threat", 
ActivityType == 2021, "2021 - Threat Killed By Policy", 
ActivityType == 2022, "2022 - Threat Remediated By Policy", 
ActivityType == 2023, "2023 - Threat Rolledback By Policy", 
ActivityType == 2024, "2024 - Threat Quarantined By Policy", 
ActivityType == 2025, "2025 - Threat Quarantined From Network By Policy", 
ActivityType == 2028, "2028 - Threat Incident Status Changed", 
ActivityType == 3201, "3201 - Remote shell created", 
ActivityType == 4001, "4001 - Threat Mark As Threat", 
ActivityType == 4002, "4002 - Threat Suspicious Resolved", 
ActivityType == 4003, "4003 - New Suspicious Threat Not Mitigated", 
ActivityType == 4011, "4011 - Threat Suspicious Unresolved", 
ActivityType == 4104, "4104 - STAR manual response marked event as malicious", 
ActivityType == 4105, "4105 - STAR manual response marked event as suspicious", 
ActivityType == 4106, "4106 - STAR active response marked event as malicious", 
ActivityType == 4107, "4107 - STAR active response marked event as suspicious", "other")
```


# More KQL Searches
```
SentinelOne
| where ActivityType != ""
| summarize count() by ActivityType
| sort by count_ desc 
```


```
SentinelOne_CL | where data_confidenceLevel_s contains "malicious"
```
```
SentinelOne_CL | where data_threatClassification_s != ""
```
```
SentinelOne_CL | where threatInfo_classification_s != ""
```
```
SentinelOne_CL
```


























| Sorted Columns |
|----------------|
| TimeGenerated [UTC] |
| ConfidenceLevel |
| ThreatClassification |
| EventVendor |
| EventProduct |
| AccountName |
| ActivityType |
| EventCreationTime [UTC] |
| DataAccountName |
| DataFullScopeDetails |
| DataScopeLevel |
| DataScopeName |
| DataSiteId |
| DataSiteName |
| SrcUserName |
| EventId |
| EventOriginalMessage |
| SiteId |
| SiteName |
| UpdatedAt [UTC] |
| UserIdentity |
| EventType |
| DataByUser |
| DataRole |
| DataUserScope |
| EventTypeDetailed |
| DataSource |
| DataExpiryDateStr |
| DataExpiryTime |
| DataNetworkquarantine |
| DataRuleCreationTime |
| DataRuleDescription |
| DataRuleExpirationMode |
| DataRuleId |
| DataRuleName |
| DataRuleQueryDetails |
| DataRuleQueryType |
| DataRuleSeverity |
| DataScopeId |
| DataStatus |
| DataSystemUser |
| DataTreatasthreat |
| DataUserId |
| DataUserName |
| EventSubStatus |
| AgentId |
| DataComputerName |
| DataExternalIp |
| DataGroupName |
| DataSystem |
| DataUuid |
| GroupId |
| GroupName |
| DataGroup |
| DataOptionalGroups |
| DataCreatedAt [UTC] |
| DataDownloadUrl |
| DataFilePath |
| DataFilename |
| DataUploadedFilename |
| Comments |
| DataNewValue |
| DataPolicyId |
| DataPolicyName |
| DataNewValueb |
| DataShouldReboot |
| DataRoleName |
| DataScopeLevelName |
| ActiveDirectoryComputerDistinguishedName |
| ActiveDirectoryComputerMemberOf |
| ActiveDirectoryLastUserDistinguishedName |
| ActiveDirectoryLastUserMemberOf |
| ActiveThreats |
| AgentVersion |
| AllowRemoteShell |
| AppsVulnerabilityStatus |
| ComputerName |
| ConsoleMigrationStatus |
| CoreCount |
| CpuCount |
| CpuId |
| SrcDvcDomain |
| EncryptedApplications |
| ExternalId |
| ExternalIp |
| FirewallEnabled |
| GroupIp |
| InRemoteShellSession |
| Infected |
| InstallerType |
| IsActive |
| IsDecommissioned |
| IsPendingUninstall |
| IsUninstalled |
| IsUpToDate |
| LastActiveDate [UTC] |
| LastIpToMgmt |
| LastLoggedInUserName |
| LicenseKey |
| LocationEnabled |
| LocationType |
| Locations |
| MachineType |
| MitigationMode |
| MitigationModeSuspicious |
| SrcDvcModelName |
| NetworkInterfaces |
| NetworkQuarantineEnabled |
| NetworkStatus |
| OperationalState |
| OsArch |
| SrcDvcOs |
| OsRevision |
| OsStartTime [UTC] |
| OsType |
| RangerStatus |
| RangerVersion |
| RegisteredAt [UTC] |
| RemoteProfilingState |
| ScanFinishedAt [UTC] |
| ScanStartedAt [UTC] |
| ScanStatus |
| ThreatRebootRequired |
| TotalMemory |
| UserActionsNeeded |
| Uuid |
| Creator |
| CreatorId |
| Inherits |
| IsDefault |
| Name |
| RegistrationToken |
| TotalAgents |
| Type |




```
AccountName
ActiveDirectoryComputerDistinguishedName
ActiveDirectoryComputerMemberOf
ActiveDirectoryLastUserDistinguishedName
ActiveDirectoryLastUserMemberOf
ActiveThreats
ActivityType
AgentId
AgentVersion
AllowRemoteShell
AppsVulnerabilityStatus
Comments
ComputerName
ConfidenceLevel
ConsoleMigrationStatus
CoreCount
CpuCount
CpuId
Creator
DataAccountName
DataByUser
DataComputerName
DataCreatedAt [UTC]
DataDownloadUrl
DataExpiryDateStr
DataExpiryTime
DataExternalIp
DataFilename
DataFilePath
DataFullScopeDetails
DataGroup
DataGroupName
DataNetworkquarantine
DataNewValue
DataNewValueb
DataOptionalGroups
DataPolicyId
DataPolicyName
DataRole
DataRoleName
DataRuleCreationTime
DataRuleDescription
DataRuleExpirationMode
DataRuleId
DataRuleName
DataRuleQueryDetails
DataRuleQueryType
DataRuleSeverity
DataScopeId
DataScopeLevel
DataScopeLevelName
DataScopeName
DataShouldReboot
DataSiteId
DataSiteName
DataSource
DataStatus
DataSystem
DataSystemUser
DataTreatasthreat
DataUploadedFilename
DataUserId
DataUserName
DataUserScope
DataUuid
EncryptedApplications
EventCreationTime [UTC]
EventId
EventOriginalMessage
EventProduct
EventSubStatus
EventType
EventTypeDetailed
EventVendor
ExternalId
ExternalIp
FirewallEnabled
GroupId
GroupIp
GroupName
Infected
Inherits
InRemoteShellSession
InstallerType
IsActive
IsDecommissioned
IsDefault
IsPendingUninstall
IsUninstalled
IsUpToDate
LastActiveDate [UTC]
LastIpToMgmt
LastLoggedInUserName
LicenseKey
LocationEnabled
Locations
LocationType
MachineType
MitigationMode
MitigationModeSuspicious
Name
NetworkQuarantineEnabled
NetworkStatus
OperationalState
OsArch
OsRevision
OsStartTime [UTC]
OsType
RangerStatus
RangerVersion
RegisteredAt [UTC]
RegistrationToken
RemoteProfilingState
ScanFinishedAt [UTC]
ScanStartedAt [UTC]
ScanStatus
SiteId
SiteName
SrcDvcDomain
SrcDvcModelName
SrcDvcOs
SrcUserName
ThreatClassification
ThreatRebootRequired
TimeGenerated [UTC]
TotalAgents
TotalMemory
Type 
UpdatedAt [UTC]
UserActionsNeeded
UserIdentity
Uuid
```
