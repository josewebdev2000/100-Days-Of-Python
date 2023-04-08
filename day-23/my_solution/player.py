# Player Class

# Player for the Crossing Street game

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    
    def __init__(self):
        """Initialize this Player object."""
        
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.reposition()
        self.setheading(90)
    
    def move(self):
        """Move the player upwards ONLY."""
        self.sety(self.ycor() + MOVE_DISTANCE)
    
    def reposition(self):
        """Place the turtle back in the beginning when it reached the top."""
        self.goto(STARTING_POSITION)
     
    def is_at_the_end(self):
        """Checks whether this Turtle is at the end of the finish line or not."""
        return self.ycor() >= FINISH_LINE_Y
        
