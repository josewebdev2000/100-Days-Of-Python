#!/bin/python3

import time
from turtle import Turtle, Screen

def main():
    """Run the program as a whole."""

    # Generate a square window
    screen = Screen()
    screen.setup(width = 600, height = 600)
    screen.bgcolor("black")
    screen.title("Awesome Snake Game")

    # Turn tracer off in order to get rid of default animations
    screen.tracer(0)

    # Store the snake's body parts in a list and append them once they are properly created
    body_parts = []

    # Generate the three turtles using a for loop
    x_coor = 0
    for i in range(3):
        body_part = Turtle("square")
        body_part.color("white")
        body_part.penup()
        body_part.width(20)
        body_part.setx(x_coor)
        x_coor -= 20
        body_parts.append(body_part)

    # As long as the user is playing, keep the serpent moving
    game_is_on = True

    while game_is_on:
        # Update screen to recognize animations and before handling each body part
        # To make them behave as a whole
        screen.update()
        time.sleep(0.1)
        
        # Reverse for loop through the body parts for proper motion handling
        for body_part_num in range(len(body_parts) - 1, 0, -1):
            new_x = body_parts[body_part_num - 1].xcor()
            new_y = body_parts[body_part_num - 1].ycor()
            body_parts[body_part_num].goto(new_x, new_y)

        # Send the first segment forward so the rest follow it
        body_parts[0].forward(20)


    # Exit screen on click
    screen.exitonclick()


# Run only if the program is called directly
if __name__ == "__main__":
    main()
