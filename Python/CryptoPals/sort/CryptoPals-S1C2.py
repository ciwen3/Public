
hex1 = input("What is the first Value? ")
x = len(hex1)
#print(x)
hex1 = int(hex1, 16)
#print(hex1)

hex2 = input("What is the second Value? ")
y = len(hex2)
#print(y)
hex2 = int(hex2, 16)
#print(hex2)

if x == y:
	z = hex1 ^ hex2
	print(hex(z))
else:
	print("The values you entered are not equal-length buffers.")
	print("Closing Program.")
