"""
Problem 10 - Summation of Primes

The sum of the primes below 10 is
2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math

def check_if_prime(in_number):
    if in_number == 1: return False

    """
    If the number n is not divisible by any prime number that is less that 
    √n than the number n is prime.
    """
    temp = 2
    while temp <= math.sqrt(in_number):
        if in_number%temp < 1:
            return False
        temp += 1
    return temp>1

limit_num = 2000000
answer = 0
for value in range(1, limit_num+1):
    check_prime = check_if_prime(value)
    if check_prime:
        answer += value

print("Answer:")
print(answer)