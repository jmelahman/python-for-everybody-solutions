"""
Exercise  11.1: Write a simple program to simulate the operation of the grep
command on Unix. Ask the user to enter a regular expression and count the
number of lines that matched the regular expression:

$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-

$ python grep.py
Enter a regular expression: java$
mbox.txt had 4218 lines that matched java$

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, June 4, 2017
"""
import re

count = 0                               # Initialize variables

input_exp = input('Enter a regular expression: ')
reg_exp = str(input_exp)                # Regular Expressions are strings
fname = 'mbox.txt'
fhand = open(fname)

for line in fhand:
    line = line.rstrip()

    # Only counts if something was found
    if re.findall(reg_exp, line) != []:
        count += 1

print(fname + ' had ' + str(count) + ' lines that matched ' + reg_exp)
