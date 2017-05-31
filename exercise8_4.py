"""
Exercise  8.3: Download a copy of the file from www.py4e.com/code3/romeo.txt

Write a program to open the file romeo.txt and read it line by line. For each
line, split the line into a list of words using the split function. 

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, May 31, 2017
"""

myList = []
fhand = open('romeo.txt')
for line in fhand:
	words = line.split()				#Splits line into array of words
	for word in words:
		if word in myList : continue	#Discards duplicates
		myList.append(word)				#Updates the list
print(sorted(myList))					#Alphabetical order