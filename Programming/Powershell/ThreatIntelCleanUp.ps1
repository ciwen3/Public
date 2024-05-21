<#
This script was made for cleaning up lots of CSV log files downloaded from ThreatIntel Feed Alerts in MS Sentinel
This script assumes it is being run in the same folder as those downloaded CSV files
This script will do two things
1. create a list of unique blocklist of IP addresses from the CSVs to be uploaded to a firewall
2. it will combine all the logs into a single file and remove duplicates 
#>

# check to see if there is a folder called finished in the current directory, if not then create it
If (-not (Test-Path ".\finished")) { New-Item -Path ".\finished" -ItemType Directory }

# import all query_data*.csv files downloaded from MS sentinel to do work on the data
$TI = Get-ChildItem .\query_data*.csv | foreach { Import-csv $_}

# remove duplicates and create an IP blocklist
$TI.TI_ipEntity |  sort -unique | Out-File .\finished\Blocklist.csv -Encoding ascii 

# import all query_data*.csv files to combine into a single log file 
Import-Csv (Get-ChildItem '.\query_data*.csv') | Sort-Object -Unique SourceIP,DestinationIP | Export-Csv '.\finished\Logs.csv' -NoClobber -NoTypeInformation

# remove old csv files 
Get-ChildItem -Path '.\' query_data*.csv | foreach { Remove-Item -Path $_.FullName }
