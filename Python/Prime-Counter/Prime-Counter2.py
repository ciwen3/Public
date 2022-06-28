#!/usr/bin/env python3

# Created by Christopher Iwen 5/16/2021
# I created this based on a theory I came up with about a decade ago
# I was trying to find a way to verify if a number was Prime
# I started by seeing if I could rule out anything that was divisible by 2 & 3
# I realized that if a number was divisible by 6 then it was divisible by 2 & 3
# then I noticed that this only leaves a few options left 1 - 5
# we can rule out anything with a even modulus 2 & 4 (divisible by 2)
# we can also rule out anything with a modulus of 3 (divisible by 3)
# this only leaves numbers with a modulus of 1 or 5
# after some checking I realized that all Prime numbers, when divided by 6 will have a modulus of 1 or 5
# after some more checking I realized that other numbers also fit this pattern that aren't Prime
# after some check I started to notice a pattern
# the false positives were all factors of prime numbers (ie. 25, 49, etc.)
# this means we will still ahve to do a Prime chec to make sure the number is Prime, 
# but this greatly reduces the time to calculate
# then I realized that since we have already tested for divisible by 2 or 3 
# I don't have to go through the entire lower Primes to verify
# instead I just go to Potential Prime divided by 3 
# this greatly reduces the calculations needed as well 
# this is still in testing but I hope my theory is correct 

# I am not sure why it is not adding the number 5 to the array yet
# that is one known flaw that I need to work out
# 2 & 3 will need to be manually added to the array because of the formula used to calculate possible primes

# create file if id doesnt exist and allow appending to the file
path = './Prime-Count.txt'
prime_file = open(path,'a+')

# create file if id doesnt exist and allow appending to the file
path2 = './Bad-Prime-Count.txt'
badprime_file = open(path2,'a+')

#lower=0 #old for limited count
#upper=100000000  # this was the max I could get it to run at on my PC. 
prime_file.write(str("2\n"))
prime_file.write(str("3\n"))
# prime_file.write(str("5\n"))

# array = [ 2, 3, 5]
# badarray = [ ]

num=0

while True:
    # create file if id doesnt exist and allow appending to the file
    # path = './Prime-Count.txt'
    # prime_file = open(path,'a+')
    # # create file if id doesnt exist and allow appending to the file
    # path2 = './Bad-Prime-Count.txt'
    # badprime_file = open(path2,'a+')

    primer = num * 6
    pone = primer + 1
    pfive = primer + 5
    A = pone/3   
    B = pfive/3  
    if pone>0:  # Might not need this line
        if A > 1:
            with open(path, 'r') as array:
                for i in array:  # need to have it read each line of a file
                    if pone % int(i)==0:
                        badprime_file.write(str(pone))
                        badprime_file.write(str("\n"))
                        # badarray.append(pone)
                        break
                    elif int(i) > A:
                        prime_file.write(str(pone))
                        prime_file.write(str("\n"))
                        # array.append(pone)
                        break
                    else:
                        continue    
            array.close()         # not sure if I need
        if B > 1:
            with open(path, 'r') as array:
                for i in array:  # need to have it read each line of a file
                    if pfive % int(i)==0:
                        badprime_file.write(str(pfive))
                        badprime_file.write(str("\n"))
                        # badarray.append(pfive)
                        break
                    elif int(i) > B:
                        prime_file.write(str(pfive))
                        prime_file.write(str("\n"))
                        # array.append(pfive)
                        break
                    else:
                        continue  
            array.close()       # not sure if I need  
    num+=1
# print(badarray)
# prime_file.write(str(array))
# badprime_file.write(str(badarray))
# print("Done, Please check my work.") 
