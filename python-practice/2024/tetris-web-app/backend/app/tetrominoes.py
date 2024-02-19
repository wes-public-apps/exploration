from typing import List

from app import constants as C
from app.grid import Grid, map_from_grid


class Tetromino:
    def __init__(
        self,
        name: str,
        rotations: List[int],
        grid: Grid,
        num_rotations=4,
    ):
        self._grid = grid
        self._rotations: List[int] = rotations
        self._num_rotations = num_rotations

        self._moved_down = False
        self._current_rotation = 0

        self.name = name

    @property
    def current_viewed_position(self) -> List[int]:
        """Gets the slice of the 1D array intended to track the current rotation.
        Returns:
            List[int]: List of positions representing the current block on the grid.
        """
        return [map_from_grid(p, 12, 10) for p in self.current_position]

    @property
    def current_position(self) -> List[int]:
        """Gets the slice of the 1D array intended to track the current rotation.
        Returns:
            List[int]: List of positions representing the current block on the grid.
        """
        return self.get_rotation_position(self._current_rotation)

    def rotate(self) -> bool:
        """Complete the rotation logic for this tetromino. If the resulting rotation is illegal
        then ignore.
        Returns:
            bool: True if rotation successful. False otherwise.
        """
        target_rotation = (self._current_rotation + 1) % self._num_rotations
        target_position = self.get_rotation_position(target_rotation)
        # check if proposed change is allowed
        if any((self._grid.is_position_not_allowed(p) for p in target_position)):
            return False
        else:
            # execute change
            self._current_rotation = target_rotation
            return True

    def get_rotation_position(self, rotation: int) -> List[int]:
        """Gets the slice of the 1D array intended to track the current rotation.
        Args:
            rotation (int): shape rotation id
        Returns:
            List[int]: List of positions representing the current block on the grid.
        """
        assert (
            rotation < self._num_rotations
        ), f"Invalid rotation provided. Got {rotation}. Expected 0-{self._num_rotations-1}"
        start_ind = rotation * C.NUM_BLOCKS
        return self._rotations[start_ind : start_ind + C.NUM_BLOCKS]

    def translate_left(self) -> bool:
        """Moves the tetromino to the left one block unless the block is obstructed
        Returns:
            bool: True if moved. False otherwise.
        """
        rotation = self.get_rotation_position(self._current_rotation)
        # check if proposed change is allowed
        if any((self._grid.is_position_not_allowed(p - 1) for p in rotation)):
            return False
        else:
            # execute translation
            self._rotations = [p - 1 for p in self._rotations]
            return True

    def translate_right(self) -> bool:
        """Moves the tetromino to the right one block unless the block is obstructed
        Returns:
            bool: True if moved. False otherwise.
        """
        rotation = self.get_rotation_position(self._current_rotation)
        # check if proposed change is allowed
        if any((self._grid.is_position_not_allowed(p + 1) for p in rotation)):
            return False
        else:
            # execute translation
            self._rotations = [p + 1 for p in self._rotations]
            return True

    def translate_up(self) -> bool:
        """Moves the tetromino up one block unless the block is obstructed
        Returns:
            bool: True if moved. False otherwise.
        """
        rotation = self.get_rotation_position(self._current_rotation)
        # check if proposed change is allowed
        if any(
            (
                self._grid.is_position_not_allowed(p + self._grid.col_count)
                for p in rotation
            )
        ):
            return False
        else:
            # execute translation
            self._rotations = [p + self._grid.col_count for p in self._rotations]
            return True

    def translate_down(self) -> bool:
        """Moves the tetromino down one block unless the block is obstructed
        Returns:
            bool: True if moved. False otherwise.
        """
        rotation = self.get_rotation_position(self._current_rotation)
        # check if proposed change is allowed
        if any(
            (
                self._grid.is_position_not_allowed(p - self._grid.col_count)
                for p in rotation
            )
        ):
            return False
        else:
            # execute translation
            self._rotations = [p - self._grid.col_count for p in self._rotations]
            self._moved_down = True
            return True

    def has_moved_down(self):
        return self._moved_down

    def get_visualization_str(self, rotation: int) -> str:
        print(self._rotations)
        col_pos = [p % self._grid.col_count for p in self._rotations]
        row_pos = [int(p / self._grid.col_count) for p in self._rotations]
        print(col_pos, row_pos)
        min_col = min(col_pos)
        max_col = max(col_pos)
        min_row = min(row_pos)
        max_row = max(row_pos)
        print(min_col, min_row)
        start_ind = rotation * C.NUM_BLOCKS
        rotation_cols = col_pos[start_ind : start_ind + C.NUM_BLOCKS]
        rotation_rows = row_pos[start_ind : start_ind + C.NUM_BLOCKS]
        print(rotation_cols, rotation_rows)
        rotation_cols = [c - min_col for c in rotation_cols]
        rotation_rows = [r - min_row for r in rotation_rows]
        print(rotation_cols, rotation_rows)
        grid = [
            ["-", "-", "-", "-"],
            ["-", "-", "-", "-"],
            ["-", "-", "-", "-"],
            ["-", "-", "-", "-"],
        ]
        for i in range(4):
            grid[3 - rotation_rows[i]][rotation_cols[i]] = "X"
        return "\n".join(["".join(r) for r in grid])


class IShape(Tetromino):
    def __init__(self, grid: Grid):
        ref = grid.spawn_point
        roff = grid.col_count
        roff2 = grid.col_count * 2
        rotations = [
            ref - 2,
            ref - 1,
            ref,
            ref + 1,  # rot 0
            ref + roff,
            ref,
            ref - roff,
            ref - roff2,  # rot 90
        ]
        super().__init__("I", rotations, grid, num_rotations=2)


class OShape(Tetromino):
    def __init__(self, grid: Grid):
        ref = grid.spawn_point
        roff = grid.col_count
        rotations = [ref - 1, ref, ref - 1 - roff, ref - roff]
        super().__init__("O", rotations, grid, num_rotations=1)


class JShape(Tetromino):
    def __init__(self, grid: Grid):
        ref = grid.spawn_point
        roff = grid.col_count
        rotations = [
            ref - 1,
            ref,
            ref + 1,
            ref + 1 - roff,  # rot 0
            ref - roff,
            ref,
            ref + roff,
            ref + roff + 1,  # rot 90
            ref - 1 + roff,
            ref - 1,
            ref,
            ref + 1,  # rot 180
            ref - 1 - roff,
            ref - roff,
            ref,
            ref + roff,  # rot 270
        ]
        super().__init__("J", rotations, grid, num_rotations=4)


class LShape(Tetromino):
    def __init__(self, grid: Grid):
        ref = grid.spawn_point
        roff = grid.col_count
        rotations = [
            ref - 1,
            ref,
            ref + 1,
            ref - 1 - roff,  # rot 0
            ref - roff,
            ref,
            ref + roff,
            ref + 1 + roff,  # rot 90
            ref - 1,
            ref,
            ref + 1,
            ref + 1 + roff,  # rot 180
            ref - 1 + roff,
            ref + roff,
            ref,
            ref - roff,  # rot 270
        ]
        super().__init__("L", rotations, grid, num_rotations=4)


class TShape(Tetromino):
    def __init__(self, grid: Grid):
        ref = grid.spawn_point
        roff = grid.col_count
        rotations = [
            ref - 1,
            ref,
            ref + 1,
            ref - roff,  # rot 0
            ref + roff,
            ref,
            ref - roff,
            ref + 1,  # rot 90
            ref - 1,
            ref,
            ref + roff,
            ref + 1,  # rot 180
            ref - 1,
            ref,
            ref - roff,
            ref + roff,  # rot 270
        ]
        super().__init__("T", rotations, grid, num_rotations=4)


class SShape(Tetromino):
    def __init__(self, grid: Grid):
        ref = grid.spawn_point
        roff = grid.col_count
        rotations = [
            ref,
            ref + 1,
            ref - roff,
            ref - 1 - roff,  # rot 0
            ref + roff,
            ref,
            ref + 1,
            ref + 1 - roff,  # rot 90
        ]
        super().__init__("S", rotations, grid, num_rotations=2)


class ZShape(Tetromino):
    def __init__(self, grid: Grid):
        ref = grid.spawn_point
        roff = grid.col_count
        rotations = [
            ref - 1,
            ref,
            ref - roff,
            ref + 1 - roff,  # rot 0
            ref,
            ref - roff,
            ref + 1,
            ref + 1 + roff,  # rot 90
        ]
        super().__init__("Z", rotations, grid, num_rotations=2)
