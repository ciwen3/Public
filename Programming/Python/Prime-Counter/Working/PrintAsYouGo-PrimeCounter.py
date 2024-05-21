import time

start = time.time()
nums=range(2,1000000)
prime_list = []

def is_prime(i):
	for num in i:
		trust = True
		if num in range(2,4): # needed to add the prime numbers 2 & 3 to the list. its a limitation of using the modulus of 6 on a number. 
			print(num)
		elif (num%6) == 1 or (num%6) == 5:
			check = ".0"
			for x in prime_list: 
				if x <= int(num/2):
					if str(num/x).endswith(check): 
						trust = False
						break
			if trust == True:
				print(num)

is_prime(nums)
#print(prime_list)

end = time.time()
print(end - start)
