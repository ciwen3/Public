import sys
import base64

#take input value
value1 = input("What value would you like to convert? ")

#convert from Hex to bytes
x = bytes.fromhex(value1)
sys.stdout.buffer.write(x)
print()

#convert from bytes to base64
y = base64.b64encode(x)
sys.stdout.buffer.write(y)
print()

