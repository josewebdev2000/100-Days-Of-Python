from turtle import Turtle
import random as r

# Food Class
# Boiler template for the food the snake will eat in the Snake Game

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    
    def refresh(self):
        """Place the food to a new random location."""
        random_x = r.randint(-280, 280)
        random_y = r.randint(-280, 280)
        self.goto(random_x, random_y)
