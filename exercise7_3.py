#!/usr/bin/env python3
"""
Exercise  7.3: Sometimes when programmers get vored or want to have a bit of
fun, they adda harmless Easter Egg to their program. Modify the program that
prompts the user for a file name so that is prints a funny message when the
the user types in the exact file name "na na boo boo". the program should
behave normally for all other files which exist and don't exit. Here is a
sample execution of the program:

python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt

python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt

python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""

fname = input('Enter the file name: ')
word = input('What word from line you wanna count? ') #input user for word you wanna search

try:
    if fname == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
        exit()
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

count = 0
countw = 0
for line in fhand:
    if line.startswith(word):
        count += 1
    if word in line:
        countw += 1 
#add condition when count word in front of line and count word in line same or not
if count == countw:
    print('Same Count')

print('There were', count, 'lines start with',word,'in', fname) #print for count at first of line
print('There were', countw, word,'words in lines at', fname) #print for count word in line
