import re
import base64

def deobfuscate(obfuscated_commands):
  deobfuscated_commands = []

  # Remove concatenation
  obfuscated_commands = [re.sub(r'\+\s*\"(.+?)\"', r'\1', c) for c in obfuscated_commands]

  # Do string formatting
  obfuscated_commands = [re.sub(r'-F\s*\"(.+?)\"', r'\1', c) for c in obfuscated_commands]

  # Remove extra parentheses and quotes
  obfuscated_commands = [re.sub(r'[\(\)]', '', c) for c in obfuscated_commands]
  obfuscated_commands = [re.sub(r'^\"|\"$', '', c) for c in obfuscated_commands]

  # Base64 decode
  deobfuscated_commands = [base64.b64decode(c).decode('utf-8') for c in obfuscated_commands]

  # Remove -EncodedCommand representation
  deobfuscated_commands = [re.sub(r'^.+?\s', '', c) for c in deobfuscated_commands]

  return deobfuscated_commands

# Test the deobfuscate function
obfuscated_commands = [
  "dwB{0}AG8AYQBtAGkA" -F "o", "notused", "NA",
  "dwB{0}A`YQBtAGkA" -F "o", "notused", "NA",
  "dwB{0}A" + "G8A`YQBtAGkA" -F "o", "notused", "NA",
  "dwB{0}A" + "G8A`YQBtAGkA" -F "o",
  "dwBoAG8AYQBtAGkA",
  "dwBoAG8AYQBtAGkA"
]
deobfuscated_commands = deobfuscate(obfuscated_commands)
print(deobfuscated_commands)
