#!/usr/bin/env python3
"""
Exercise 4.7: Rewrite the grade program from previous chapter using a function
called computegrade that takes a score as its parameter and returns a grade as
a string.

Score    Grade
>= 0.9      A
>= 0.8      B
>= 0.7      C
>= 0.6      D
< 0.6      F
~~~

Enter score: 0.95
A

Enter score: perfect
Bad score

Enter score: 10.0
Bad score

Enter score: 0.75
C

Enter score: 0.5
F

Run the program repeatedly  to test the various, different values for input.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""


def computegrade(tmp_score):
    """
    Computes the final grade based on a 0.0 to 1.0 scale. If the score is
    not between 0.0 and 1.0, returns "Bad score."
    Input:    score -- score (must be between 0.0 and 1.0)
    Output:    returns a grade as a string.
    """
    if 0.0 <= tmp_score <= 1.0:
        if tmp_score >= 0.9:
            return 'A'
        if tmp_score >= 0.8:
            return 'B'
        if tmp_score >= 0.7:
            return 'C'
        if tmp_score >= 0.6:
            return 'D'
        return 'F'
    # Case 'score' is not on the interval
    return 'Bad score'


input_score = input('Enter score: ')
score = 0.0

try:
    score = float(input_score)             # Only allows input floats
except ValueError:
    print('Bad score')
    quit()

grade = computegrade(score)
print(grade)
