"""
Exercise  8.3: Rewrite the guardian code in the above example without two if
statements. Instead, use a compound logical expression using the and logical
operator with a single if statement.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, May 31, 2017
"""

fhand = open('exercise8_2.txt')
for line in fhand:
	words = line.split()
	if len(words) == 0 or len(words) < 2 or words[0] != 'From' : continue
	print(words[2])
	
#P.S I am not sure why the instructions say to use the 'and' operator. 'Or' 
#works fine and using 'and' produces an error.