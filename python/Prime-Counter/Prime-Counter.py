#!/usr/bin/env python3

path = './Prime-Count.txt'
prime_file = open(path,'r+')

path = './Bad-Prime-Count.txt'
badprime_file = open(path,'r+')

lower=0
upper=100000000  # this was the max I could get it to run at on my PC. 
array = [ 2, 3, 5]
badarray = [ ]

for num in range (lower, upper+1):
    primer = num * 6
    pone = primer + 1
    pfive = primer + 5
    A = pone/3   
    B = pfive/3  
    if pone>0:
        if A > 1:
            for i in array:
                if pone % i==0:
                    badarray.append(pone)
                    break
                elif i > A:
                    array.append(pone)
                    break
                else:
                    continue             
        if B > 1:
            for i in array:
                if pfive % i==0:
                    badarray.append(pfive)
                    break
                elif i > B:
                    array.append(pfive)
                    break
                else:
                    continue  
print(array)
prime_file.write(str(array))
badprime_file.write(str(badarray))
print("")
print("Done, Please check my work.")
