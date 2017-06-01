"""
Exercise  10.2: This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the "From" line by finding
the time string and then splitting that string into parts using the colon 
character. Once you have accumulated the counts for each hour, print out the
counts, one per line, sorted by hour as shown below.

Sample line: From stephen.marquard@uct.ac.az Sat Jan 05 09:14:16 2008

Sample Execution:

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, June 1, 2017
"""
import string

dictionary_hours = dict()                       #Initializes the dictionary
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    
for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) < 2 or words[0] != 'From': 
        continue
    else:
        colpos = words[5].find(':')
        hour = words[5][:colpos]
        if hour not in dictionary_hours:
            dictionary_hours[hour] = 1       #First entry
        else:
            dictionary_hours[hour] += 1      #Additional counts

lst = list()                            #Initializes the lst
for key, val in list(dictionary_hours.items()):
    lst.append((key,val))               #fills list with hour, count of dict
    
lst.sort()                          #sorts by hour

for key, val in lst:                #
    print(key,val)