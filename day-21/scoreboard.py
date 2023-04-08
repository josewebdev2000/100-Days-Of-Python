# Scoreboard Class

# Software Object to keep track of the score of the snake game

from turtle import Turtle

class Scoreboard(Turtle):
    """Keep track of the snake game."""

    ALIGNMENT = "center"
    FONT = ("Courier", 24, "normal")

    def __init__(self):
        """Initialize this scoreboard."""

        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align = Scoreboard.ALIGNMENT, font = Scoreboard.FONT)
    
    def increase_score(self):
        """Increase the score."""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """Write Game Over."""
        self.goto(0,0)
        self.write("GAME OVER", align=Scoreboard.ALIGNMENT, font=Scoreboard.FONT)
        
