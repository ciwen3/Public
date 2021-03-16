'VBScript: NetShareServer.vbs
'Written by: Christopher Iwen
'Date: 01/22/16
'Class: Comp230
'Professor: Stanley Kuchel
'=========================================

Set fso = Createobject("Scripting.FileSystemObject")
Set fileServ = GetObject("WinNT://vlab-PC1/LanmanServer , FileService")

fso.CreateFolder("C:\Public")
fso.CopyFile "C:\Windows\Cursors\w*.*","C:\Public"



WScript.Echo vbCrLf & "End of Program"
