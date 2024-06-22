import re
import base64

def deobfuscate(obfuscated_command):
  # Remove powershell.exe -EncodedCommand representation
  obfuscated_command = re.sub(r'^powershell\.exe\s+-EncodedCommand\s+', '', obfuscated_command)

  # Remove concatenation
  obfuscated_command = re.sub(r'\+\s*\"(.+?)\"', r'\1', obfuscated_command)

  # Do string formatting
  obfuscated_command = re.sub(r'-F\s*\"(.+?)\"', r'\1', obfuscated_command)

  # Remove extra parentheses and quotes
  obfuscated_command = re.sub(r'[\(\)]', '', obfuscated_command)
  obfuscated_command = re.sub(r'^\"|\"$', '', obfuscated_command)

  # Base64 decode
  deobfuscated_command = base64.b64decode(obfuscated_command).decode('utf-8')

  # Remove -EncodedCommand representation
  deobfuscated_command = re.sub(r'^.+?\s', '', deobfuscated_command)

  return deobfuscated_command

# Test the deobfuscate function
obfuscated_command = 'powershell.exe -EncodedCommand (("dwB{0}AG8AYQBtAGkA") -F "o", "notused", "NA")'
deobfuscated_command = deobfuscate(obfuscated_command)
print(deobfuscated_command)
