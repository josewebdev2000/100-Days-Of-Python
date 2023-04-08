#!/bin/python3

# Python Turtle Challenge 3: Draw a dashed line

from turtle import Turtle, Screen

screen = Screen()

tom = Turtle()
tom.hideturtle()
tom.penup()
tom.goto(-200,0)
tom.pendown()

for _ in range(30):
    tom.pencolor("red")
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()

screen.exitonclick()