#!/bin/python3

# Python Turtle Challenge 4: Draw many shapes with random colors

# Imports
from turtle import Turtle, Screen

screen = Screen()
distance = 100

colors = tuple(set(("yellow", "cyan", "red", "light blue", "pink", "blue", "green", "orange")))

num_sides = (3,4,5,6,7,8,9,10)

internal_angles= tuple(int(360 / num_side) for num_side in num_sides)

tommy = Turtle()
tommy.hideturtle()
tommy.pensize(5)

# For every polygon
for i in range(len(num_sides)):
    # Set up a random color
    tommy.color(colors[i])
    
    # Draw the figure according to its number of sides
    for side in range(num_sides[i]):
        
        # Rotate the turtle first
        tommy.left(internal_angles[i])
        tommy.forward(distance)

screen.exitonclick()