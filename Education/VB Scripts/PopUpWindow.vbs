'VBScript: NameAge.vbs
'written by: Christopher Iwen
'Date: 01/14/16
'Class: Comp230
'Professor: Kuchel
'=================================================
name = "John Doe"
ageStr = "50"
'Calculate Age+10 and assign to ageStr10
ageStr10 = Cstr( CInt(ageStr)+10 )
'Display Name and Age Values


WScript.Echo "Your Name is " & vbTab & vbTab & name
WScript.Echo "Your Age is " & vbTab & vbTab & ageStr

WScript.Echo vbCrLf & "Your Age in 10 years is ...... " & _
	ageStr10 & vbCrLf
WScript.Echo "End of Program"


