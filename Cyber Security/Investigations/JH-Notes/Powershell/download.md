# Invoke-WebRequest
```
Invoke-WebRequest -URI $URL -OutFile $Path
```
```
Invoke-WebRequest "http://www.contoso.com" | Select-Object -ExpandProperty Content | Out-File "file"
```

# Invoke-RestMethod
```
Invoke-RestMethod -Uri <source> -OutFile <destination>
```
```
$source = 'http://speedtest.tele2.net/10MB.zip'
$destination = 'c:\dload\10MB.zip'
Invoke-RestMethod -Uri $source -OutFile $destination
```

# New-Object System.Net.WebClient
```
(New-Object System.Net.WebClient).DownloadFile ($URL, $Path)
```
```
$WebClient = New-Object System.Net.WebClient
$WebClient.DownloadFile("https://www.contoso.com/file","C:\path\file")
```
```
# Define the source link and destination path
$source = 'http://speedtest.tele2.net/10MB.zip'
$destination = 'c:\dload\10MB.zip'
# Create the new WebClient
$webClient = [System.Net.WebClient]::new()
# Download the file
$webClient.DownloadFile($source, $destination)
```

# System.Net.Http.HttpClient
```
# Set the source and destination
$source = 'http://speedtest.tele2.net/10MB.zip'
$destination = 'c:\dload\10MB.zip'
# Create the HTTP client download request
$httpClient = New-Object System.Net.Http.HttpClient
$response = $httpClient.GetAsync($source)
$response.Wait()
# Create a file stream to pointed to the output file destination
$outputFileStream = [System.IO.FileStream]::new($destination, [System.IO.FileMode]::Create, [System.IO.FileAccess]::Write)
# Stream the download to the destination file stream
$downloadTask = $response.Result.Content.CopyToAsync($outputFileStream)
$downloadTask.Wait()
# Close the file stream
$outputFileStream.Close()
```

# Start-BitsTransfer
```
Start-BitsTransfer -Source $URL -Destination $Path
```
```
Import-Csv .\filelist.csv | Start-BitsTransfer
```

# wget
```
wget
```

# Install-Module
Download and install one or more modules from an online gallery.

# Update-Module
Download/install a new module version.

# Update-Help
Download and install the newest PowerShell help files on your computer.




# References: 
- https://www.itprotoday.com/powershell/3-ways-download-file-powershell
- https://4sysops.com/archives/use-powershell-to-download-a-file-with-http-https-and-ftp/
- https://adamtheautomator.com/powershell-download-file/
- https://ss64.com/ps
