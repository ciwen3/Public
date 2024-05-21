# downloading multiple csv log files from sentinel combining them and deduplicating it based on some of the colums
$TI = Get-ChildItem .\*.csv | foreach { Import-csv $_}
$TI.TI_ipEntity |  sort -unique | Out-File .\finished\Blocklist.csv -Encoding ascii
Import-Csv (Get-ChildItem '.\*.csv') | Sort-Object -Unique SourceIP,DestinationIP | Export-Csv '.\finished\Logs.csv' -NoClobber -NoTypeInformation
