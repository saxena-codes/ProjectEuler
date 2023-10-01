"""
Problem 1 - Multiples of 3 or 5

If we list all the natural numbers below 10
that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

answer = 0

# Finding all the multiple of 3 or 5 and adding to count
count = 1
while count < 10:
    if count%3 == 0 or count%5 == 0:
        answer += count
    count += 1

# Adding all the multiples of the list
print("Answer:")
print(answer)