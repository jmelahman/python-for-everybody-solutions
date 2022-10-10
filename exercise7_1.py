#!/usr/bin/env python3
"""
Exercise  7.1: Write a program to read through a file and print the contents
of the file (line by line) all in upper case. Executing the program will look
as follows:

python shout.py
enter a file name: mbox.short.txt
FROM STEPHEN.MARQUARD@UTC.AC.ZA SAT JAN 5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
    BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
    SAT, 05 JAN 2008 09:14:16 -0500

You can download the file from
www.py4e.com/code3/mbox-short.txt

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""

# If in a unix-like environment, you can download mbox-short.txt with the
# following command,
# $ curl -O https://www.py4e.com/code3/mbox-short.txt
fhand = open('mbox-short.txt')
print('Input line of words you dont wanna shout!!We will erase that line from result') 
exception = input() # made user input
count = 0

for line in fhand:                      # Handles one line at a time
    if exception not in line:               # erase input user word from our new capitalize result     
        #count += 1   
        shout = line.rstrip().upper()       # Handles one line at a time
        print(shout)                        # Removes newline and capitalizes
    else:
        count += 1
print(count,'LINE BEING ERASED CAUSE HAD WORD',exception)
