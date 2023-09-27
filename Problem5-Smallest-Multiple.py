"""
Problem 5 - Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?
"""

"""
# Lengthy Approach - and how it should actually work - taking too much time.

def divisibility(dividend, divisor):
    output = False
    if dividend%divisor == 0:
        output = True
    return output

# Getting divisors ready from 1 to 20
divisors = []
for value in range(1,21):
    divisors.append(value)

count = 1
while True:
    check_divisibility = False
    for divisor in divisors:
        check_divisibility = divisibility(count, divisor)
        if check_divisibility == False:
            break

    # Checking if count is divisible by all divisors
    if check_divisibility:
        print("Answer:")
        print(count)
        break
    count += 1
    print(count)
"""

"""
How I solved it- 
1. Multiplied all the prime numbers and made a function which checks if the
all numbers from 1 to 20 diuvides the multiplication.

2. No removed the lower numbers such as 2 and 3 for as if numbers like 4, 8 and 9 are dividing the multiplication,
so they will definitely devide the number.

3. Finally with lot of iterations found a number which is divisible by all the number from 1 to 20.
"""

# not actually prime numbers - started from prime number
prime_numbers = (5,7,9,11,13,16,17,19)

#multiplication of all prime number till 20
multiplication = 1
for number in prime_numbers:
    multiplication = multiplication*number
print(multiplication)

# Getting divisors ready from 1 to 20
divisors = []
for value in range(1,21):
    divisors.append(value)

result = False
count = 1
while count <= 20:
    if multiplication%count == 0:
        result = True
    else:
        result = False
    print(f"{count}: {result}")
    count += 1
