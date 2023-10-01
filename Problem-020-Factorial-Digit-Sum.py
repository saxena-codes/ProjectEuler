"""
Problem 20 - Factorial Digit Sum

n! means n x (n-1) x ... x 3 x 2 x 1.

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!.
"""

import math

factorial_100 = math.factorial(100)
factorial_100 = str(factorial_100)
factorial_100 = list(factorial_100)

# Adding all the digits in the list
answer = 0

for value in factorial_100:
    answer += int(value)

print("Answer:")
print(answer)