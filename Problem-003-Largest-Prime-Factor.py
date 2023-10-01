"""
Problem 3 - Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
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

def largest_prime_factor(number):
    answer = None
    count = int(math.sqrt(number)) + 2
    while count >= 2:
        
        # Checking if count is prime number or not
        checking_prime = check_if_prime(count)
        
        if checking_prime:
            # Checking if number is divisible by prime number - count.
            if number%count == 0:
                answer = count
                break
        count -= 1
    return answer

print("Answer:")
print(largest_prime_factor(600851475143))