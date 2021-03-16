'VBScript: FinalProject.vbs
'written by: Christopher Iwen
'Date: 01/14/16
'Class: Comp230
'Professor: Stanley Kuchel
'=================================================

'Used throughout the script (pg. 179)
'====================================
Dim strDomain , strUser , oNetwork , vResult , vaResult
Set oNetwork = CreateObject("WScript.Network")
strDomain = oNetwork.UserDomain
strUser = oNetwork.UserName
	
'Questions and user input (pg. 103-105, 179)
'pulls computer name and user name for the MsgBox
'================================================
vResult = MsgBox ("Welcome to " & strDomain & ", "& strUser &"!" &_
	vbCr & "Would you like to access the Network Drive?", _
	36, "Network Share Script")
	
If vResult = 6 Then 
'Map Network Drive (pg. 175)
'===========================
	oNetwork.MapNetworkDrive "Z:" , "\\Alice\Share", _
	False, "mygu", "1derland"

	end if 
	
	
'Questions and user input (pg. 103-105, 179)
'===========================================
vaResult = MsgBox ("Would you like to access the Network Printer?", _
	36, "Network Share Script")

If vaResult = 6 Then 
'Add Network Printer (pg. 177)
'=============================
	oNetwork.AddWindowsPrinterConnection "\\Alice\Printer"

'Set Network Printer as Defualt (pg. 178)
'========================================
	oNetwork.SetDefaultPrinter( _
	"\\Alice\Printer")


	end if 	
	