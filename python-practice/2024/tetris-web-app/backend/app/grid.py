from dataclasses import dataclass
from functools import lru_cache


@lru_cache
def map_to_grid(index: int, num_src_cols: int, num_dest_cols) -> int:
    assert index >= 0, "Negative indices not supported"
    col = index % num_src_cols
    rows = int(index / num_src_cols)
    col_offset = (num_dest_cols - num_src_cols) / 2
    return rows * num_dest_cols + rows * col_offset * 2 + col_offset + col


@lru_cache
def map_from_grid(index, num_src_cols, num_dest_cols) -> int:
    assert index >= 0, "Negative indices not supported"
    col = index % num_src_cols
    rows = int(index / num_src_cols)
    col_offset = (num_dest_cols - num_src_cols) / 2
    return rows * num_dest_cols - col_offset + col


@dataclass
class Grid:
    viewed_col_count: int
    viewed_row_count: int
    viewed_spawn_point: int

    def __post_init__(self):
        self.col_count = self.viewed_col_count + 2
        self.row_count = self.viewed_row_count + 2
        self.spawn_point = (
            int(self.viewed_spawn_point / self.viewed_col_count) * self.col_count
            + 1
            + (self.viewed_spawn_point % self.viewed_col_count)
        )
        # make a grid where there are invisible rows at top and bottom
        # and invisible columns on each end
        self._positions = [False] * (self.row_count * self.col_count)
        top_offset = (self.row_count - 1) * self.col_count
        for i in range(self.col_count):
            self._positions[i] = True
            self._positions[top_offset + i] = True
        for i in range(self.row_count):
            self._positions[i * self.col_count] = True
            self._positions[i * self.col_count + self.col_count - 1] = True

        self._positions = [False] * (self.row_count * self.col_count)

        self._length = self.row_count * self.col_count

    def is_position_not_allowed(self, index) -> bool:
        return index < 0 or index > self._length or self._positions[index]

    def _index_map(self, index) -> int:
        return 2 * int(index / self.col_count) + 1 + index

    def __getitem__(self, index) -> int:
        ind = map_to_grid(index, self.viewed_col_count, self.col_count)
        return self._positions[ind]

    def __setitem__(self, key, value) -> None:
        ind = map_to_grid(key, self.viewed_col_count, self.col_count)
        self._positions[ind] = value

    def __len__(self):
        return self._length
