"""
Exercise 4.6 Rewrite your pay computation with time-and-a-half for overtime
and create a function called computepay which takes two paramteters (hours and
rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, May 28, 2017
"""

def computepay(hours,rate):
#Calculates the amount to pay taking into account overtime
#Inputs:	hours -- the total hours worked
#			rate -- pay rate of the employee
#Output:	prints pay -- amount to be paid
	if hours < 40:
		pay = rate * hours				#No overtime calculation
	else:
		times_over = hours // 40 - 1	#Number of times over 40 hours
		overtime = hours % 40			#How much overtime is left
		pay = 40.0 * rate + times_over * rate * 60 + overtime * rate * 1.5
	print('Pay:',pay)

input_hours = input('Enter Hours: ')
try:
	hours = float(input_hours)			#Only allows input floats
except:
	print('Error, please enter numeric input')
	quit()

input_rate = input('Enter Rate: ')
try:
	rate = float(input_rate)			#Only allows input floats
except:
	print('Error, please enter numeric input')
	quit()

computepay(hours,rate)