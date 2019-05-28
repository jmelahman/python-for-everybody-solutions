"""
Exercise  9.3: Write a program to read through a mail log, build a histogram
using a dictionary to count how many messages have come from each email
address, and print the dictionary.

Enter file name: mbox-short.txt
{'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 3,
'zqian@umich.edu': 4, 'rjlowe@iupui.edu': 2, 'cwen@iupui.edu': 5,
'gsilver@umich.edu': 3, 'wagnermr@iupui.edu': 1,
'antranig@caret.cam.ac.uk': 1, 'gopal.ramasammycook@gmail.com': 1,
'david.horwitz@uct.ac.za': 4, 'ray@media.berkeley.edu': 1}

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, May 31, 2017
"""


dictionary_addresses = dict()                   # Initializes the dictionary
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in dictionary_addresses:
            dictionary_addresses[words[1]] = 1  # First entry
        else:
            dictionary_addresses[words[1]] += 1     # Additional counts

print(dictionary_addresses)
