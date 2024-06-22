#!/usr/bin/python3

import re
import base64
import sys

def decode_powershell(text):
  # Use the re.sub() function to replace all semicolons that are not
  # followed by a newline character with a semicolon and a newline character
  #print(text)
  text = re.sub(r';(?!\n)', ' ;\n', text)
  #print(text)
  lline = []

  # Iterate through each line of the text
  for line in text.split('\n'):
    #print(line)
    # remove any instances of one or two quotes
    line = re.sub(r'(\'{1,2}|\"{1,2})\s*\+\s*(\'{1,2}|\"{1,2})', '', line)
    #print(line)

    if re.search(r'(-f)(((\'|\"){1,2}(\w|\.)+(\'|\"){1,2})(,*))+', line):
      list = (re.search(r'(-f)(((\'|\"){1,2}(\w|\.)+(\'|\"){1,2})(,*))+', line).group(0).split(','))
      pattern = r'(-f)(((\'|\"){1,2}(\w|\.)+(\'|\"){1,2})(,*))+'
      #print(line)
      line = re.sub(pattern, '', line )
      #print(line)
      #.sub(pat, '', line)
      for a in range(len(list)):
        pat = r'(-f)?(\'|\"){1,2}'
        list[a] = re.sub(pat, '', str(list[a]))
      for i in range(len(list)):
        line = line.replace("{"+ str(i) +"}", str(list[i]))
        #print(line)


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
      print(line)    

# Test the decode_powershell() function
powershell_command = sys.argv[1] #'powershell.exe -encodedCommand d2hvYW1p'
#print(powershell_command)
decoded_command = decode_powershell(powershell_command)
#print(decoded_command)
