#!/bin/python3

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

def main():
    """Run the program as a whole."""

    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)

    l_paddle = Paddle(-350,0)
    r_paddle = Paddle(350,0)
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    speeding_secs = 0.1

    game_is_on = True

    while game_is_on:
        time.sleep(speeding_secs)
        screen.update()
        ball.move()

        # Detect collision with the vertical walls
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.vbounce()

        # Detect collision with right horizontal wall
        if ball.xcor() > 380:
            ball.reappear()
            scoreboard.l_point()
            speeding_secs = 0.1

        # Detect collision with left horizontal wall
        if ball.xcor() < -380:
            ball.reappear()
            scoreboard.r_point()
            speeding_secs = 0.1

        # Detect collision with right paddle and left paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
            ball.hbounce()

            speeding_secs *= 0.9
 
    screen.exitonclick()

if __name__ == "__main__":
    main()
