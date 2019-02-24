"""
Exercise 3.2: Rewrite your pay program using try and except so that your
program handles non-numerica input gracefully by printing a message and
exiting the program. The folowing shows two executions of the program:

Enter Hours: 20
Enter Rate : nine
Error, please enter numeric input

Enter Hours: forty
Error, please enter numeric input

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, May 28, 2017
"""

input_hours = input('Enter Hours: ')
try:
	hours = float(input_hours) 			#Only allows input floats
except:
	print('Error, please enter numeric input')
	quit()

input_rate = input('Enter Rate: ') 		#Only allows input floats
try:
	rate = float(input_rate)
except:
	print('Error, please enter numeric input')
	quit()

if hours < 40:
	pay = rate * hours					#No overtime calculation
else:
	times_over = hours // 40 - 1		#Number of times over 40 hours
	overtime = hours % 40				#How much overtime is left
	pay = 40.0 * rate + times_over * rate * (40 * 1.5) + overtime * rate * 1.5
print('Pay:',pay)
