# Car Manager class

# Class for the car for the Crossing the Streets game

from turtle import Turtle
import random as r

COLORS = ("red", "orange", "yellow", "green", "blue", "purple")
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

FINISH_X_LINE = -300

WIDTH_STRETCH = 1
HEIGHT_STRETCH = 4

# Add to the cars a random element of speed to make them move differently (Different positions are not enough)
RANDOM_SPEED_FACTORS = tuple((i for i in range(0,4)))

# Populate a random list of numbers from -260 to 260 (Possible X and Y Positions of Cars)
Y_COORS = tuple(i for i in range(-240,240 + 1))
X_COORS =tuple(i for i in range(200,300))

# Y coors that where randomly chosen by the CarManager
CHOSEN_YCOORS = []

# Helper Funcs
def chosen_y_filter(ycoor):
    """Decide whether to admit a new y-coordinate into the CHOSEN_YCOORS list or not."""
    
    # Loop through every element present in the y-coordinate
    if len(CHOSEN_YCOORS) > 0:
        for y_coor in CHOSEN_YCOORS:
            # If the coordinate to add is less than 20 pixels from any ycoor present, return false
            if abs(y_coor - ycoor) < 50:
                return False
        
    # At this point, the y coordinate to add is at least 20 pixels away from every other ycoor, so return True
    return True
    
from turtle import Turtle

class CarManager(Turtle):
    """Car for the Crossing the Streets game."""
    
    def __init__(self):
        """Initialize this Turtle object."""
        
        # Initialize the Parent Class Object
        super().__init__()
        self.shape("square")
        self.penup()
        
        # Get a random color from the list of colors
        self.color(self.r_color())
        self.goto(self.new_coors())
        
        # Speed parameter
        self.speed = STARTING_MOVE_DISTANCE + r.choice(RANDOM_SPEED_FACTORS)
        
        # Get the turtle it's appropiate shape
        self.resizemode("user")
        self.shapesize(WIDTH_STRETCH, HEIGHT_STRETCH)
    
    def r_color(self):
        """Set a new random color for the user."""
        return r.choice(COLORS)
    
    def reset_x(self):
        """Place back the object to a random x-coordinate form the beginning."""
        self.setx(r.choice(X_COORS))
    
    def new_coors(self):
        """Get a random set of coordinates to position oneself."""
        
        # While the difference of the Y coordinates is less than 20, get a new y random coordinate
        xcoor = r.choice(X_COORS)
        ycoor = r.choice(Y_COORS)
        
        while not chosen_y_filter(ycoor):
            ycoor = r.choice(Y_COORS)
        
        # Add the y-coordinate to the list of chosen y coordinates
        CHOSEN_YCOORS.append(ycoor)
            
        return tuple((xcoor, ycoor))
    
    def move(self):
        """Move the car horizontally from the right to the left"""
        self.setx(self.xcor() - self.speed)
    
    def increase_speed(self):
        """Increase the current speed as the player advances levels."""
        
        self.speed += MOVE_INCREMENT
    
    def is_at_edge(self):
        """Return True when the car is at the horizontal edge of the screen."""
        return self.xcor() <= FINISH_X_LINE