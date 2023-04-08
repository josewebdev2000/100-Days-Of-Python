##      Snake Object

## Software Snake Object for the 
## Snake Game program in turtle

from turtle import Turtle

class Snake(object):
    """Snake for the Snake game."""

    # Define moving directions
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0
    STARTING_POSITIONS = ((0,0), (-20,0), (-40,0))

    def __init__(self):
        """Initialize this snake."""

        # Store the body parts in a property
        self.segments = []

        # Initial number of snakes
        self.init_segs = 3

        self.width = 20

        self.color = "white"

        self.shape = "square"

        # Distance move per iteration
        self.moved_per_iter = 20

        # Populate the snakes segments list
        self.populate()

        # Save the snakes body
        self.head = self.segments[0]

    def populate(self):
        """Populate the snake's body."""

        # X coordinate for the snakes

        # Generate the snake body with 3
        for i in range(self.init_segs):
            self.add_segment(Snake.STARTING_POSITIONS[i])

    def extend(self):
        """Add new segment to the snake."""
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        """Add a segment to the snake's body."""

        segment = Turtle(self.shape)
        segment.color(self.color)
        segment.penup()
        segment.width(self.width)
        segment.goto(position)

        # Populate the snakes segments list
        self.segments.append(segment)

    def move(self):
        """Move the snake."""

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(self.moved_per_iter)

    def up(self):
        """Make the serpent move upwards."""
        
        # Make sure the serpent doesn't do up when it is going dowm
        if self.head.heading() != Snake.DOWN:
            self.head.setheading(Snake.UP)

    def down(self):
        """Make the serpent move down."""

        # Make sure the serpent doesn't go down when it is going up
        if self.head.heading() != Snake.UP:
            self.head.setheading(Snake.DOWN)

    def left(self):
        """Make the serpent move left."""
        
        # Make sure the serpent doesn't go left when it is going right
        if self.head.heading() != Snake.RIGHT:
            self.head.setheading(Snake.LEFT)

    def right(self):
        """Make the serpent move right."""
        
        # Make sure the serpent doesn't go right when it is going left
        if self.head.heading() != Snake.LEFT:
            self.head.setheading(Snake.RIGHT)

