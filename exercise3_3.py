#!/usr/bin/env python3
"""
Exercise 3.Write a program to prompt for a score between 0.0 and 1.0. If the
score is out of range, print an error message. If the score is between 0.0 and
1.0, print a grade using the following table:
Score    Grade
>= 0.9      A
>= 0.8      B
>= 0.7      C
>= 0.6      D
< 0.6      F
~~~

Enter score: perfect
Bad score

Enter score: 10.0
Bad score

Enter score: 0.75
C

Enter score: 0.5
F

Run the program repeatedly as shown above to test the various, different
values for input.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""
score = 0.0                                # Initialize variables
grade = ""
name = input('Input name here: ')

input1 = input('Enter score from 0 - 100: ')
try:
    score = float(input1)                  # Only allows input floats
except ValueError:
    print('Input Number From 0 - 100')
    quit()

score = score / 100

if 0.0 <= score <= 1.0:                    # Scores must be between 0.0 and 1.0
    if score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    else:
        grade = 'F. Fail'
else:
    grade = 'We are not accept number above or below range'

print(name, "get score", grade)
