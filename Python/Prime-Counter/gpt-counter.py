import math

def generate_numbers():
    i = 1
    while True:
        if (i % 6 == 1) or (i % 6 == 5):
            yield i
        i += 1

# Open a file for writing
with open('results.txt', 'a') as f:
    # Write the initial numbers to the file
    f.write('2\n3\n')
    
    for number in generate_numbers():
        if not math.isqrt(number)**2 == number:
            # Write each number to the file on a new line
            f.write(str(number) + '\n')
