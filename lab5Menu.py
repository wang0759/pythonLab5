#Create a program that displays a simple menu to the user

import wang0759Library
from gfxhat import lcd, backlight
import random
import time

def mainMenu():

    print('welcome to my menu!')
    print('1.Create a function that displays a vertical line at a given x coordinate on the gfx hat.')
    print('2.Create a function that displays a horizontal line at a given y coordinate.')
    print('3.Create a function that creates a staircase starting at a specific coordinate. One stair has a width of w and a height of h.')
    print('4.Create a function that displays random pixel on the screen for a given period of time specifies in seconds.')
    print('5.Create a function clearBacklight() that resets the backlight color.')
    while True:
        try:
            selection = int(input('Please select from 1 to 5:'))
            if selection==1:
                xLine()
                break
            elif selection==2:
                yLine()
                break
            elif selection==3:
                stair()
                break
            elif selection==4:
                randPixel()
                break
            elif selection==5:
                clearBacklight()
                break
            else:
                print("Invalid choice. Please enter 1-5.")
                mainMenu()
        except ValueError:
            print('Invalid choice. Please enter 1-5.')
    exit


mainMenu()

