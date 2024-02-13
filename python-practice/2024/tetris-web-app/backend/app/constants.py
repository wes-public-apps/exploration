GRID_COLUMN_COUNT = 10  # 0 row is bottom
GRID_ROW_COUNT = 20  # 0 col is left
NUM_ROTATIONS = 4  # most common number of block rotations
NUM_BLOCKS = 4
ROFFSETS = [
    GRID_ROW_COUNT,
    GRID_ROW_COUNT * 2,
]
SPAWN_POINT = GRID_COLUMN_COUNT * GRID_ROW_COUNT - int(GRID_COLUMN_COUNT / 2) + 1