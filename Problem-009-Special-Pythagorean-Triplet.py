"""
Problem 9 - Special Pythagorean Triplet

A Pythagorean triplet is a set of three natural numbers, a<b<c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
Solution:

Following understood:
a^2 + b^2 = c^2 and a + b + c = 1000

This deduce that:
=> a^2 + b^2 = c^2
=> (a+b)^2 = c^2 + 2ab
=> 2ab = (a+b)^2 - c^2
=> ab = 1/2{(a+b)^2 - c^2}
=> abc = (c/2)*{(a+b)^2 - c^2}

Now as,
a + b + c = 1000
a + b = 1000 - c

Hence,
=> abc = (c/2)*{(1000-c)^2 - c^2}
=> abc = (c/2)*(1000^2 + c^2 - 2000c - c^2)
=> abc = (c/2)*(1000^2 - 2000c)
=> abc = 500c * (1000 - 2c)
=> abc = 1000c * (500 - c)
"""

answer = 0
answer_abc = {}
found_answer = False
for value_a in range(1, 1000):
    for value_b in range(value_a, 1000):
        for value_c in range(value_b, 1000):
            if (value_a + value_b + value_c) == 1000:
                temp_object = {
                    "a": value_a,
                    "b": value_b,
                    "c": value_c                            
                }

                abc_value = temp_object['a'] * temp_object['b'] * temp_object['c']
                equation_value = (1000 * temp_object['c']) * (500 - temp_object['c'])

                if abc_value == equation_value:
                    answer = abc_value
                    answer_abc = temp_object
                    found_answer = True
                    break

            if found_answer: break
        if found_answer: break
    if found_answer: break

print("Answer:")
print(answer)
print("a,b,c values:")
print(answer_abc)