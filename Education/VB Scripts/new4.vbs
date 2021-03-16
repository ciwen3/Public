WScript.StdOut.Write("Please Enter your age ....")
ageStr = WScript.StdIn.ReadLine()
If ageStr < 13 OR ageStr > 19 Then 
	WScript.StdOut.WriteLine("The value of age is a Teenager")
Else
	WScript.StdOut.WriteLine("The value of age is NOT a Teenager")
End If
WScript.StdOut.WriteLine("End of Program")