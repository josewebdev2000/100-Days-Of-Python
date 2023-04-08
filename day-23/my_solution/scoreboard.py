# Scoreboard for the Turtle Crossing Game.

from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    """Give score to the Turtle Crossing Game."""
    
    def __init__(self):
        """Initialize this Scoreboard"""
        
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard((-200,250), f"Score: {self.score}")
    
    def update_scoreboard(self, coors, text):
        """Make the scoreboard interactive."""
        
        # Clear to avoid overwritting
        self.clear()
        self.goto(coors)
        self.write(text, align="center", font=FONT)

    def increase_score(self):
        """Increase left's paddle score."""

        self.score += 1
        self.update_scoreboard((-200,250), f"Score: {self.score}")
    
    def game_over(self):
        """Terminate the game once the player loses."""
        
        # Finish once you're done with the car object
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)



