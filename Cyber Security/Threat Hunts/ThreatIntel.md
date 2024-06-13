# Threat Intel
https://learn.microsoft.com/en-us/azure/sentinel/use-threat-indicators-in-analytics-rules

### pull Threat Intel from other workspace
This is a modified TI map Analytic 
```kql
let dt_lookBack = 1h; // Look back 1 hour for DNS events
let ioc_lookBack = 14d; // Look back 14 days for threat intelligence indicators
// Fetch threat intelligence indicators related to IP addresses
let IP_Indicators = workspace('<workspace-name>').ThreatIntelligenceIndicator
  | where TimeGenerated >= ago(ioc_lookBack)
  | summarize LatestIndicatorTime = arg_max(TimeGenerated, *) by IndicatorId
  | where Active == true and ExpirationDateTime > now()
  | where isnotempty(NetworkIP) or isnotempty(EmailSourceIpAddress) or isnotempty(NetworkDestinationIP) or isnotempty(NetworkSourceIP)
  | extend TI_ipEntity = iff(isnotempty(NetworkIP), NetworkIP, NetworkDestinationIP)
  | extend TI_ipEntity = iff(isempty(TI_ipEntity) and isnotempty(NetworkSourceIP), NetworkSourceIP, TI_ipEntity)
  | extend TI_ipEntity = iff(isempty(TI_ipEntity) and isnotempty(EmailSourceIpAddress), EmailSourceIpAddress, TI_ipEntity)
  | where ipv4_is_private(TI_ipEntity) == false and  TI_ipEntity !startswith "fe80" and TI_ipEntity !startswith "::" and TI_ipEntity !startswith "127.";
// Perform a join between IP indicators and DNS events
IP_Indicators
  // Use innerunique to keep performance fast and result set low, as we only need one match to indicate potential malicious activity that needs investigation
  | join kind=innerunique (
      DnsEvents
      | where TimeGenerated >= ago(dt_lookBack)
      | where SubType =~ "LookupQuery" and isnotempty(IPAddresses)
      | mv-expand SingleIP = split(IPAddresses, ", ") to typeof(string)
      | extend DNS_TimeGenerated = TimeGenerated
  )
  on $left.TI_ipEntity == $right.SingleIP
  // Filter out DNS events that occurred after the expiration of the corresponding indicator
  | where DNS_TimeGenerated < ExpirationDateTime
  // Group the results by IndicatorId and SingleIP, and keep the DNS event with the latest timestamp
  | summarize DNS_TimeGenerated = arg_max(DNS_TimeGenerated, *) by IndicatorId, SingleIP
  // Select the desired output fields
  | project DNS_TimeGenerated, Description, ActivityGroupNames, IndicatorId, ThreatType, Url, DomainName, ExpirationDateTime, ConfidenceScore,
    TI_ipEntity, Computer, EventId, SubType, ClientIP, Name, IPAddresses, NetworkIP, NetworkDestinationIP, NetworkSourceIP, EmailSourceIpAddress, Type
  | extend timestamp = DNS_TimeGenerated, HostName = tostring(split(Computer, '.', 0)[0]), DnsDomain = tostring(strcat_array(array_slice(split(Computer, '.'), 1, -1), '.'))
```
##### Note:
```kql
let IP_Indicators = workspace('<workspace-name>').ThreatIntelligenceIndicator
```
This will import new TI from the other workspace. great for sharing TI in an MSSP when the TI company wants to charge you a new license for each workspace. 


### pull from remote CSV example
This is directly from Microsoft TI map Analytic
```kql
let dt_lookBack = 1h;
let ioc_lookBack = 14d;
let IoCList = materialize(externaldata(TimeGenerated:datetime,IoC:string,IoC_Type:string,ExpirationDateTime:datetime,Description:string,Action:string, ConfidenceScore:real, ThreatType:string, Active:string,Type:string, TrafficLightProtocolLevel:string, ActivityGroupNames:string)[@"https://raw.githubusercontent.com/microsoft/mstic/master/RapidReleaseTI/Indicators.csv"] with(format="csv", ignoreFirstRecord=True));
let IP_Indicators = (union isfuzzy=true
(ThreatIntelligenceIndicator
| where TimeGenerated >= ago(ioc_lookBack) and ExpirationDateTime > now()
| summarize LatestIndicatorTime = arg_max(TimeGenerated, *) by IndicatorId
| where Active == true
// Picking up only IOC's that contain the entities we want
| where isnotempty(NetworkIP) or isnotempty(EmailSourceIpAddress) or isnotempty(NetworkDestinationIP) or isnotempty(NetworkSourceIP)
// As there is potentially more than 1 indicator type for matching IP, taking NetworkIP first, then others if that is empty.
// Taking the first non-empty value based on potential IOC match availability
| extend TI_ipEntity = iff(isnotempty(NetworkIP), NetworkIP, NetworkDestinationIP)
| extend TI_ipEntity = iff(isempty(TI_ipEntity) and isnotempty(NetworkSourceIP), NetworkSourceIP, TI_ipEntity)
| extend TI_ipEntity = iff(isempty(TI_ipEntity) and isnotempty(EmailSourceIpAddress), EmailSourceIpAddress, TI_ipEntity)
//Exclude local addresses, using the ipv4_is_private operator
| where ipv4_is_private(TI_ipEntity) == false and  TI_ipEntity !startswith "fe80" and TI_ipEntity !startswith "::" and TI_ipEntity !startswith "127."
),
(IoCList
| where IoC_Type =~ 'IP'
| where ExpirationDateTime > now()
| summarize LatestIndicatorTime = arg_max(TimeGenerated, *) by IoC
| where Active =~ 'True'
| extend TI_ipEntity = IoC
| project-away  IoC_Type
)
);
IP_Indicators
// using innerunique to keep perf fast and result set low, we only need one match to indicate potential malicious activity that needs to be investigated
| join kind=innerunique (
    AzureDiagnostics
    | where TimeGenerated >= ago(dt_lookBack)
    | where OperationName in ("AzureFirewallApplicationRuleLog", "AzureFirewallNetworkRuleLog")
    | parse kind=regex flags=U msg_s with Protocol 'request from ' SourceHost 'to ' DestinationHost @'\.? Action: ' Firewall_Action @'\.' Rest_msg
    | extend SourceAddress = extract(@'([\.0-9]+)(:[\.0-9]+)?', 1, SourceHost)
    | extend DestinationAddress = extract(@'([\.0-9]+)(:[\.0-9]+)?', 1, DestinationHost)
    | extend RemoteIP = case(not(ipv4_is_private(DestinationAddress)), DestinationAddress, not(ipv4_is_private(SourceAddress)), SourceAddress, "")
    // Traffic that involves a public address, and in case this is the source address then the traffic was not denied
    | where isnotempty(RemoteIP)
    | project-rename AzureFirewall_TimeGenerated = TimeGenerated
)
on $left.TI_ipEntity == $right.RemoteIP
| where AzureFirewall_TimeGenerated < ExpirationDateTime
| summarize AzureFirewall_TimeGenerated = arg_max(AzureFirewall_TimeGenerated, *) by IndicatorId, RemoteIP, IoC
| project LatestIndicatorTime, Description, ActivityGroupNames, IndicatorId, ThreatType, Url, DomainName, ExpirationDateTime, ConfidenceScore, AzureFirewall_TimeGenerated,
TI_ipEntity, Resource, Category, msg_s, SourceAddress, DestinationAddress, Firewall_Action, Protocol, NetworkIP, NetworkDestinationIP, NetworkSourceIP, EmailSourceIpAddress, Type
| extend timestamp = AzureFirewall_TimeGenerated
```
