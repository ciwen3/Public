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
	
'confirmation msgbox
'verify that the drive Z was loaded
'possible printer confirmation code
'might want to put in confirmation msgbox
'==================================
Call Printer_Status

Sub Printer_Status
    strComputer ="."
    intPrinters = 1
    Set objWMIService = GetObject _
      ("winmgmts:\\" & strComputer & "\root\CIMV2")
    Set colItems = objWMIService.ExecQuery _
      ("SELECT * FROM Win32_Printer")
    WScript.Sleep(1000)
    For Each objItem In colItems
      WScript.Echo _
        "Printer: " & objItem.DeviceID & vbCrLf & _
        "===============================================" & vbCrLf & _
        "Driver Name ............. " & objItem.DriverName & vbCrLf & _
        "Port Name ............... " & objItem.PortName & vbCrLf & _
        "Printer State ........... " & objItem.PrinterState & vbCrLf & _
        "Printer Status .......... " & objItem.PrinterStatus & vbCrLf & _
        "Print Processor ......... " & objItem.PrintProcessor & vbCrLf & _
        "Spool Enabled ........... " & objItem.SpoolEnabled & vbCrLf & _
        "Shared .................. " & objItem.Shared & vbCrLf & _
        "ShareName ............... " & objItem.ShareName & vbCrLf & _
        "Horizontal Res .......... " & objItem.HorizontalResolution & vbCrLf & _
        "Vertical Res ............ " & objItem.VerticalResolution & vbCrLf
      intPrinters = intPrinters + 1
    next
End Sub