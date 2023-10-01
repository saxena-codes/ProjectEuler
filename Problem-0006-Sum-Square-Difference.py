"""
Problem 6 - Sum Square Difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025


Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

"""
Solution based on following:
(a+b)^2 = a^2 + b^2 + 2ab
(a+b+c)^2 = a^2 + b^2 + c^2 + 2ab + 2ac + 2bc
(a+b+c+d)^2 = a^2 + b^2 + c^2 + d^2 + 2ab + 2ac + 2ad + 2bc + 2bd + 2cd
and so on

So,
(a+b+c+d)^2 - (a^2 + b^2 + c^2 + d^2) = 2(ab + ac + ad + bc + bd + cd)
"""

numbers = []
for value in range(1, 101):
    numbers.append(value)

answer = 0

count_1 = 0
while count_1 < len(numbers):

    count_2 = count_1 + 1
    temp_multiply = 0
    while count_2 < len(numbers):
        temp_multiply = numbers[count_1]*numbers[count_2]
        answer += temp_multiply
        count_2 += 1

    count_1 += 1

print("Answer:")
print(answer*2)