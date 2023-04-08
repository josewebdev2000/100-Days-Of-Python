#!/bin/python3

# Python Turtle Challenge 5: Spirograph

import turtle
from turtle import Turtle, Screen
import random

# Set color mode to RGB
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    return r, g, b

screen = Screen()

directions = (0, 90, 180, 270)
radius = 100
angle = 5

tim = Turtle()
tim.speed("fastest")
tim.hideturtle()

for _ in range(72):
    tim.color(random_color())
    tim.left(angle)
    tim.circle(radius)


screen.exitonclick()

