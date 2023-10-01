"""
Problem 18 - Maximum Path Sum I

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
(Traingle in Problem-018-Traingle.txt)

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""

"""
Solution:

Using WuHoUnited's example, modified for uniqueness:

   9
  7 0
 2 4 6
8 5 1 3

Ask yourself this: If you found yourself at 2, would you ever take 8 instead of 5, knowing they are the leaf nodes of the tree? Similarly, If you found yourself at 6, would you ever take 3 instead of 1, knowing those are the leaf nodes of the tree?
Certainly not. We can now reduce the tree, knowing what decision we'd take at the penultimate branch (regardless of how we got there):

   9
  7 0
10 9 9

I think you see where this is going.
"""

# Reading Content
from pathlib import Path
path = Path("Problem18-Traingle.txt")
content = path.read_text().strip()
lines = content.splitlines()

traingle_tree = []
for line in lines:
    value = line.split(" ")
    traingle_tree.append(value)

def return_reduced_line(x, y):

    # x is the larger line
    count_x = len(x) - 1
    count_y = len(y) - 1

    #initializing reduced line
    z = []
    for value in range (0, count_y+1):
        value = 0
        z.append(value)

    while count_y >= 0:

        temp = count_y
        #comparing values of x
        if x[temp] > x[temp+1]:
            z[temp] = int(y[temp]) + int(x[temp])
        else:
            z[temp] = int(y[temp]) + int(x[temp+1])
        count_y -= 1
    return z

# reducing the traingle tree while checking from the last line
count = len(traingle_tree) - 1
while count > 0:

    temp = return_reduced_line(traingle_tree[count], traingle_tree[count-1])
    del(traingle_tree[count])
    traingle_tree[count-1] = temp
    count -= 1

print("Answer:")
print(traingle_tree[0][0])