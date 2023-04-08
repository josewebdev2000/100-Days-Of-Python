#!/bin/python3

from turtle import Turtle, Screen
import random as r

def main():
    """Run the program as a whole."""
    global tim, screen, colors

    colors = ("red", "orange", "yellow", "blue", "pink", "purple")

    screen = Screen()

    # Set up the screen's width and height
    screen.setup(width = 500, height = 400)

    # Control if race is going on
    is_race_on = False

    y_positions = (-70, -40, -10, 20, 50, 80)
    turtles = []

    for i in range(0, 6):
        tim = Turtle(shape = "turtle")
        tim.penup()
        tim.color(colors[i])
        tim.goto(x = -230, y = y_positions[i])
        turtles.append(tim)

    # Ask the user on an input box what they'll bet
    user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
    
    if user_bet:
        is_race_on = True

    while is_race_on:

        for turtle in turtles:
            
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")

                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")

            rand_instance = r.randint(0,10)
            turtle.forward(rand_instance)


    screen.exitonclick()

if __name__ == "__main__":
    main()

