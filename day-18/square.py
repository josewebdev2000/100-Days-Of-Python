#!/bin/python3

# Challenge Turtle 1: Draw a Square
# Draw a 100 square 

from turtle import Turtle, Screen

my_screen = Screen()

my_turtle = Turtle()

# Hide the turtle object from the screen
my_turtle.hideturtle()

# Draw the square
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

my_screen.exitonclick()