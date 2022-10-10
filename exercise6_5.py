#!/usr/bin/env python3
"""
Exercise  6.5: Take the following Python code that stores a string:

string = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the string after the
colon character and then use the float function to convert the extraced string
into a floating number.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""
string = input('Input Your Variable. Made Sure add : sign in your variable ') #words from user input

#exception if we dont use : sign
if ':' not in string:
    print('You dont insert : sign')
    quit()

col_pos = string.find(':')                  # Finds the colon character
number = string[col_pos + 1:]                 # Extracts portion after colon
confidence = float(number)                  # Converts to floating point number
print(confidence)
