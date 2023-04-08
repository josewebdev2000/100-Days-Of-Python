#!/bin/python3

# Final Challenge: Make a 2 million dollar piece of art

import colorgram
import turtle as t
import random as r

def main():
    """Run the program as a whole."""

    # Set turtle module to allow RGB
    t.colormode(255)

    tim = t.Turtle()

    # Middle point between 180 and 270
    tim.penup()
    tim.hideturtle()
    tim.setheading(225)
    tim.forward(300)
    tim.speed("fastest")
    tim.setheading(0)
    num_of_dots = 100

    # Get colors tuple
    colors = extract_colors()

    for dot_count in range(1,num_of_dots + 1):
        tim.dot(20, r.choice(colors))
        tim.forward(50)

        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)

def extract_colors():
    """Extract colors from given image."""

    return tuple(tuple(color.rgb) for color in colorgram.extract("crazy_dots.jpg", 15))

if __name__ == "__main__":
    main()
