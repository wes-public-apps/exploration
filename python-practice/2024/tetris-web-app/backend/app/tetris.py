import asyncio
from enum import Enum

from app import tetrominoes
from app.grid import Grid


class TetrisEvent(Enum):
    TRANSLATE_LEFT = 0
    TRANSLATE_RIGHT = 1
    SPACEBAR = 2
    TRANSLATE_DOWN = 3


class Tetris:
    SCORE_FACTOR_BY_COUNT = {
        0: 0,
        1: 40,
        2: 100,
        3: 300,
        4: 1200,
    }

    def __init__(self):
        self._score = 0
        self._grid = Grid(10, 20, 195)
        self._current_tetromino: tetrominoes.Tetromino = None
        self._period: float = 1
        self._level = 0

    def calculate_score(self):
        rows_eliminated = self._grid.handle_solid_rows()
        return Tetris.SCORE_FACTOR_BY_COUNT[rows_eliminated] * (self._level + 1)

    def next(self) -> bool:
        if self._current_tetromino.translate_down():
            pass
        else:
            if not self._current_tetromino.has_moved_down():
                return False
            self._score += self.calculate_score()
            self.start_new_cycle()

    async def play(self):
        while self.next():
            asyncio.sleep(self._period)

    def start_new_cycle(self):
        # randomly pick tetromino
        pass

    def handle_event(self, event: TetrisEvent):
        pass


if __name__ == "__main__":
    print("Hello")
