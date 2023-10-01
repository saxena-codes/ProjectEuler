"""
Problem 12 - Highly Divisible Traingular Number

The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:
1: 1
3: 1, 3
6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28

We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
"""

"""
Solution:

The important observation to improve your code is that the nth triangular number is given by
T(n) = n(n+1)/2.
Now, n and n+1 are coprime.
If a and b are coprime numbers,
the number of divisors of a*b is just the product of number of divisors of a and b
"""

def no_of_divisors(in_number):
    
    factors_len = 0
    in_number = int(in_number)

    for value in range(1, in_number+1):
        if in_number%value == 0:
            factors_len += 1
    
    return factors_len

for n in range(1, 1000000):
    Tn = (n*(n+1))/2
    if n%2 == 0:
        cnt = no_of_divisors(n/2)*no_of_divisors(n+1)
    else:
        cnt = no_of_divisors(n)*no_of_divisors((n+1)/2)
    
    if cnt > 500:
        print(int(Tn))
        break