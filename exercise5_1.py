"""
Exercise 5.1: Write a program which repeatedly reads numbers until the user
enters "done". ONce "done" is entered, print out the total, count, and average
of the numbers. If the user enters anything other than a number, detect their
mistake using try and except and print an error message and skip to the next
number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.33333333333333

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
	input_number = input('Enter a number: ')
	if input_number == 'done' : break	#Exits the loop
	try:
		number = float(input_number)	#Only allows input floats
	except:
		print('Invalid input')

	count = count + 1					#Counter
	total = total + number				#Running total
	
average = total / count					#Computes the average
	
print(total,count,average)
