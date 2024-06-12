```
Apart from utcNow() function  other datetime functions can be used to work with dates and times. Date and time functions available are:

startOfDay – Return the start of the day for a timestamp.
startOfHour – Return the start of the hour for a timestamp.
startOfMonth – Return the start of the month for a timestamp
addDays – Add several days to a timestamp.
addHours – Add several hours to a timestamp.
addMinutes – Add several minutes to a timestamp.
addSeconds – Add several seconds to a timestamp.
addToTime – Add several time units to a timestamp.
convertFromUtc – Convert a timestamp from Universal Time Coordinated (UTC) to the target time zone.
convertTimeZone – Convert a timestamp from the source time zone to the target time zone.
convertToUtc – Convert a timestamp from the source time zone to Universal Time Coordinated (UTC).
getFutureTime – Return the current timestamp plus the specified time units
getPastTime – Return the current timestamp minus the specified time units.

 
dayOfMonth – Return the day of the month component from a timestamp.
dayOfWeek – Return the day of the week component from a timestamp.
dayOfYear – Return the day of the year component from a timestamp.
subtractFromTime – Subtract several time units from a timestamp.
ticks – Return the ticks property value for a specified timestamp
formatDateTime – Return the date from a timestamp.
```

### get last months name
```kql
let f = (a:int){
	case(
	a==1,"January", 
	a==2,"February", 
	a==3,"March",
	a==4,"April",
	a==5,"May",
	a==6,"June",
	a==7,"July",
	a==8,"August",
	a==9,"September",
	a==10,"October",
	a==11,"November",
	a==12,"December",
    "ERROR"
	)
};
search *
| extend month = f(getmonth(startofmonth(datetime(now),-1)))
| summarize arg_min(TimeGenerated, *) by month
| project month
```
