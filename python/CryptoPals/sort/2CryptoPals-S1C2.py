import sys
import base64

print("This program will take two equal-length buffers ")
print("and produces their XOR combination.")

#take input value
value1 = input("What is the first Value? ")
a = int(value1, 16)
print(a)
print(hex(a))
print(len(value1))
x = len(value1)

#take input value
value2 = input("What is the second Value? ")
b = int(value2, 16)
print(b)
print(hex(b))
print(len(value2))
y = len(value2)

if x == y:
	z = bin(a ^ b)
	print(z)
else:
	print("The values you entered are not equal-length buffers.")
	print("Closing Program.")
