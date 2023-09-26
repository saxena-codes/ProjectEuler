"""
Problem 5 - Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?
"""

"""
# Lengthy Approach

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
