#!/usr/bin/env python3
"""
Exercise 4.6: Rewrite your pay computation with time-and-a-half for overtime
and create a function called computepay which takes two paramteters (hours and
rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""


def computepay(tmp_hours, tmp_rate):
    """
    Calculates the amount to pay taking into account overtime
    Inputs: tmp_hours -- the total hours worked
            tmp_rate -- pay rate of the employee
    Output: amount due to employee
    """
    if tmp_hours <= 40.0:
        return tmp_rate * tmp_hours                # No overtime calculation

    # Since the value is returned if hours <= 40, we no longer need the
    # else statement here.
    overtime = tmp_hours - 40.0                # How much overtime is left
    return (tmp_rate * 40.0) + (1.5 * tmp_rate * overtime)


def check_for_float(input1):
    """
    Checks if the type of "input1" is a float and returns the value if so.
    Input:    input1 -- variable to check
    Output: val -- value of float
    """
    try:
        val = float(input1)                # Only allows input floats
        return val
    except ValueError:
        print('Error, please enter numeric input')
        quit()


def process():
    input_name = input('Input name of employer: ')
    input_hours = input('Enter Hours: ')
    hours = check_for_float(input_hours)

    input_rate = input('Enter Rate: ')
    rate = check_for_float(input_rate)

    pay = computepay(hours, rate)
    print('Name of Employee:', input_name,'and The Pay is', pay)

process()

while True:
    again = input('Still Wanna Count? (y/n) ')
    if again == 'Y' or again == 'y':
        process()
    else:
        quit()
