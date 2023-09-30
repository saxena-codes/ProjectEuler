"""
Problem 16 - Power Digit Sum

2^15 = 32768 and the sum of its digits is
3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

product = 2**1000
product = str(product)
number = list(product)
sum_of_digits = 0
for value in number:
    temp = int(value)
    sum_of_digits += temp

print("Answer:")
print(sum_of_digits)