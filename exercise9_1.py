#!/usr/bin/env python3
"""
Exercise  9.1: Write a program that reads the words in words.txt and stores
them as keys in a dictionary. Download a copy of the file from
https://www.py4e.com/code3/words.txt. It doesn't matter what the values are.
Then use the 'in' operator as a fast way to check whether a string is in the
dictionary.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""


search = input('Input words you wanna search ')
count = 0
countd = 0 
dictionary_words = dict()                   # Initializes the dictionary
fhand = open('words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        count += 1
        if word in dictionary_words:        # Discards duplicates
            continue  
        countd += 1  
        
        dictionary_words[word] = count      # Value is first time word appears
        
print(countd,'not same words from', count)

if search in dictionary_words:
    print('True. You got the word',search)
else:
    print('False. There are not word like that')

