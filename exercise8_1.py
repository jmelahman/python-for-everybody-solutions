"""
Exercise  8.1: Write a function called chop that takes a list and modifies it,
removing the first and last elements, and returns None.

Then write a function called middle that takes a list and returns a new list
that contains all but the first and last elements.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, May 31, 2017
"""


def chop(t):
#Takes a list, modifies it, removing the first and last elements, and returns
#None.
#Input:	t -- a list
#Output:None
	del(t[0])							#Removes the first element
	del(t[-1])							#Removes the last element

def middle(t):
#Takes a list and returns a new list that contains all but the first and last 
#elements.
#Input: t -- a list
#Output: new -- new list with first and last elements removed
	new = t[1:]							#Stores all but the first element
	del(new[-1])						#Deletes the last element
	return(new)
	
myList = [1,2,3,4]
myList2 = [1,2,3,4]

chopList = chop(myList)
print(myList)							#Should be [2,3]
print(chopList)							#Should be None

middleList = middle(myList2)
print(myList2)							#Should be unchanged
print(middleList)						#Should be [2,3]
