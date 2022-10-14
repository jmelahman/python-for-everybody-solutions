#!/usr/bin/env python3
"""
Exercise 3.2: Rewrite your pay program using try and except so that your
program handles non-numerical input gracefully by printing a message and
exiting the program. The following shows two executions of the program:

Enter Hours: 20
Enter Rate : nine
Error, please enter numeric input

Enter Hours: forty
Error, please enter numeric input

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""
hours = 0.0                                 # Initialize variables
rate = 0.0
pay = 0.0

input_hours = input('Enter Hours: ')
try:
    hours = float(input_hours)              # Only allows input floats
except ValueError:
    print('Error, please enter numeric input')
    quit()

input_rate = input('Enter Rate: ')
try:
    rate = float(input_rate)                # Only allows input floats
except ValueError:
    print('Error, please enter numeric input')
    quit()

if hours < 40:
    pay = rate * hours                      # No overtime calculation
else:
    overtime = hours - 40                   # Calculate amount of overtime
    pay = (rate * 40.0) + (1.5 * rate * overtime)

print('Pay: ', pay)
