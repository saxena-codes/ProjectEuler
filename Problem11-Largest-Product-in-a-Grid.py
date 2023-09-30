"""
Problem 11 - Largest Product in a Grid

In the 20 x 20 grid below, four numbers along a diagonal line have been marked in red.

(Grid in Problem11-Grid.txt)

The product of these numbers is 26 x 63 x 78 x 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the grid?
"""

"""
Solution:

Read the matrix into an array and iterate through the rows, columns and diagonals to find four adjacent cells that produce a maximum product.
We can eliminate redundant calculations by only checking right, down, diagonal down-left, and diagonal down-right.
The other complementary directions would evaluate to the same product by virtue of the commutative properties of multiplication.
"""

# Reading Content
from pathlib import Path
path = Path("Problem11-Grid.txt")
contents = path.read_text()
lines = contents.splitlines()

# Making Matrix out of Content
matrix = []
for line in lines:
    temp_line = line.split(" ")
    temp_line_int = []
    for value in temp_line:
        temp_line_int.append(int(value))
    matrix.append(temp_line_int)

largest_product = 0

# Diaganol Down-Right
x = 0
while x < 20-3:
    y = 0
    while y < 20-3:

        if x > 16: coord_x = 18-x
        else: coord_x = x
        if y > 16: coord_y = 18-y
        else: coord_y = y

        value_a = matrix[coord_x][coord_y]
        value_b = matrix[coord_x + 1][coord_y + 1]
        value_c = matrix[coord_x + 2][coord_y + 2]
        value_d = matrix[coord_x + 3][coord_y + 3]

        #print(f"{x}, {y}: {value_a}, {value_b}, {value_c}, {value_d}")
        multiplication = value_a * value_b * value_c * value_d
        if multiplication > largest_product:
            largest_product = multiplication

        y += 1
    x += 1

# Diaganol Down-Left
x = 0
while x < 20-3:
    y = 0
    while y < 20-3:

        if x > 16: coord_x = 18-x
        else: coord_x = x
        if y > 16: coord_y = 18-y
        else: coord_y = y

        value_a = matrix[coord_x][coord_y]
        value_b = matrix[coord_x + 1][coord_y - 1]
        value_c = matrix[coord_x + 2][coord_y - 2]
        value_d = matrix[coord_x + 3][coord_y - 3]

        #print(f"{x}, {y}: {value_a}, {value_b}, {value_c}, {value_d}")
        multiplication = value_a * value_b * value_c * value_d
        if multiplication > largest_product:
            largest_product = multiplication

        y += 1
    x += 1

# Columns
x = 0
while x < 20-3:
    y = 0
    while y < 20:

        if x > 16: coord_x = 18-x
        else: coord_x = x
        if y > 16: coord_y = 18-y
        else: coord_y = y

        value_a = matrix[coord_x][coord_y]
        value_b = matrix[coord_x + 1][coord_y]
        value_c = matrix[coord_x + 2][coord_y]
        value_d = matrix[coord_x + 3][coord_y]

        #print(f"{x}, {y}: {value_a}, {value_b}, {value_c}, {value_d}")
        multiplication = value_a * value_b * value_c * value_d
        if multiplication > largest_product:
            largest_product = multiplication

        y += 1
    x += 1

# Rows
x = 0
while x < 20:
    y = 0
    while y < 20-3:

        if x > 16: coord_x = 18-x
        else: coord_x = x
        if y > 16: coord_y = 18-y
        else: coord_y = y

        value_a = matrix[coord_x][coord_y]
        value_b = matrix[coord_x][coord_y + 1]
        value_c = matrix[coord_x][coord_y + 2]
        value_d = matrix[coord_x][coord_y + 3]

        #print(f"{x}, {y}: {value_a}, {value_b}, {value_c}, {value_d}")
        multiplication = value_a * value_b * value_c * value_d
        if multiplication > largest_product:
            largest_product = multiplication

        y += 1
    x += 1

print("Answer:")
print(largest_product)