"""
Problem 14 - Longest Collatz Sequence

The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def count_collatz_chain(in_number):

    count = 1
    if in_number == 1 or in_number == 0: return count
    else:
        temp = in_number
        while True:

            if temp%2 == 0:
                temp = temp/2
            else:
                temp = (3*temp + 1)

            count += 1
            if temp == 1: break

    return count


starting_number = 1000000
answer = 0
answer_count = 0
while starting_number > 0:
    count = count_collatz_chain(starting_number)
    if count > answer_count:
        answer_count = count
        answer = starting_number
    starting_number -= 1

print("Answer:")
print(answer)
print("Collatz Chain Count:")
print(answer_count)