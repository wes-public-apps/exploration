from time import sleep

from app import constants as C
from app import tetrominoes

class Tetris:
    def __init__(self):
        self._score = 0
        self._grid = [False] * (C.GRID_COLUMN_COUNT * C.GRID_ROW_COUNT)
        self._current_tetromino: tetrominoes.Tetromino = None
    
    def calculate_score(self):
        # if single line 100 pts (tetris zone)
        # if 4 lines 800 pts (tetris)
        # sequential tetris is 1200 pts
        pass
    
    def next(self) -> bool:
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
    tetrominoes_list = [
        tetrominoes.IShape(),
        tetrominoes.OShape(),
        tetrominoes.JShape(),
        tetrominoes.LShape(),
        tetrominoes.SShape(),
        tetrominoes.ZShape(),
        tetrominoes.TShape(),
    ]
    for tetromino in tetrominoes_list:
        print('-'*100)
        for i in range(tetromino._num_rotations):
            print(f"Rotation {i}")
            rotation = tetromino.get_rotation(i)
            print(rotation)
            rotation = [
                (p-C.SPAWN_POINT)
                for p in rotation
            ]
            print(rotation)
            rotation2 = [
                18 in rotation,
                19 in rotation,
                20 in rotation,
                21 in rotation,
                -2 in rotation,
                -1 in rotation,
                0 in rotation,
                1 in rotation,
                -22 in rotation,
                -21 in rotation,
                -20 in rotation,
                -19 in rotation,
                -42 in rotation,
                -41 in rotation,
                -40 in rotation,
                -39 in rotation,
            ]
            print(rotation2)
            line = ''
            for idx, flag in enumerate(rotation2):
                if idx%4==0:
                    print(line)
                    line=''
                if flag:
                    line += 'X'
                else:
                    line += '-'
            print(line)
main()
                





        