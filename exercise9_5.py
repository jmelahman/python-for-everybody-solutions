#!/usr/bin/env python3
"""
Exercise  9.5: This program records the domain name (instead of the address)
where the message was sent from instead of who the mail came from (i.e., the
whole email address). At the end of the program, print out the contents of
your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
['media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7, 'gmail.com': 1,
'caret.cam.ac.uk': 1, 'iupui.edu': 8}

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""

dictionary_domains = dict()                       # Initialize variables
maximum = 0
maximum_domain = ''

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    quit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        atpos = words[1].find('@')               # Position of '@'
        domain = words[1][atpos + 1:]              # Store characters after '@'
        if domain not in dictionary_domains:
            dictionary_domains[domain] = 1       # First entry
        else:
            dictionary_domains[domain] += 1      # Additional counts

print(dictionary_domains)

#made code for maximum count at domain
for address in dictionary_domains:
    if dictionary_domains[address] > maximum:     # Checks if new maximum
        # Update the maximum if needed
        maximum = dictionary_domains[address]
        # Stors the address of maximum
        maximum_address = address

print(maximum_address, maximum)
