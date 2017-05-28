"""
Exercise 3.1: Rewrite your pay computation to give the employee 1.5 times the
rate for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay : 475.0

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, May 28, 2017
"""

input_hours = input('Enter Hours: ')
input_rate = input('Enter Rate: ')
hours = float(input_hours) 				#Only allows input floats
rate = float(input_rate) 				#Only allows input floats
if hours < 40:
	pay = rate * hours					#No overtime calculation
else:
	times_over = hours // 40 - 1		#Number of times over 40 hours
	overtime = hours % 40				#How much overtime is left
	pay = 40.0 * rate + times_over * rate * 60 + overtime * rate * 1.5
print('Pay:',pay)