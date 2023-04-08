# Scoreboard class

# Scoreboard for the Pong game

from turtle import Turtle

class Scoreboard(Turtle):
    """Keep track of Pong Game."""

    def __init__(self):
        """Initialize this Pong object."""

        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Make the scoreboard interactive."""

        # Clear to avoid overwritting
        self.clear()
        self.goto(-100, 160)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 160)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """Increase left's paddle score."""

        self.l_score += 1
        self.update_scoreboard()
    
    def r_point(self):
        """Increase right's paddle score."""
        self.r_score += 1
        self.update_scoreboard()
