# Description
This project is designed to allow users to play tetris in a terminal window.

# Allowed input
right arrow - move a block to the right until it hits an edge
left arrow - move a block to the left until it hits an edge
down arrow - move down a row
spacebar - transform object
a key - allow AI to play
m key - take back manual control of the game

# State
Grid detailing object location
Store user input (grid state and then series of moves to land the next block)

# Display
Time elapsed
Grid state
incoming block

# Terminology
input - any information provided by the user
block - a single filled unit in the grid
object - composite of blocks that combine to form a unique shape and have a discrete set of transformations
grid - underlying component that drives the discrete untils a block can move

# Rules
1. a block cannot overlap another block meaning any user action that would violate this must be rejected


# Configuration
allowed time in each row