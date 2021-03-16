num1 = ""
num2 = ""
set wshShell = WScript.CreateObject("WScript.Shell")
num1 = InputBox("Please enter the value for the first number .......")
num2 = InputBox("Please enter the value for the second number ......")

Function MaxNum(ByVal num1, ByVal num2)
	If (num1 > num2) Then
		MaxNum = num1
	Else
		MaxNum = num2
	End If
	MsgBox "the larger number is MaxNum"
	
End Function


