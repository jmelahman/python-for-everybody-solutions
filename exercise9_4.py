#!/usr/bin/env python3
"""
Exercise  9.4: Add code to the above program to figure out who has the most
messages in the file.

After all the data has been read and the dictionary has been created, look
through the dictionary using a maximum loop (see Section [maximumloop]) to
find who has the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.ed 5

Enter a file name: mbox.txt
zqian@umich.edu 195

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""


dictionary_addresses = dict()                   # Initialize variables
maximum = 0
maximum_address = ''

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

    if words[1] not in dictionary_addresses:
        dictionary_addresses[words[1]] = 1      # First entry
    else:
        dictionary_addresses[words[1]] += 1     # Additional counts

for address in dictionary_addresses:
    if dictionary_addresses[address] > maximum:     # Checks if new maximum
        # Update the maximum if needed
        maximum = dictionary_addresses[address]
        # Stors the address of maximum
        maximum_address = address

print(maximum_address, maximum)
