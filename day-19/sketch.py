#!/bin/python3

# Sketch Challenge 1: Make a simple Sketch App

# D: Rotate to the Right
# S: Move Backwards
# A: Rotate to the Left
# W: Move Forwards
# C: Clear and Restore

from turtle import Turtle, Screen

DISTANCE = 20
ANGLE = 20

def main():
    """Run the program as a whole."""
    global tom, screen

    screen = Screen()

    tom = Turtle()

    # Add event listeners
    screen.listen()

    screen.onkey(key = "d", fun = move_right)
    screen.onkey(key = "s", fun = move_backward)
    screen.onkey(key = "a", fun = move_left)
    screen.onkey(key = "w", fun = move_forward)
    screen.onkey(key = "c", fun = restore)

    screen.exitonclick()

def move_forward():
    
    tom.forward(DISTANCE)

def move_backward():

    tom.backward(DISTANCE)

def move_left():

    tom.left(ANGLE)

def move_right():

    tom.right(ANGLE)

def restore():
    """Clear the screen and place the turtle on the origin of the canvas."""
    
    tom.clear()
    tom.home()
    

if __name__ == "__main__":
    main()

