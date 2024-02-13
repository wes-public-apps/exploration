from time import sleep

from app import constants as C
from app.tetrominoes import Tetromino

class Tetris:
    def __init__(self):
        self._score = 0
        self._grid = [False] * (C.GRID_COLUMN_COUNT * C.GRID_ROW_COUNT)
        self._current_tetromino: Tetromino = None
    
    def calculate_score(self):
        # if single line 100 pts (tetris zone)
        # if 4 lines 800 pts (tetris)
        # sequential tetris is 1200 pts
        pass
    
    def next(self) -> bool:
        # sleep for a period (score dependent)
        sleep(1)
        if self._current_tetromino.translate_down():
            self.calculate_score()
            self.update_grid()
        else:
            if not self._current_tetromino.has_moved():
                return False
            self.start_new_cycle()
    
    def update_grid(self):
        # remove solid lines
        pass

    def start_new_cycle(self):
        # randomly pick tetromino
        # determine start location on grid
        pass


    def save(self):
        pass

    def main():
        game = Tetris()
        while game.next():
            