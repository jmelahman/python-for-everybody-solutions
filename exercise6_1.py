#!/usr/bin/env python3
"""
Exercise 6.1: Write a while loop that starts at the last character in the
string and works its way backwards to the first character in the string,
printing each letter on a separate line, except backwards.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""

fruit = 'banana'
index = len(fruit) - 1                    # Convert to index
while index >= 0:
    letter = fruit[index]
    print(letter)
    index -= 1                          # Update index
