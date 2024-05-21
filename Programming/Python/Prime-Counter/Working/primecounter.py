import time

start = time.time()
nums=range(2,1000000)
prime_list = []

def is_prime(i):
	for num in i:
		trust = True
		if num in range(2,4): # needed to add the prime numbers 2 & 3 to the list. its a limitation of using the modulus of 6 on a number. 
			prime_list.append(num)
		elif (num%6) == 1 or (num%6) == 5:
			check = ".0"
			for x in prime_list: #2, 3, 5, 7, 11, 13, 17, 19, 23, 
				if x <= int(num/2):
					if str(num/x).endswith(check): #25/5=5.0
						trust = False
						break
			if trust == True:
				prime_list.append(num)

is_prime(nums)
print(prime_list)

end = time.time()
print(end - start)

