"""
Problem 13 - Large Sum

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
(Numbers in Problem13-Numbers.txt)
"""

"""
Solution:

Adding only first 12 digits of each number in order to get the answer.
"""
# Reading Content
from pathlib import Path
path = Path("Problem13-Numbers.txt")
numbers = path.read_text().strip()
lines = numbers.splitlines()

list_of_first_12s = []
for value in lines:
    temp = value[0:12]
    list_of_first_12s.append(temp)

answer = 0
for value in list_of_first_12s:
    answer += int(value)

print("Answer:")
answer = str(answer)
print(answer[0:10])