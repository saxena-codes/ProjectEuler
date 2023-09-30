"""
Problem 15 - Lattice Paths

Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?

"""

"""
Solution: 

Undertanding theory:
https://stemhash.com/counting-lattice-paths/

For a 4x4 grid: 

n = 4
k = 4
n = n+k = 8

(n Choose k)
nCk = n! / {(n-k)! * k!}

So in this case for a 4x4 grid:
nCk = 8! / {(8-4)! * 4!}
nCk = 40320/ (24*24) = 70
"""
import math
def factorial(n):
    return math.factorial(n)

# For 20x20 Grid
n = 20
k = 20
n = n + k
nCk = factorial(n) / (factorial(n-k)*factorial(k))
print("Answer:")
nCk = int(nCk)
print(nCk)