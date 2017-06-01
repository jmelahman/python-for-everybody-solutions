"""
Exercise  9.4: Add ccode to the above program to figure out who has the most
mesasges in the file.

After all the data has been read and the dictionary has been created, look
through the dictionary using a maximum loop (see Section [maximumloop]) to
find who has the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.ed 5

Enter a file name: mbox.txt
zqian@umich.edu 195

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, May 31, 2017
"""

dictionary_addresses = dict()                       #Initializes the dictionary
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
        if words[1] not in dictionary_addresses:
            dictionary_addresses[words[1]] = 1       #First entry
        else:
            dictionary_addresses[words[1]] += 1      #Additional counts

maximum = 0                                          #Initilizes the variable
for address in dictionary_addresses:
    if dictionary_addresses[address] > maximum:      #Checks if new maximum
        maximum = dictionary_addresses[address]      #Updates the maximum if need
        maximum_address = address                    #Stores the address of maximum

print(maximum_address, maximum)
    
