#!/usr/bin/env python3
"""
Exercise 4.2 Move the last line of this program to the top, so the function
call appears before the definitions. Run the program and see what error
message you get.

Code: http://www.py4e.com/code3/lyrics.py

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""

input_word = input('How much you wanna replay word: ')

try:
    input = int(input_word)              # Only allows input floats
except ValueError:
    print('Error, please enter numeric input')
    quit()

def repeat_lyrics():
    print_lyrics() 
    #print_lyrics()
    

def print_lyrics():
    for x in range(input):
        x = print("I'm a lumberjack, and I'm okay.")
        x = print('I sleep all night and I work all day.')


repeat_lyrics()




"""
Error message:
Traceback (most recent call last):
  File "/home/jamison/workspace/python-for-everybody/exercise4_2.py", line 14, in <module>
    repeat_lyrics()
NameError: name 'repeat_lyrics' is not defined
"""
