'VBScript: NameAge.vbs
'written by: Christopher Iwen
'Date: 01/14/16
'Class: Comp230
'Professor: Kuchel
'=================================================
'Check for command line arguments
set args = WScript.Arguments
If args.Count < 2 then
  WScript.Echo "You must enter the name and age as Command Line Arguments!!"
  WScript.Sleep(5000)
  WScript.Quit
 end If 
 'Assign name and age Variables to Cmd Line Args

name = args.item(0)
ageStr = args.item(1)
'Calculate Age+10 and assign to ageStr10
ageStr10 = Cstr( CInt(ageStr)+10 )
'Build output as a single string msgStr
msgStr =  "Your Name is " & vbTab & vbTab & name & _
	vbCrLf & "Your Age is " & vbTab & vbTab & ageStr & _
	vbCrLf & "Your Age in 10 years is ...... " & _
	ageStr10 & vbCrLf & _
	"End of Program"

WScript.Echo msgStr