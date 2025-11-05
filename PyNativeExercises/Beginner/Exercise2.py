'''
Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.
'''

def sum_current_number():
    previous = 0
    for number in range(11):

        sum = previous + number
        print(f'Current Number {number}, Previous Number {previous}, Sum: {sum}')
        previous = number

sum_current_number()

