# Explination:
Python function that takes in a string of text as an input (text) and attempts to decode any base64-encoded strings that it finds within the input. 
It first uses the re.sub() function to replace all semicolons that are not followed by a newline character with a semicolon and a newline character. 
It then iterates through each line of the input text, using regular expressions to try to identify and extract any base64-encoded strings. 
If it finds one, it decodes the base64-encoded string and replaces the encoded string in the line with the decoded string. 
Finally, the script returns the modified text.

### Here is a brief overview of how the script works:
- The script defines the decode_powershell() function, which takes a string of text as an input.
- The re.sub() function is used to replace all semicolons that are not followed by a newline character with a semicolon and a newline character.
- The script iterates through each line of the input text.
- It uses regular expressions to try to identify and extract any base64-encoded strings from the line.
- If it finds an encoded string, it decodes the base64-encoded string and replaces the encoded string in the line with the decoded string.
- The script returns the modified text.

### example:
```
./de-b64.py 'powershell.exe [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("d2hvYW1p")'

this is the concatenation changes powershell.exe [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("d2hvYW1p")
this is the encoded changes [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("d2hvYW1p")
this is the encoded changes "d2hvYW1p")
this is the decoded changes whoami
this is the line 2 changes powershell.exe whoami
powershell.exe whoami
```
