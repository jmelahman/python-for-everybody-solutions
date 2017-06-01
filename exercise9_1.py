"""
Exercise  9.1: Write a program that reads the words in words.txt and stores
them as keys in a dictionary. Download a copy of the file from 
https://www.py4e.com/code3/words.txt. It doesn't matter what the values are. 
Then use the 'in' operator as a fast way to check whether a string is in the
dictionary.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, May 31, 2017
"""

count = 0
dictionary_words = dict()                       #Initializes the dictionary
fhand = open('words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        count = count + 1                       
        if word in dictionary_words : continue   #Discards duplicates
        dictionary_words[word] = count        #Value is first time word appears
        
if 'Python' in dictionary_words: 
    print('True')
else:
    print('False')