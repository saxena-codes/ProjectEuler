"""
Problem 21 - Amicable Numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a != b,
then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 
1,2,4,5,10,11,20,22,44,55 and 110;
therefore d(220) = 284.
The proper divisors of 284 are 
1,2,4,71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def proper_divisors(n):
    divisors = []
    for value in range(1, n):
        if n%value == 0:
            divisors.append(value)
    return divisors

# making a dictionary of all divisors sum and storing them in list
divisors_sum = {}
for value in range(1, 10000):
    temp = proper_divisors(value)
    summation = sum(temp)
    if value > 1:
        divisors_sum[value] = summation

# Finding amicable numbers
ammicable_numbers = []
for key, value in divisors_sum.items():

    temp = {
        "key": key,
        "value": value
    }

    for key_1, value_1 in divisors_sum.items():
        if key_1 != value_1 and key_1 == temp["value"] and value_1 == temp["key"]:
            ammicable_numbers.append(key)
            break

print("Amicable Numbers:")
print(ammicable_numbers)
print("Answer:")
print(sum(ammicable_numbers))