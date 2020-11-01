#!/usr/bin/env python3
"""
Exercise 5.1: Write a program which repeatedly reads numbers until the user
enters "done". Once "done" is entered, print out the total, count, and average
of the numbers. If the user enters anything other than a number, detect their
mistake using try and except and print an error message and skip to the next
number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.33333333333333

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""


def check_for_float(input1):
    """
    Checks if the type of "input1" is a float and returns the value if so.
    Input:    input1 -- variable to check
    Output: val -- value of float
    """
    try:
        val = float(input1)                   # Only allows input floats
        return val
    except ValueError:
        print('Error, please enter numeric input')
        quit()


# Check module name since check_for_float is being imported in the next
# exercise. See also, https://www.youtube.com/watch?v=sugvnHA7ElY (video)
# or https://www.tutorialspoint.com/python/python_modules.htm (text)
if __name__ == "__main__":
    count = 0                                 # Initializes values
    total = 0.0
    average = 0.0

    while True:                               # Stays in loop until break
        input_number = input('Enter a number: ')
        if input_number == 'done':
            break                             # Exits the while loop

        number = check_for_float(input_number)

        count += 1                            # Counter
        total = total + number                # Running total

    # Ensures count is not 0 which would cause division error
    if count:
        average = total / count               # Computes the average

    print(total, count, average)
