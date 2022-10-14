#!/usr/bin/env python3
# pylint: disable=assignment-from-no-return
"""
Exercise  8.1: Write a function called chop that takes a list and modifies it,
removing the first and last elements, and returns None.

Then write a function called middle that takes a list and returns a new list
that contains all but the first and last elements.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""


def chop(lst):
    """
    Takes a list, modifies it, removing the first and last elements, and
    returns None.
    Input:  lst -- a list
    Output: None
"""
    del lst[0]                          # Removes the first element
    del lst[-1]                         # Removes the last element


def middle(lst):
    """
    Takes a list and returns a new list that contains all but the first and
    last elements.
    Input: lst -- a list
    Output: new -- new list with first and last elements removed
    """
    new = lst[1:]                       # Stores all but the first element
    del new[-1]                         # Deletes the last element
    return new


my_list = [1, 2, 3, 4]
my_list2 = [1, 2, 3, 4]

chop_list = chop(my_list)
print(my_list)                          # Should be [2,3]
print(chop_list)                        # Should be None

middle_list = middle(my_list2)
print(my_list2)                         # Should be unchanged
print(middle_list)                      # Should be [2,3]
