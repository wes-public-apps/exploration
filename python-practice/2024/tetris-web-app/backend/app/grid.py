from dataclasses import dataclass
from functools import lru_cache


@lru_cache
def map_to_grid(index: int, num_src_cols: int, num_dest_cols: int) -> int:
    """transform function that maps an index onto the grid
    Args:
        index (int): position to map
        num_src_cols (int): number of columns in source grid
        num_dest_cols (int): number of columns in dest grid
    Returns:
        int: mapped index
    """
    assert index >= 0, "Negative indices not supported"
    col = index % num_src_cols
    rows = int(index / num_src_cols) + 1
    col_offset = int((num_dest_cols - num_src_cols) / 2)
    return rows * num_dest_cols + col_offset + col


@lru_cache
def map_from_grid(index, num_src_cols, num_dest_cols) -> int:
    """transform function that maps an index from the src grid to dest grid
    Args:
        index (int): position to map
        num_src_cols (int): number of columns in source grid
        num_dest_cols (int): number of columns in dest grid
    Returns:
        int: mapped index
    """
    assert index >= num_src_cols + 1, "Negative indices not supported"
    col_offset = int((num_src_cols - num_dest_cols) / 2)
    col = (index % num_src_cols) - col_offset
    rows = int(index / num_src_cols) - 1
    return rows * num_dest_cols + col


@dataclass
class Grid:
    col_count: int
    row_count: int
    spawn_point: int

    def __post_init__(self):
        self.raw_col_count = self.col_count + 2
        self.raw_row_count = self.row_count + 2
        self.raw_spawn_point = map_to_grid(
            self.spawn_point, self.col_count, self.raw_col_count
        )
        self.raw_length = self.raw_col_count * self.raw_row_count

        # make a grid where there are invisible rows at top and bottom
        # and invisible columns on each end
        self._positions = [False] * (self.raw_row_count * self.raw_col_count)
        assert len(self._positions) == self.raw_length, "invalid length"
        top_offset = (self.raw_row_count - 1) * self.raw_col_count
        for i in range(self.raw_col_count):
            self._positions[i] = True
            self._positions[top_offset + i] = True
        for i in range(self.raw_row_count):
            self._positions[i * self.raw_col_count] = True
            self._positions[i * self.raw_col_count + self.raw_col_count - 1] = True

    def is_position_allowed(self, index: int) -> bool:
        """Checks is the provided raw position is an allowed location by ensuring it is within
        grid bounds and that position is not already occupied.
        Args:
            index (int): position tracked as index to validate
        Returns:
            bool: True if position is available. False otherwise.
        """
        return not (index < 0 or index > self.raw_length or self._positions[index])

    def set_position(self, index: int, value: bool) -> None:
        """Sets the value of the grid block located at index. Index is not the raw position but
        rather the position on the theoretical view region.
        Args:
            index (int): position of grid block to set
            value (bool): value to assign grid block
        """
        ind = map_to_grid(index, self.col_count, self.raw_col_count)
        self._positions[ind] = value

    def get_position(self, index: int) -> bool:
        """Retrieves the value of the grid block located at index. Index is not the raw position
        but rather the position on the theoretical view region.
        Args:
            index (int): position of grid block value to retrieve
        Returns:
            bool: value assigned to the grid position
        """
        ind = map_to_grid(index, self.col_count, self.raw_col_count)
        return self._positions[ind]

    def get_visualization_str(self) -> str:
        """Helper method that generates a representation of the grid as a string.
        Returns:
            str: grid representation as a string
        """
        grid_str = ""
        for i in range(self.raw_row_count - 1, -1, -1):
            start = self.raw_col_count * i
            end = start + self.raw_col_count
            grid_str += (
                str(i)
                + ": "
                + "".join(["X" if p else "-" for p in self._positions[start:end]])
            )
            grid_str += "\n"
        return grid_str

    def __getitem__(self, index) -> bool:
        return self._positions[index]

    def __setitem__(self, key, value) -> bool:
        self._positions[key] = value
