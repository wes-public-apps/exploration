# Purpose
The goal of this web app is to replicate the game of tetris.

# Resources
Wiki - https://en.wikipedia.org/wiki/Tetris
Standford HW Problem - https://web.stanford.edu/class/archive/cs/cs108/cs108.1092/handouts/11HW2Tetris.pdf
original rotation - https://tetris.wiki/Original_Rotation_System#:~:text=The%20Original%20Rotation%20System%20is,piece%20is%20one%20block%20higher.

# Key Terms
tetrominoes - tetris blocks
wall kicks - rotation is obstructed

# User Inputs
side to side movement
rotate - spacebar
soft drop - tap down
hard drop - hold down

# Server Driven
1. time based position update
2. random tetromino selection

# Technical Implementation
Implementing a single dimensional array for grid. Width = 10 Height = 20

States: Locked, Unlocked