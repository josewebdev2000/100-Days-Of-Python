#!/bin/python3

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

# Load data for the game
states_data = pandas.read_csv("50_states.csv")

# You may load new images as shape by adding shapes
# to the screen object
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []

# Check answer is one of the states
all_states = states_data["state"].to_list()

# Figure out coors for every U.S. state (already done)
while len(guessed_states) < len(states_data.state):
    
    # Ask user for states
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed", prompt="Enter a U.S. State Name").title()

    # Also check state is not duplicated
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_data[states_data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
    
    elif answer_state == "Exit":
        break

# States to learn.csv

# Dict of states still to guess
states_to_guess_list = [state for state in all_states if state not in guessed_states]

states_to_guess_dict = {
    "states_to_learn" : states_to_guess_list
}

to_learn = pandas.DataFrame(states_to_guess_dict)

to_learn.to_csv("states_to_study.csv")

turtle.mainloop()

