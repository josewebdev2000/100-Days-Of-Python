# Ball Class

# Ball for the Pong Game

from turtle import Turtle

class Ball(Turtle):
    """Ball for Pong."""

    def __init__(self):
        """Initialize this Ball object."""

        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """Move the ball around the screen."""

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def vbounce(self):
        """Bounce the ball when it hits the wall."""
        self.y_move *= -1

    def hbounce(self):
        """Bounce the ball when it hits a paddle."""
        self.x_move *= -1

    def reappear(self):
        """Make the ball reapear at the center of the screen."""
        self.goto(0,0)
        self.hbounce()









        
