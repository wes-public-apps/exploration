import unittest

from app import constants as C
from app import tetrominoes


class TestTetrominoes(unittest.TestCase):
    def test_I_rotations(self):
        self.assertTrue(False)

    def test_O_rotations(self):
        self.assertTrue(False)

    def test_J_rotations(self):
        self.assertTrue(False)

    def test_L_rotations(self):
        self.assertTrue(False)

    def test_S_rotations(self):
        self.assertTrue(False)

    def test_Z_rotations(self):
        self.assertTrue(False)

    def test_T_rotations(self):
        self.assertTrue(False)


def sanity_check():
    """Helper method that quickly visualizes a tetris object."""
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
        print("-" * 50 + tetromino.name + "-" * 50)
        for i in range(tetromino._num_rotations):
            print(f"Rotation {i}")
            line = tetromino.get_visualization_str(i)
            print(line)


if __name__ == "__main__":
    sanity_check()
