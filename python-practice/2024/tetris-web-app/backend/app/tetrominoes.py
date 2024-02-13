from enum import Enum
from typing import List

from app import constants as C

class Rotation(Enum):
    original = 0
    ninety = 1
    one_eighty = 2
    two_seventy = 3

class Tetromino:
    def __init__(self, rotations):
        self._current_rotation = Rotation.original
        self._rotations: List[int] = rotations
        self._moved = False

    def fast_rotate(self, grid: List[bool]) -> List[int]:
        """Complete the rotation logic for this tetromino. If the resulting rotation is illegal
        then complete the necessary corrections.
        Returns:
            List[int]: List of positions representing the current block on the grid.
        """        
        self._current_rotation = (self._current_rotation + 1) % C.SHAPE_BLOCK_COUNT
        return self.kick(grid)
    
    def kick(self, grid: List[bool]) -> List[int]:
        """Correct the post rotation shape when it overlaps with an occupied space.
        Args:
            grid (List[bool]): 1D array representing the tetris game state.
        Returns:
            List[int]: Modified position of the current rotation.
        """        
        # TODO: validate rotation is legal. if not complete wall kick.
        # check if position is in bounds
        # check if position overlaps with existing point
        rotation = self.get_current_rotation()
        if all((p<0 or p>len(grid) or grid[p] for p in rotation)):
            return rotation

    
    def get_current_rotation(self) -> List[int]:
        """Gets the slice of the 1D array intended to track the current rotation.
        Returns:
            List[int]: List of positions representing the current block on the grid.
        """        
        start_ind = self._current_rotation * C.SHAPE_BLOCK_COUNT
        return self._rotations[start_ind:start_ind + C.SHAPE_BLOCK_COUNT]

    def translate_left(self, grid: List[bool]) -> bool:
        """Moves the tetromino to the left one block unless the block is obstructed
        Args:
            grid (List[bool]): 1D array representing the tetris game state.
        Returns:
            bool: True if moved. False otherwise.
        """        
        rotation = self.get_current_rotation()
        # check if against left wall
        if any((p%C.GRID_COLUMN_COUNT==0 for p in rotation)):
            return False
        # check if bordering any existing pieces on the left
        if any((grid[p-1] for p in rotation)):
            return False
        # execute translation
        self._rotations = [p-1 for p in self._rotations]
        return True

    def translate_right(self, grid: List[bool]) -> bool:
        """Moves the tetromino to the right one block unless the block is obstructed
        Args:
            grid (List[bool]): 1D array representing the tetris game state.
        Returns:
            bool: True if moved. False otherwise.
        """        
        rotation = self.get_current_rotation()
        # check if against right wall
        if any((p+1%C.GRID_COLUMN_COUNT==0 for p in rotation)):
            return False
        # check if bordering any existing pieces on the right
        if any((grid[p+1] for p in rotation)):
            return False
        # execute translation
        self._rotations = [p+1 for p in self._rotations]
        return True
    
    def translate_up(self, grid: List[bool]) -> bool:
        """Moves the tetromino up one block unless the block is obstructed
        Args:
            grid (List[bool]): 1D array representing the tetris game state.
        Returns:
            bool: True if moved. False otherwise.
        """        
        rotation = self.get_current_rotation()
        # check if against top
        if any((p+C.GRID_COLUMN_COUNT>=len(grid) for p in rotation)):
            return False
        # check if bordering any existing pieces on the top
        if any((grid[p+C.GRID_COLUMN_COUNT] for p in rotation)):
            return False
        # execute translation
        self._rotations = [p+C.GRID_COLUMN_COUNT for p in self._rotations]
        return True
    
    def translate_down(self, grid: List[bool]) -> bool:
        """Moves the tetromino down one block unless the block is obstructed
        Args:
            grid (List[bool]): 1D array representing the tetris game state.
        Returns:
            bool: True if moved. False otherwise.
        """        
        rotation = self.get_current_rotation()
        # check if against bottom
        if any((p-C.GRID_COLUMN_COUNT<0 for p in rotation)):
            return False
        # check if bordering any existing pieces on the bottom
        if any((grid[p-C.GRID_COLUMN_COUNT] for p in rotation)):
            return False
        # execute translation
        self._rotations = [p-C.GRID_COLUMN_COUNT for p in self._rotations]
        self._moved = True
        return True

    def has_moved(self):
        return self._moved

class IShape(Tetromino):
    def __init__(self):
        rotations = [
            193, 194, 195, 196,  # rot 0
            205, 195, 185, 175,  # rot 90
            183, 184, 185, 186,  # rot 180
            204, 194, 184, 174   # rot 270
        ]
        super().__init__(rotations)

    def rotate(self):
        pass

class OShape(Tetromino):
    pass

class JShape(Tetromino):
    pass

class LShape(Tetromino):
    pass

class TShape(Tetromino):
    pass

class SShape(Tetromino):
    pass

class ZShape(Tetromino):
    pass
