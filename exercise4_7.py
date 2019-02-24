"""
Exercise 4.7: Rewrite the grade program from previous chapter using a function
called computegrade that takes a score as its parameter and returns a grade as
a string.

Score	Grade
>= 0.9	  A
>= 0.8	  B
>= 0.7	  C
>= 0.6	  D
< 0.6	  F
~~~

Enter score: 0.95
A

Enter score: perfect
Bad score

Enter score: 10.0
Bad score

Enter score: 0.75
C

Enter score: 0.5
F

Run the program repeatedly  to test the various, different values for input.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, May 28, 2017
"""

def computegrade(score):
#Computes the final grade based on a 0.0 to 1.0 scale
#Input:		score -- score (must be between 0.0 and 1.0)
#Output:	prints final grade as a string
	if score >= 0.0 and score <= 1.0:
		if score >= 0.9:
			print('A')
		elif score >= 0.8:
			print('B')
		elif score >= 0.7:
			print('C')
		elif score >= 0.6:
			print('D')
		else:
			print('F')

	else:
		print('Bad score')


input_score = input('Enter score: ')
try:
	score = float(input_score)			#Only allows input floats
except:
	print('Bad score')
	quit()

computegrade(score)
