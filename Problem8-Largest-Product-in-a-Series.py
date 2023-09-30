"""
Problem 8 - Largest Product in a Series

The four adjacent digits in the 1000-digit number that have the greatest product are 
9 x 9 x 8 x 9 = 5832.

(Series in Problem8-Series.txt)

Find the thirteen adjacent digits in the 100-digit number that have the greatest product.
What is the value of this product?
"""
from pathlib import Path
path = Path('Problem8.txt')
digits_1000 = path.read_text().strip()
digits_1000 = digits_1000.replace("\n", "")
digits_1000 = list(digits_1000)

max_product = 0
max_product_digits = []
count = 0
while count < len(digits_1000) - 12:

    # Multipying consequent 13 digits
    temp_product = 1
    count_13 = 0
    while count_13 < 13:
        temp_product *= int(digits_1000[count + count_13])
        count_13 += 1

    if max_product < temp_product:
        max_product = temp_product
    count += 1

print(max_product)
#print(max_product_digits)