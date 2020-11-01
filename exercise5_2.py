#!/usr/bin/env python3
"""
Exercise 5.1: Write another program that prompts for a list of numbers as
above and at the end prints out both the maximum and minimum of the numbers
instead of the average.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""
from exercise5_1 import check_for_float

# Handles the special case for the first input
input1 = input('Enter a number: ')
if input1 == 'done':
    quit()                                # Exits if no input

number = check_for_float(input1)          # Ensure input is a float

smallest = number
largest = number

while True:                               # Stays in loop until break
    input1 = input('Enter a number: ')
    if input1 == 'done':
        break                             # Exits loop

    number = check_for_float(input1)      # Ensure input is a float

    if number > largest:                  # Condition for maximum
        largest = number
    if number < smallest:                 # Condition for minimum
        smallest = number

print(largest, smallest)
