"""
Exercise 3.1: Rewrite your pay computation to give the employee 1.5 times the
rate for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay: 475.0

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, May 28, 2017
"""
pay = 0.0                                   # Initialize variables

input_hours = input('Enter Hours: ')
input_rate = input('Enter Rate: ')
hours = float(input_hours)                  # Only allows input floats
rate = float(input_rate)                    # Only allows input floats

if hours < 40:
    pay = rate * hours                      # No overtime calculation
else:
    overtime = hours - 40                   # Calculate amount of overtime
    pay = (rate * 40.0) + (1.5 * rate * overtime)

print('Pay: ', pay)
