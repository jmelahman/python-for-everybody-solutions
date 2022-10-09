#!/usr/bin/env python3
"""
Exercise 4.1: Run the program on your system and see what numbers you get.
Run the program more than once and see what numbers you get.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""

def gil():
    import random

    print('Guess number from 1 to 10')

    guess = int(input('My number guess: '))
#for i in range(10):
    x = random.randint(1, 10)
    if guess == x :
        print(x, ',You Right!!')
    else:
        print('Number is',x,'.You wrong')

gil()
while True:
    play = input('Still wanna play ? (y/n) ')
    if play == 'Y' or play == 'y':
        gil()
    else:
        quit()


"""
Run 1:
0.21764319507444463
0.8329991443974214
0.5701549669913151
0.8637443412384684
0.2047094119147722
0.3202386315168375
0.9782522613350779
0.9220494004895224
0.17966209998031546
0.7983521239029091

Run 2:
0.47116913276761185
0.49784628316541546
0.7292518476972524
0.2355420735182987
0.16876377822830468
0.6365600615263461
0.1689585397335408
0.41161696529382463
0.9895980083921391
0.23023688059069947
"""
