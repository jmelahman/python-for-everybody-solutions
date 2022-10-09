#!/usr/bin/env python3
"""
Exercise 3.1: Rewrite your pay computation to give the employee 1.5 times the
rate for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay: 475.0

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""
pay = 0.0                                   # Initialize variables

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))                    # Only allows input floats (made it short)

if hours < 40:
    pay = rate * hours                      # No overtime calculation
else:
    overtime = hours - 40                   # Calculate amount of overtime
    pay = (rate * 40.0) + (1.5 * rate * overtime)

print('Pay: ', pay)
