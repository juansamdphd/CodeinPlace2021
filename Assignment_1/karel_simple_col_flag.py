from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""

def main():
    """
    Precondition: Karel is facing E at (1,1). No beepers in the world. Karel is a DefaultWorld (8x8)
    Postcondition: Karel sits facing E at (8,8) facing E
    """
    while front_is_clear():
        paint_corner(RED)    
        move()
    if front_is_blocked():
        paint_corner(RED)
        turn_left()
        move()
        turn_left()
        while front_is_clear():
            paint_corner(BLUE)
            move()
    if front_is_blocked():
        paint_corner(BLUE)
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            paint_corner(YELLOW)
            move()
    if front_is_blocked():
        paint_corner(YELLOW)

def turn_around():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
