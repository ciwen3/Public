#!/usr/bin/python3

import re
import base64
import sys

def decode_powershell(text):
  # Use the re.sub() function to replace all semicolons that are not
  # followed by a newline character with a semicolon and a newline character
  text = re.sub(r';(?!\n)', ';\n', text)
  lline = []

  # Iterate through each line of the text
  for line in text.split('\n'):
    # Use a regular expression to find and remove any instances of one or two 
    # single or double quotes that are preceded and followed by zero or more 
    # spaces and a plus sign
    line = re.sub(r'(\'{1,2}|\"{1,2})\s*\+\s*(\'{1,2}|\"{1,2})', '', line)
    #print("this is the concatenation changes " + line)

    # If the line contains the string pattern
    if re.search(r'(-en?c?o?d?e?d?C?o?m?m?a?n?d? |\[(System\.)*Text\.Encoding\]::\w{4,}\.GetString\(\[(System\.)*Convert\]::FromBase64String\(|\[(System\.)*Convert\]::FromBase64String\(\[Text\.Encoding\]::\w{4,}\.GetBytes\()(\S+)', line):
      # Find the base64 encoded string
      encoded_str1 = re.search(r'(-en?c?o?d?e?d?C?o?m?m?a?n?d? |\[(System\.)*Text\.Encoding\]::\w{4,}\.GetString\(\[(System\.)*Convert\]::FromBase64String\(|\[(System\.)*Convert\]::FromBase64String\(\[Text\.Encoding\]::\w{4,}\.GetBytes\()(\S+)', line).group(0)
      #print("this is the encoded changes " + str(encoded_str1))
      encoded_str = re.search(r'(-en?c?o?d?e?d?C?o?m?m?a?n?d? |\[(System\.)*Text\.Encoding\]::\w{4,}\.GetString\(\[(System\.)*Convert\]::FromBase64String\(|\[(System\.)*Convert\]::FromBase64String\(\[Text\.Encoding\]::\w{4,}\.GetBytes\()(\S+)', line).group(5)
      #print("this is the encoded changes " + str(encoded_str))

      # If the encoded string was found
      if encoded_str:
        # Remove certain characters from the encoded string and decode it from base64
        decoded_str = base64.b64decode(encoded_str.replace("'", "").replace("`", "").replace('"', '').replace('(', '').replace(')', '')).decode()
        #print("this is the decoded changes " + decoded_str)

        # Replace the encoded string with the decoded string in the line
        lline.append(line.replace(encoded_str1, decoded_str))
        #print("this is the line 2 changes " + lline)

  # Return the modified text
  if len(lline) > 0:
  	for i in range(len(lline)):
  		print(lline[i])
  else:
  	return line

# Test the decode_powershell() function
powershell_command = sys.argv[1] #'powershell.exe -encodedCommand d2hvYW1p'
decoded_command = decode_powershell(powershell_command)
print(decoded_command)
