#!/usr/bin/python3

import re
import base64
import sys


def remove_cat(line):
  # remove any instances of concatenation
  line = re.sub(r'(\'{1,2}|\"{1,2})\s*\+\s*(\'{1,2}|\"{1,2})', '', line)
  return line


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


def base64_decode(line):
# If the line contains the string pattern
  encoded_str1 = re.search(r'(-en?c?o?d?e?d?C?o?m?m?a?n?d? |\[(System\.)*Text\.Encoding\]::\w{4,}\.GetString\(\[(System\.)*Convert\]::FromBase64String\(|\[(System\.)*Convert\]::FromBase64String\(\[Text\.Encoding\]::\w{4,}\.GetBytes\()(\S+)', line).group(0)
  encoded_str = re.search(r'(-en?c?o?d?e?d?C?o?m?m?a?n?d? |\[(System\.)*Text\.Encoding\]::\w{4,}\.GetString\(\[(System\.)*Convert\]::FromBase64String\(|\[(System\.)*Convert\]::FromBase64String\(\[Text\.Encoding\]::\w{4,}\.GetBytes\()(\S+)', line).group(5)
  # If the encoded string was found
  if encoded_str:
    # Remove certain characters from the encoded string and decode it from base64
    decoded_str = base64.b64decode(encoded_str.replace("'", "").replace("`", "").replace('"', '').replace('(', '').replace(')', '')).decode()
    # Replace the encoded string with the decoded string in the line
    line.replace(encoded_str1, decoded_str)
    return line


def order_of_operations(line):
  # variable to track if a change was made
  change_made = False

  # remove concatenation
  if re.search(r'(\'{1,2}|\"{1,2})\s*\+\s*(\'{1,2}|\"{1,2})', line):
    line = remove_cat(line)
    change_made = True

  # decode line formatting and remove extra
  if re.search(r'(-f)(((\'|\"){1,2}(\w|\.)+(\'|\"){1,2})(,*))+', line):
    line = format_decode(line)
    change_made = True

  # decode base64 and remove extra
  if re.search(r'(-en?c?o?d?e?d?C?o?m?m?a?n?d? |\[(System\.)*Text\.Encoding\]::\w{4,}\.GetString\(\[(System\.)*Convert\]::FromBase64String\(|\[(System\.)*Convert\]::FromBase64String\(\[Text\.Encoding\]::\w{4,}\.GetBytes\()(\S+)', line):
    line = base64_decode(line)
    change_made = True

  # If a change was made, call the function again
  if change_made:
    order_of_operations(line)
  # If no changes were made, return the modified line
  else:
    print(line)


# Take input and do some magic
powershell_command = sys.argv[1] #'powershell.exe -encodedCommand d2hvYW1p'

# decode powershell command
text = re.sub(r';(?!\n)', ' ;\n', powershell_command)
# Iterate through each line of the text
for line in text.split('\n'):
  order_of_operations(line)
