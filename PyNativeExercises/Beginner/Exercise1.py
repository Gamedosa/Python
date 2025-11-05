'''
Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
'''

def sum_of_two_numbers(number1, number2):
    limit = 1000
    product = number1 * number2
    sum = number1 + number2
    if(product) <= limit:
        print(product)
    else: print(sum)

sum_of_two_numbers(40,30)

