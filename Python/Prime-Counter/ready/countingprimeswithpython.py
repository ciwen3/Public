import os

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Check if the file 'primeoutputgpt.txt' exists
if not os.path.isfile('primeoutputgpt.txt'):
    # If the file doesn't exist, create it and append '2 3' to it
    with open('primeoutputgpt.txt', 'w') as file:
        file.write('2 3\n')

# Read the last number from the file 'primeoutputgpt.txt' into the variable 'last_number'
with open('primeoutputgpt.txt', 'r') as file:
    numbers = file.read().split()
    last_number = int(numbers[-1])

# Start an infinite loop
while True:
    last_number += 1

    # Check if (last_number % 6) is equal to 1 or 5
    if (last_number % 6) == 1 or (last_number % 6) == 5:
        # Define a function to check if the number is prime by checking against known primes
        def check_known_prime(number):
            with open('primeoutputgpt.txt', 'r') as file:
                primes = [int(x) for x in file.read().split()]
                for prime in primes:
                    if prime > number // 2:
                        break
                    if number % prime == 0:
                        return False
            return True

        # Check if last_number is prime using check_known_prime
        if check_known_prime(last_number):
            # Append last_number to 'primeoutputgpt.txt'
            with open('primeoutputgpt.txt', 'a') as file:
                file.write(f' {last_number}')

    # Restart the loop to continue checking the next number
