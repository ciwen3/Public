Dim num1, num2
	set num1 = ""
	set num2 = ""

Function MAxNum(ByVal num1, ByVal num2)
	If (num1 > num2) then
		MsgBox ("the larger number is " & num1 & "")
	Else
		MsgBox ("the larger number is " & num2 & "")
	End If
End Function

