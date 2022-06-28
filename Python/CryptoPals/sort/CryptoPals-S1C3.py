
hex1 = input("What is the XOR encoded message? ")
#hex1 = int(hex1, 16)
#print(hex1)

import binascii

nums = binascii.unhexlify(hex1)
print(nums)


strings = (''.join(chr(num ^ key) for num in nums) for key in range(256))
max(strings, key=lambda s: s.count(' '))


