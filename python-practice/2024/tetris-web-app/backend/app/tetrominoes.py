from enum import Enum
from typing import List

from app import constants as C

class Rotation(Enum):
    original = 0
    ninety = 1
    one_eighty = 2
    two_seventy = 3

class Tetromino:
    def __init__(self, rotations, num_rotations=C.NUM_ROTATIONS):
        self._current_rotation = Rotation.original
        self._rotations: List[int] = rotations
        self._moved = False
        self._num_rotations = num_rotations

    def rotate(self, grid: List[bool]) -> bool:
        """Complete the rotation logic for this tetromino. If the resulting rotation is illegal
        then ignore.
        Returns:
            bool: True if rotation successful. False otherwise.
        """        
        temp_rotation = (self._current_rotation + 1) % self._num_rotations
        temp_rotation_shape = self.get_rotation(temp_rotation)
        if any((p<0 or p>len(grid) or grid[p] for p in temp_rotation_shape)):
            return False
        else:
            self._current_rotation = temp_rotation
            return True

    def get_rotation(self, rotation) -> List[int]:
        """Gets the slice of the 1D array intended to track the current rotation.
        Returns:
            List[int]: List of positions representing the current block on the grid.
        """        
        start_ind = rotation * C.NUM_ROTATIONS
        return self._rotations[start_ind:start_ind + C.NUM_BLOCKS]

    def translate_left(self, grid: List[bool]) -> bool:
        """Moves the tetromino to the left one block unless the block is obstructed
        Args:
            grid (List[bool]): 1D array representing the tetris game state.
        Returns:
            bool: True if moved. False otherwise.
        """        
        rotation = self.get_rotation(self._current_rotation)
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
        rotation = self.get_rotation(self._current_rotation)
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
        rotation = self.get_rotation(self._current_rotation)
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
        rotation = self.get_rotation(self._current_rotation)
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
        ref = C.SPAWN_POINT
        rotations = [
            ref-2, ref-1, ref, ref+1,  # rot 0
            ref+C.ROFFSETS[0], ref, ref-C.ROFFSETS[0], ref-C.ROFFSETS[1],  # rot 90
        ]
        super().__init__(rotations, num_rotations=2)


class OShape(Tetromino):
    def __init__(self):
        ref = C.SPAWN_POINT
        rotations = [ref-1, ref, ref-1-C.ROFFSETS[0], ref-C.ROFFSETS[0]]
        super().__init__(rotations, num_rotations=1)

class JShape(Tetromino):
    def __init__(self):
        ref = C.GRID_COLUMN_COUNT * C.GRID_ROW_COUNT - int(C.GRID_COLUMN_COUNT / 2) + 1  # # Row 20 Col 6
        rotations = [
            ref-1, ref, ref+1, ref+1-C.ROFFSETS[0],  # rot 0
            ref-C.ROFFSETS[0], ref, ref+C.ROFFSETS[0], ref+C.ROFFSETS[0]+1,  # rot 90
            ref-1+C.ROFFSETS[0], ref-1, ref, ref+1,  # rot 180
            ref-1-C.ROFFSETS[0], ref-C.ROFFSETS[0], ref, ref+C.ROFFSETS[0],  # rot 270
        ]
        super().__init__(rotations, num_rotations=4)

class LShape(Tetromino):
    def __init__(self):
        ref = C.SPAWN_POINT
        rotations = [
            ref-1, ref, ref+1, ref+1-C.ROFFSETS[0],  # rot 0
            ref-C.ROFFSETS[0], ref, ref+C.ROFFSETS[0], ref+1+C.ROFFSETS[0],  # rot 90
            ref-1, ref, ref+1, ref+1+C.ROFFSETS[0],  # rot 180
            ref-1+C.ROFFSETS[0], ref+C.ROFFSETS[0], ref, ref-C.ROFFSETS[0],  # rot 270
        ]
        super().__init__(rotations, num_rotations=4)

class TShape(Tetromino):
    def __init__(self):
        ref = C.SPAWN_POINT
        rotations = [
            ref-1, ref, ref+1, ref-C.ROFFSETS[0],  # rot 0
            ref+C.ROFFSETS[0], ref, ref-C.ROFFSETS[0], ref+1,  # rot 90
            ref-1, ref, ref+C.ROFFSETS[0], ref+1,  # rot 180
            ref-1, ref, ref-C.ROFFSETS[0], ref+C.ROFFSETS[0],  # rot 270
        ]
        super().__init__(rotations, num_rotations=4)

class SShape(Tetromino):
    def __init__(self):
        ref = C.SPAWN_POINT
        rotations = [
            ref, ref+1, ref-C.ROFFSETS[0], ref-1-C.ROFFSETS[0],  # rot 0
            ref+C.ROFFSETS[0], ref, ref+1, ref+1-C.ROFFSETS[0],  # rot 90
        ]
        super().__init__(rotations, num_rotations=2)

class ZShape(Tetromino):
    def __init__(self):
        ref = C.SPAWN_POINT
        rotations = [
            ref-1, ref, ref-C.ROFFSETS[0], ref+1-C.ROFFSETS[0],  # rot 0
            ref, ref-C.ROFFSETS[0], ref+1, ref+1+C.ROFFSETS[1],  # rot 90
        ]
        super().__init__(rotations, num_rotations=2)
