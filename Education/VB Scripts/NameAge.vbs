'VBScript: NameAge.vbs
'written by: Christopher Iwen
'Date: 01/14/16
'Class: Comp230
'Professor: Kuchel
'=================================================
'prompt user for Name and Age
WScript.StdOut.Write("Please enter your FULL Name ..............")
'Create name and age variables
name = WScript.StdIn.ReadLine()
WScript.StdOut.WriteLine()  'Skip 1 Line
WScript.StdOut.Write("Please Enter your age ....................")
ageStr = WScript.StdIn.ReadLine()
'Calculate Age+10 and assign to ageStr10
ageStr10 = Cstr( CInt(ageStr)+10 )
'Display Name and Age Values
WScript.StdOut.WriteBlankLines(2) 'Skip 2 lines

WScript.StdOut.WriteLine("Your Name is " & vbTab & vbTab & name)
WScript.StdOut.WriteLine("Your Age is " & vbTab & vbTab & ageStr)

WScript.StdOut.WriteLine(vbCrLf & "Your Age in 10 years is ...... " & _
	ageStr10 & vbCrLf)
WScript.StdOut.WriteLine("End of Program")


