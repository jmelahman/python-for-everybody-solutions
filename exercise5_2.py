"""
Exercise 5.1: Write another program that prompts for a list of numbers as
above and at the end prints out both the maximum and minimum of the numbers
instead of the average.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, May 28, 2017
"""

count = 0								#Initializes values
total = 0
largest = None
smallest = None

while True:								#Stays in loop until break
	number = 0.0
	input1 = input('Enter a number: ')
	if input1 == 'done' : break			#Exits loop
	try:
		number = float(input1)			#Only allows input floats
	except:
		print('Invalid input')

	if largest is None or number > largest:		#Condition for maximum
		largest = number
	if smallest is None or number < smallest:	#Condition for Minimum
		smallest = number

	count = count + 1					#Counter
	total = total + number				#Running total
	
print(total,count,largest,smallest)
