"""
Exercise  8.3: Rewrite the guardian code in the above example without two if
statements. Instead, use a compound logical expression using the and logical
operator with a single if statement.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, May 31, 2017
"""


fhand = open('exercise8_2.txt')
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])
