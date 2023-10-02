"""
Problem 23 - Non-Abundant Sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.

By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def find_factors_sum(n):
    factors_sum = 0
    for value in range(1, n):
        if n%value == 0:
            factors_sum += value
    return factors_sum

def check_abundant_number(n):
    result = False
    factors_sum = find_factors_sum(n)
    if factors_sum > n:
        result = True
    return result

# making abundant_number list
abundant_number_list = []
for value in range(1, 28123):
    temp = check_abundant_number(value)
    if temp:
        abundant_number_list.append(value)

#Preparing Answer List
answer_list = []
for value in range(0, 28123 + 1):
    answer_list.append(value)

# Checking if sum of two abundant numbers are less that 28123
# And removing it from answer_list, replacing with 0
for x in range(0, len(abundant_number_list)):
    for y in range(x, len(abundant_number_list)):
        sum_of_2_abundant_nos = abundant_number_list[x] + abundant_number_list[y]
        if sum_of_2_abundant_nos <= 28123:
            if answer_list[sum_of_2_abundant_nos]:
                answer_list[sum_of_2_abundant_nos] = 0

print("Answer:")
print(sum(answer_list))