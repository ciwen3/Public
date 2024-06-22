# powershell source
https://github.com/PowerShell/PowerShell/blob/master/docs/FAQ.md

# Order Of Operations:
### - split into new lines 
``` 
def add_new_line_after_semicolon(text):
  # Use a regular expression to find and replace semicolons that are not followed by a new line
  return re.sub(r';(?!\n)', ';\n', text)
```
### - remove concatenation: 
``` 
/(\'{1,2}|\"{1,2})\s*\+\s*(\'{1,2}|\"{1,2})/gm 
```
### - reverse a string
https://learn-powershell.net/2012/08/12/reversing-a-string-using-powershell/
```powershell
$String = "This is a test, hope it works!"
([regex]::Matches($String,'.','RightToLeft') | ForEach {$_.value}) -join ''
```
```powershell
$string = 'Hello World'
$string[-1..-$string.Length] -join ''
```
```powershell
"Hello World"[-1..-20] -join ''
```
lots of others examples on this page. 

```python
"Hello World"[::-1]
```
### - remove special characters 
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_special_characters?view=powershell-7.3

### PowerShell recognizes these escape sequences:

|Sequence |	Description|
|---------|------------|
|`0 |	Null|
|`a |	Alert|
|`b |	Backspace|
|`e |	Escape (added in PowerShell 6)|
|`f |	Form feed|
|`n |	New line|
|`r |	Carriage return|
|`t |	Horizontal tab|
|`u{x} |	Unicode escape sequence (added in PowerShell 6)|
|`v |	Vertical tab|

PowerShell also has a special token to mark where you want parsing to stop. All characters that follow this token are used as literal values that aren't interpreted.

Special parsing tokens:
|Sequence |	Description|
|---------|------------|
|-- |	Treat the remaining values as arguments not parameters|
|--% |	Stop parsing anything that follows|

### - remove \` from the strings
### - variable substitution
```
/(\$[\w.]*)(=)(.*);/gi
```
```
/(\$.+)(=)(.+);/gi
```
### - string format
```
def format_decode(line):
  list = (re.search(r'(-f)(((\'|\"){1,2}(\w|\.)+(\'|\"){1,2})(,*))+', line).group(0).split(','))
  pattern = r'(-f)(((\'|\"){1,2}(\w|\.)+(\'|\"){1,2})(,*))+'
  line = re.sub(pattern, '', line )
  for a in range(len(list)):
    pat = r'(-f)?(\'|\"){1,2}'
    list[a] = re.sub(pat, '', str(list[a]))
  for i in range(len(list)):
    line = line.replace("{"+ str(i) +"}", str(list[i]))
  return line
```
### - base64decode
```
def decode_and_replace(text):
  # Use a regular expression to find and capture base64 encoded strings
  encoded_strings = re.findall(r'(-en?c?o?d?e?d?C?o?m?m?a?n?d? |\[(System\.)*Text\.Encoding\]::\w{4,}\.GetString\(\[(System\.)*Convert\]::FromBase64String\(|\[(System\.)*Convert\]::FromBase64String\(\[Text\.Encoding\]::\w{4,}\.GetBytes\()(\S+)\s', text, re.IGNORECASE)

  # Iterate through the list of encoded strings and decode them
  for encoded in encoded_strings:
    # Remove the capture groups from the encoded string
    encoded = encoded[3]

    # Decode the base64 encoded string
    decoded = base64.b64decode(encoded).decode()

    # Use a regular expression to replace the encoded string in the original text with the decoded string
    text = re.sub(re.escape(encoded), decoded, text, flags=re.IGNORECASE)

  # Remove quotes, parentheses, and backticks from the text
  text = text.replace("'", "").replace("`", "").replace('"', '').replace('(', '').replace(')', '')

  return text
```
### - scriptblock
### - gzip

# Loop through OOO until no changes have been made:
- can create a variable that is set to no change made
- when a change is made it changes the variable
- at the end of the loop it checks the variable
- if the variable says no change has been made then save everything and exit

# Pull IOCs from the scripts:
- look for files accessed, created, or downloaded (ie. dlls, regular files)
- network connections (data sent or retrieved)
- 

# 1. Find powershell base64 encoded command
### Best:
grab the base64 identifiers and the base64 code after it:
```
"(-en?c?o?d?e?d?C?o?m?m?a?n?d? |\[(System\.)*Text\.Encoding\]::\w{4,}\.GetString\(\[(System\.)*Convert\]::FromBase64String\(|\[(System\.)*Convert\]::FromBase64String\(\[Text\.Encoding\]::\w{4,}\.GetBytes\()(\S+)\s"ig
```

```
(-en?c?o?d?e?d?C?o?m?m?a?n?d? |\[(System\.)*Text\.Encoding\]::\w{4,}\.GetString\(\[(System\.)*Convert\]::FromBase64String\(|\[Convert\]::ToBase64String\(\[Text\.Encoding\]::\w{4,}\.GetBytes\()\S+\s*
```
do a substitution to remove:
```
(-en?c?o?d?e?d?C?o?m?m?a?n?d? |\[(System\.)*Text\.Encoding\]::\w{4,}\.GetString\(\[(System\.)*Convert\]::FromBase64String\(|\[Convert\]::ToBase64String\(\[Text\.Encoding\]::\w{4,}\.GetBytes\()
```
then remove the following from the string:
```
" ' ` ( ) 
```
then base64 decode the string. 


### old
```regex
"(powershell.exe |powershell ).*(-en?c?o?d?e?d?C?o?m?m?a?n?d? |\[(System\.)*Text\.Encoding\]::\w{4,}\.GetString\(\[(System\.)*Convert\]::FromBase64String\()"ig
```
if this returns true then there is base64 code that needs to be decoded. 


works on:
```
powershell.exe -enc d2hvYW1p
powershell.exe -enco d2hvYW1p
powershell.exe -encod d2hvYW1p
powershell.exe -encode d2hvYW1p
powershell.exe -encoded d2hvYW1p
powershell.exe -encodedC d2hvYW1p
powershell.exe -encodedCo d2hvYW1p
powershell.exe -encodedCom d2hvYW1p
powershell.exe -encodedComm d2hvYW1p
powershell.exe -encodedComma d2hvYW1p
powershell -encodedComman d2hvYW1p
powershell [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String(d2hvYW1p)
powershell.exe [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("d2hvYW1p")
PowerShell [System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String(d2hvYW1p)
Powershell.exe [Text.Encoding]::Utf8.GetString([Convert]::FromBase64String('d2hvYW1p')
```
need to capture the base64 part after this. 

need to add the ability to find this
```
$MYTEXT = 'This is my secret text'
$ENCODED = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($MYTEXT))
Write-Output $ENCODED
```

### Even better version:
```regex
"(-en?c?o?d?e?d?C?o?m?m?a?n?d? |\[(System\.)*Text\.Encoding\]::\w{4,}\.GetString\(\[(System\.)*Convert\]::FromBase64String\(|\[Convert\]::ToBase64String\(\[Text\.Encoding\]::\w{4,}\.GetBytes\()"ig
```

# 2. Python module that can determine how many items need to be replaced and what to replace them with in a given string, you can use a combination of string manipulation and regular expressions.

also removes concatenation

```
import re

def parse_format_string(s):
    # Find all occurrences of {} in the string
    placeholders = re.findall(r'{(\d+)}', s)
    # Determine the number of placeholders
    num_placeholders = len(placeholders)
    # Split the string on the placeholders
    parts = re.split(r'{(\d+)}', s)
    # Return the number of placeholders and the parts of the string
    return num_placeholders, parts

def format_string(s, values):
    num_placeholders, parts = parse_format_string(s)
    # Check that the number of values matches the number of placeholders
    if len(values) != num_placeholders:
        raise ValueError('Number of values does not match number of placeholders')
    # Zip the values and parts together and join them with the values
    formatted_string = ''.join([parts[i] + values[int(parts[i+1])] for i in range(0, len(parts), 2)])
    return formatted_string

def print_formatted_string(s, values):
    formatted_string = format_string(s, values)
    print(f"gwcY='{formatted_string}'")

# Take input from a human
s = input("Enter the format string: ")
values = input("Enter the values as a comma-separated list: ").split(',')
print_formatted_string(s, values)
```

This revised program will prompt the user to enter the format string and the values as a comma-separated list, and then it will print the formatted string.

For example, if the user inputs the following:

```
Enter the format string: '{3}nabl{2}Sc{1}i{0}ptlockL{4}gging'
Enter the values as a comma-separated list: 'pt', 'r', 'e', 'E', 'o'
```

The program will output:

```
gwcY='EnableScriptBlockLogging'
```

Note that this example assumes that the placeholders in the format string are represented by {}. If the placeholders are represented by {n}, where n is a number, you can use the format() method of strings instead of regular expressions to parse the format string and substitute the values.


# 3. Python module that you can use to find and replace variables in a string of PowerShell code:

```
import re

def replace_variables(ps_code: str, var_map: dict) -> str:
    """Replaces variables in a string of PowerShell code with their values.

    Args:
        ps_code: A string containing PowerShell code.
        var_map: A dictionary mapping variable names to their values.

    Returns:
        A string of PowerShell code with the variables replaced with their values.
    """
    # Find all variables in the PowerShell code using a regular expression
    variables = re.findall(r'\$\w+', ps_code)

    # Replace each variable with its value
    for var in variables:
        if var in var_map:
            ps_code = ps_code.replace(var, str(var_map[var]))

    return ps_code
```
To use this module, you can simply import it and call the replace_variables function, passing in a string of PowerShell code and a dictionary mapping variable names to their values.

For example:

```
import powershell_variable_replacer

# PowerShell code with variables
ps_code = 'Write-Output $message'

# Dictionary mapping variables to their values
var_map = {
    '$message': 'Hello, world!'
}

# Replace variables in the PowerShell code
replaced_code = powershell_variable_replacer.replace_variables(ps_code, var_map)

# Output: 'Write-Output Hello, world!'
print(replaced_code)
```







# References: 
- https://regex101.com/

