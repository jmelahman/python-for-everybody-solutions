"""
Exercise 6.3: Encapsulate this code in a function named count, and generalize
it so that it accepts the string and the letter as arguments.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, May 31, 2017
"""

def count(word,letter):
#Counts the number of times a given letter appears in a word
#Input:	word -- the word in question
#		letter -- the letter in the word to count
#Output:prints the number of letters
	counter = 0
	for character in word:
		if character == letter:
			counter = counter + 1
	print(counter)

word = input('Enter the word: ')
letter = input('Enter the letter: ')
count(word,letter)