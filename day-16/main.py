#!/bin/python3

import turtle
from prettytable import PrettyTable

# Instantiate a turtle object

timmy = turtle.Turtle()
timmy.color("cyan")
timmy.shape("turtle")
timmy.forward(100)

my_screen = turtle.Screen()

# Only exit screen when it is clicked
my_screen.exitonclick()

# create a pretty table
table = PrettyTable()

# Add data to tables by column
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Change alignment of the table to left
table.align = "l"

print(table)