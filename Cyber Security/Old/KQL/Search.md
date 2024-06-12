https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/search-operator



| #	| Syntax	| Meaning | (equivalent where)	| Comments |
|---|---------|---------|---------------------|----------|
| 1	| search "err"	| where * has "err"	| |
| 2	| search in (T1,T2,A*) "err"	| union T1,T2,A* \| where * has "err"	| |
| 3	| search col:"err"	| where col has "err"	| |
| 4	| search col=="err"	| where col=="err"	| |
| 5	| search "err*"	| where * hasprefix "err"	| |
| 6	| search "*err"	| where * hassuffix "err"	| |
| 7	| search "*err*"	| where * contains "err"	| |
| 8	| search "Lab*PC"	| where * matches regex @"\bLab.*PC\b"	| |
| 9	| search *	| where 0==0 | | |
| 10	| search col matches regex "..."	| where col matches regex "..."	|
| 11	| search kind=case_sensitive | | | 	All string comparisons are case-sensitive |
| 12	| search "abc" and ("def" or "hij")	| where * has "abc" and (* has "def" or * has hij")	| |
| 13	| search "err" or (A>a and A<b)	| where * has "err" or (A>a and A<b)	| |
