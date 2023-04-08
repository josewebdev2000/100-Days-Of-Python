# Paddle Class

# Paddle Class for Pong Game

from turtle import Turtle

class Paddle(Turtle):

    MOTION_DISTANCE = 20

    def __init__(self, xcoor, ycoor):
        """Initialize this Paddle object."""
        
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(5,1)
        self.color("white")
        self.goto(xcoor, ycoor)

    def go_up(self):
        """Make the Paddle move up."""
        new_y = self.ycor() + Paddle.MOTION_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Make the Paddle move down."""
        new_y = self.ycor() - Paddle.MOTION_DISTANCE
        self.goto(self.xcor(), new_y)
