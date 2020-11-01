#!/usr/bin/env python3
"""
Exercise  7.2: Write a program to prompt for a file name, and then read
through the file and look for lines of the form:

X-DSPAM-Confidence:0.8475

When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart
the line to extract the floating-point number on the line. count these lines
and then compute the total of the spam confidence values from these lines.
When you reach the end of the file, print out the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519

Test your file on the mbox.txt and mbox-short.txt files.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""
count = 0                                   # Initialize variables
total = 0

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened: ', fname)
    quit()

for line in fhand:
    if line.startswith('X-DSPAM-Confidence: '):
        count = count + 1
        colpos = line.find(':')
        number = line[colpos + 1:].strip()    # Removes all text except number
        SPAM_C = float(number)
        total = total + SPAM_C

average = total / count
print('Average spam confidence: ', average)
