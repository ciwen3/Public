# Prime Number Counter
![Screenshot](https://img.shields.io/badge/Platform-Universal-brightgreen)
![Screenshot](https://img.shields.io/badge/Language-Python3-blue)

I created these programs to test my theory that all prime numbers will have a modulus of 1 or 5 when divided by 6 (except 2 or 3, which are part of the equation). 

# Highest Prime Number it has counted to so far: **59,999,999**

## Prime-Test.py 
  - Will check to see if any prime number in the prime_list fits my theory. 

## Prime-Counter.py 
  - Will count out prime numbers. Currently this program is limited by the amount of memory on my computer. 

### How it works:
  - The program starts with a counting variable set to 0. Then times the counting variable by 6, then does a plus 1 and plus 5, then checks if both numbers are prime. The check continues until we have gone through 1/3 of the prime numbers below our possible prime. Then we add 1 to the counting variable and start the loop over. 

### 1. How I figured it out:
  - It was some time around the year 2012 in Houston Texas, and I was hanging out with Erika and David. These two friends of mine had gone to college for Math degrees and enjoyed playing with numbers. They told me how much time in college was spent trying to determine if a number was prime. I thought this was a cool challenge and thought about it all night and the next day. On my way home from work the next day I was stuck in traffic and decided to attempt finding a solution to determine if a number is prime. After a while I started thinking of ways to rule out multiple primes at once. Starting small and figuring I would build from there I multiplied 2 and 3 and began dividing numbers by 6. I quickly realized that if the remainder is 0 then it is not prime becasue it is divisible by 2 and 6 and an even number. If the remainder is a 2 or 4 then it is divisible by 2 and an even number. If the remainder is 3 then it is divisible by 3. This leaves 1 and 5 left. When I got home I told my friends and they helped me start checking prime numbers. And every Prime number we checked when divided by 6 had a remainder of 1 or 5. At first I thought I really had something. 
### 2. How I realized it was not correct:
  - My friends helped me checking prime numbers, and everything seemed to be woring correctly. Then we decided to test it in reverse. So we started multipling numbers by 6 and adding 1 or 5 to it and checking if it was a prime number. Pretty quickly we realized that both 25 and 49 fit the mathmatical theory but are obviously not prime numbers. 
### 3. Prime factor theory:
  - I noticed a pattern forming with 25 and 49. The square root of both are prime numbers. This led me to believe that the only numbers breaking this theory are factors of prime numbers. So far this seems to be true, but since there are infinite numbers to check I will never be certain unless proven wrong. 
### 4. Why it took so long to make this program:
  - Basically I lacked the skill until now. I have tried to write these programs many times. I always got stuck at the check where you must divide the possible prime by every number below it. if it is divisible by any of those then it is not prime. While considering this problem I realized I don't actually have to go through every number. In reality you only have to go half way to the possible prime. In my case I only need to go 1/3 of the way up the possible prime because 2 and 3 are already part of the equation. And because of my theory I would only need to check if it is factorable by prime numbers. This greatly reduced the amount of processing need to calculate prime numbers based on my theory. The other major change has been my programming skills improved a lot over the years. I didn't even know the basics of programming when I had the original theory. While I am proud that my skills have grown a lot I realize I am not an amazing programmer. Feel free to offer constructive criticism and tips on improving my code. I would also like to port this to C or C++ if anyone would like to help with that task. 
## Disclaimer: 
  - I have no clue if this theory is correct or if it would be of any help to any one ever. I will continue to test it in my spare time and think about it when I am bored. If you see a flaw in my theory or the math please let me know so that I can correct it or I can stop wasting my time. 

