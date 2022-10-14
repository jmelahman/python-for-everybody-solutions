#!/usr/bin/env python3
"""
Exercise  8.2: Figure out which line of the above program is still not properly
guarded. See if you can construct a text file which causes the program to fail
and then modify the program so that the line is properly guarded and test it to
make sure it handles your new text file.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""


fhand = open('exercise8_2.txt')
for line in fhand:
    words = line.split()

    if len(words) < 3:
        continue
    if words[0] != 'From':
        continue
    print(words[2])
