#!/bin/python3

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def main():
    """Run the program as a whole."""

    # Instantiate the screen for the game
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    
    # Instantiate a player for the game.
    player = Player()
    
    # Instantiate the scoreboard
    scoreboard = Scoreboard()
    
    # Generate 8 Cars
    cars = tuple(CarManager() for i in range(8))
    
    # Move the turtle when the player presses the appropiate keys
    screen.listen()
    screen.onkey(player.move, "Up")
    screen.onkey(player.move, "w")

    # Start up the main game loop
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        
        # Move the cars
        for car in cars:
            car.move()
            
            # Check collisions with player
            if car.distance(player) < 15:
                scoreboard.game_over()
                game_is_on = False
            
            # If the car has reached the limit, reset its x coordinate
            if car.is_at_edge():
                car.reset_x()
        
        # Get the user back to the beginning if they reach the finish line
        if player.is_at_the_end():
            player.reposition()
      
            # Increase the score of the player
            scoreboard.increase_score()

screen.exitonclick()
# Only run the program if this script is executed directly
if __name__ == "__main__":
    main()
