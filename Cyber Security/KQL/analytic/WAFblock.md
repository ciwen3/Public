This was for an analytic to create alert/incidents when the WAF was experiencing a 25% increase in Blocked traffic.


```
//setting the time frames to search
let StartofBase = now(-337hour); // 14 days X 24 Hours 
let EndofBase = now(-1hour);
//IPcount will be a list of the IPs and number of WAF blocks.
let IPcount = AzureDiagnostics
| where ResourceProvider == "MICROSOFT.NETWORK" and Category == "ApplicationGatewayFirewallLog"
| where action_s == "Blocked"
| where TimeGenerated > EndofBase
| summarize count() by clientIp_s
| extend Boo = ( "" != 2 ); //this is just to get a boolean true to join with Math
// 14 day baseline Average
let Baseline = AzureDiagnostics
| where TimeGenerated between(StartofBase ..(EndofBase))
| where ResourceProvider == "MICROSOFT.NETWORK" and Category == "ApplicationGatewayFirewallLog"
| where action_s == "Blocked"
| summarize average = count() / 336
| project average, MyKey = "Key";
// last hour total
let LastHour = AzureDiagnostics
| where TimeGenerated > now(-1hour)
| where ResourceProvider == "MICROSOFT.NETWORK" and Category == "ApplicationGatewayFirewallLog"
| where action_s == "Blocked"
| summarize count()
| project count_, MyKey = "Key";
// Do Math to check if there is a 25% increase in WAF Blocks
// join the baseline and the current data
let Math = Baseline | join LastHour on MyKey
// do math on data to determine how much of a change has happened and return a Difference Percentage
| extend Difference = (average * 1.25)
| extend Boo = ( Difference <= count_ )
| project Boo;
//If ( Difference <= count_ ) == TRUE then it should show info. 
//If ( Difference <= count_ ) != TRUE then no data should be returned. 
//this will be a list of the IPs and number of WAF blocks from IPcount in descending order.  
IPcount 
| join kind=fullouter Math on Boo 
| where Boo == true
| where Boo1 == true
| sort by count_ desc 
| project clientIp_s, count_
```
