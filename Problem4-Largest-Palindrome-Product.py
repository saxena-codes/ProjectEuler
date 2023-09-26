"""
Problem 4 - Largest Palindrome Product

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91x99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def check_paindrome(number):
    output = False

    #Converting the number to string
    num_string = str(number)

    #Reversing the string
    reversed_string = num_string[::-1]

    if num_string == reversed_string:
        output = True

    return output

def check_three_digit_multiples(number):

    output = None
    
    count_1 = 999
    while count_1 > 99:

        count_2 = 999
        while count_2 > 99:
            if count_1*count_2 == number:
                output = [count_1, count_2]
                break
            count_2 -= 1

        if output:
            break
        count_1 -= 1

    return output

count = 999999
while count > 99999:
    
    #check if the number is a palindrom
    is_palindrome = check_paindrome(count)
    if is_palindrome:
        multiples = check_three_digit_multiples(count)
        if multiples:
            print("Answer:")
            print(count)
            print("Multiples:")
            print(multiples)
            break

    count -= 1