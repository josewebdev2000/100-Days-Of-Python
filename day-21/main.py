#!/bin/python3

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def main():

    # Generate and setup a proper screen for the game
    screen = Screen()
    screen.setup(width = 600, height = 600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    # Generate a snake object
    snake = Snake()

    # Start listening for keystrokes
    screen.listen()
    
    # Create the food for the snake
    food = Food()

    # Start the scoreboard
    scoreboard = Scoreboard()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # Start the game
    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)

        snake.move()

        # Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect wall collision
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail
        # If head collides with any segment in the tail. Then, trigger game_over
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    screen.exitonclick()

if __name__ == "__main__":
    main()
