#!/usr/bin/env python3
"""
Exercise  8.6: Rewrite the program that prompts the user for a list of numbers
and prints out the maximum and minimum of the numbers at the end when the user
enters "done". Write the program to store the numbers the user enters in a list
and use the max() and min() functions to compute the maximum and minimum
numbers after the loop completes.

Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""


my_list = []                        # Initialize array
while True:
    number = 0.0
    input_number = input('Enter a number: ')
    if input_number == 'done' or input_number == ' ': #add space for process:
        break

    try:
        number = float(input_number)
    except ValueError:
        print('Invalid input')
        quit()

    my_list.append(input_number)

if my_list:
    print('Maximum: ', max(my_list) or None)
    print('Minimum: ', min(my_list) or None)
