#!/bin/python3

# Python Turtle Challenge 4: Random Walk

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
distance = 30

tim = Turtle()
tim.shape("turtle")
tim.pensize(10)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen.exitonclick()
