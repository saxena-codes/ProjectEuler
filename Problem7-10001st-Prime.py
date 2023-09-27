"""
Problem 7 - 10001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

import math

def check_if_prime(in_number):
    prime = True
    if in_number == 1:
        prime = False
    elif in_number == 2 or in_number == 3:
        prime = True
    else:
        count = 2
        """
        If the number n is not divisible by any prime number that is less that 
        √n than the number n is prime.
        """
        while count <= int(math.sqrt(in_number)):
            if check_if_prime(count):
                if in_number%count == 0:
                    prime = False
                    break
            count += 1
    return prime

prime_number_len = 10001
prime_number = None
prime_number_count = 0
count = 1
while True:
    prime_check = check_if_prime(count)
    if prime_check:
        prime_number = count
        prime_number_count += 1
    if prime_number_count == prime_number_len:
        break
    count += 1

print("Answer:")
print(prime_number)