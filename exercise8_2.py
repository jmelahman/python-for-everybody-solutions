#!/usr/bin/env python3
"""
Exercise  8.2: Figure out which line of the above program is still not properly
guarded. See if you can construct a text file which causes the program to fail
and then modify the program so that the line is properly guarded and test it to
make sure it handles your new text file.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""


count = 0 #made variable
user = input('Enter name of file, is exercise8_2.txt or mbox-short.txt ')
fhand = open(user)
for line in fhand:
    words = line.split()

    if len(words) < 3: #exception for word with length < 3
        continue
        
    if words[0] != 'From': #exception for word startswith not from word
        continue
    print(words[1]) #print email
    count += 1 #add for every word included
    
print('Word is',count,'times') #count how many times word count
