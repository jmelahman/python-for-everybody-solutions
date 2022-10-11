#!/usr/bin/env python3
"""
Exercise  9.2: Write a program that categorizes each mail message by which day
of the week the commit was done. To do this, look for lines that start with
"From", then look for the third word and keep a running count of each of the
days of the week. At the end of the program, print out the contents of your
dictionary (order does not matter).

Sample Line: From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""

dictionary_days = dict()                       # Initializes the dictionary
dictionary_days1 = dict()
dictionary_days2 = dict()
dictionary_days3 = dict()
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words[2] not in dictionary_days:
            dictionary_days[words[2]] = 1       # First entry
        else:
            dictionary_days[words[2]] += 1      # Additional counts
        if words[1] not in dictionary_days1:
            dictionary_days1[words[1]] = 1
        else:
            dictionary_days1[words[1]] += 1 
        if words[3] not in dictionary_days2:
            dictionary_days2[words[3]] = 1
        else:
            dictionary_days2[words[3]] += 1 
        if words[6] not in dictionary_days3:
            dictionary_days3[words[6]] = 1
        else:
            dictionary_days3[words[6]] += 1 

print('Frequency of each day:',dictionary_days)
print('Frequency of email get send:',dictionary_days1)
print('Frequency of month:',dictionary_days2)
print('Frequency of year:',dictionary_days3)
