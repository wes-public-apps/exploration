# Validate against original tetris rules
# original roation - https://tetris.wiki/Original_Rotation_System#:~:text=The%20Original%20Rotation%20System%20is,piece%20is%20one%20block%20higher


import unittest

from app import constants as C
from app import tetrominoes
from app.grid import Grid


class TestOriginalTetrominoes(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # fix grid size for testing purposes
        cls.grid = Grid(10, 20, 195)

    def test_I_initialization(self):
        """validate the I tetromino initializes in the correct location"""
        tetro = tetrominoes.IShape(self.grid)
        actual_pos = tetro.current_position
        actual_pos.sort()
        expected_pos = [193, 194, 195, 196]
        self.assertEqual(actual_pos, expected_pos)

    def test_O_inialization(self):
        """validate the O tetromino initializes in the correct location"""
        tetro = tetrominoes.OShape(self.grid)
        actual_pos = tetro.current_position
        actual_pos.sort()
        expected_pos = [184, 185, 194, 195]
        expected_pos.sort()
        self.assertEqual(actual_pos, expected_pos)

    def test_J_inialization(self):
        """validate the J tetromino initializes in the correct location"""
        tetro = tetrominoes.JShape(self.grid)
        actual_pos = tetro.current_position
        actual_pos.sort()
        expected_pos = [186, 194, 195, 196]
        self.assertEqual(actual_pos, expected_pos)

    def test_L_inialization(self):
        """validate the L tetromino initializes in the correct location"""
        tetro = tetrominoes.LShape(self.grid)
        actual_pos = tetro.current_position
        actual_pos.sort()
        expected_pos = [184, 194, 195, 196]
        self.assertEqual(actual_pos, expected_pos)

    def test_S_inialization(self):
        """validate the S tetromino initializes in the correct location"""
        tetro = tetrominoes.SShape(self.grid)
        actual_pos = tetro.current_position
        actual_pos.sort()
        expected_pos = [184, 185, 195, 196]
        self.assertEqual(actual_pos, expected_pos)

    def test_Z_inialization(self):
        """validate the Z tetromino initializes in the correct location"""
        tetro = tetrominoes.ZShape(self.grid)
        actual_pos = tetro.current_position
        actual_pos.sort()
        expected_pos = [185, 186, 194, 195]
        self.assertEqual(actual_pos, expected_pos)

    def test_T_inialization(self):
        """validate the T tetromino initializes in the correct location"""
        tetro = tetrominoes.TShape(self.grid)
        actual_pos = tetro.current_position
        actual_pos.sort()
        expected_pos = [185, 194, 195, 196]
        self.assertEqual(actual_pos, expected_pos)

    def test_valid_I_rotations(self):
        """Validate all of the I tetrominoe rotations given enough space."""
        grid = Grid(10, 20, 95)

        # test using I shape
        tetro = tetrominoes.IShape(grid)
        self.assertTrue(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 1)
        actual = tetro.current_position
        actual.sort()
        self.assertEqual(actual, [75, 85, 95, 105])
        self.assertTrue(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 0)
        actual = tetro.current_position
        actual.sort()
        self.assertEqual(actual, [93, 94, 95, 96])
        # add an extra rotation to ensure this is cyclical
        self.assertTrue(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 1)
        actual = tetro.current_position
        actual.sort()
        self.assertEqual(actual, [75, 85, 95, 105])

    @unittest.skip("Not implemented yet")
    def test_valid_O_rotations(self):
        """Validate all of the O tetrominoe rotations given enough space."""
        pass

    @unittest.skip("Not implemented yet")
    def test_valid_J_rotations(self):
        """Validate all of the J tetrominoe rotations given enough space."""
        pass

    @unittest.skip("Not implemented yet")
    def test_valid_L_rotations(self):
        """Validate all of the L tetrominoe rotations given enough space."""
        pass

    def test_valid_T_rotations(self):
        """Validate all of the T tetrominoe rotations given enough space."""
        grid = Grid(10, 20, 95)
        # test using T shape
        tetro = tetrominoes.TShape(grid)
        self.assertTrue(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 1)
        actual = tetro.current_position
        actual.sort()
        self.assertEqual(actual, [85, 95, 96, 105])
        self.assertTrue(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 2)
        actual = tetro.current_position
        actual.sort()
        self.assertEqual(actual, [94, 95, 96, 105])
        self.assertTrue(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 3)
        actual = tetro.current_position
        actual.sort()
        self.assertEqual(actual, [85, 94, 95, 105])
        self.assertTrue(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 0)
        actual = tetro.current_position
        actual.sort()
        self.assertEqual(actual, [85, 94, 95, 96])
        # add an extra rotation to ensure this is cyclical
        self.assertTrue(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 1)
        actual = tetro.current_position
        actual.sort()
        self.assertEqual(actual, [85, 95, 96, 105])

    @unittest.skip("Not implemented yet")
    def test_valid_S_rotations(self):
        """Validate all of the S tetrominoe rotations given enough space."""
        pass

    @unittest.skip("Not implemented yet")
    def test_valid_Z_rotations(self):
        """Validate all of the Z tetrominoe rotations given enough space."""
        pass

    def test_top_block_rotation(self):
        """validate rotation is rejected at the top of the board"""
        grid = Grid(10, 20, 195)

        ## Using I Shape
        # Reject vertical rotation
        tetro = tetrominoes.IShape(grid)  # initializes in the top row
        self.assertEqual(tetro._current_rotation, 0)
        self.assertFalse(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 0)

        # Reject horizontal rotation
        tetro = tetrominoes.IShape(Grid(10, 20, 185))
        self.assertEqual(tetro._current_rotation, 0)
        self.assertTrue(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 1)
        tetro._rotations = [
            p + 20 for p in tetro._rotations
        ]  # must create unreal situation by shifting up beyond top of grid
        self.assertFalse(tetro.rotate())

        ## Using T Shape
        tetro = tetrominoes.TShape(grid)  # initializes in the top row
        self.assertEqual(tetro._current_rotation, 0)
        self.assertFalse(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 0)

    def test_left_wall_blocks_rotation(self):
        """validate rotation rejected when no room to the left"""
        grid = Grid(10, 20, 185)

        ## Using IShape
        # Reject vertical rotation - Impossible no need to test
        # Reject horizontal rotation
        tetro = tetrominoes.IShape(grid)  # initializes in the top row - 1
        self.assertEqual(tetro._current_rotation, 0)
        self.assertTrue(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 1)
        tetro._rotations = [
            p - 5 for p in tetro._rotations
        ]  # shift shape all the way to column 0
        self.assertFalse(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 1)

        ## Using TShape
        tetro = tetrominoes.IShape(grid)  # initializes in the top row - 1
        self.assertEqual(tetro._current_rotation, 0)
        self.assertTrue(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 1)
        tetro._rotations = [
            p - 5 for p in tetro._rotations
        ]  # shift shape all the way to column 0
        self.assertFalse(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 1)

    def test_right_wall_blocks_rotation(self):
        """validate rotation rejected when no room to the right"""
        grid = Grid(10, 20, 185)

        ## Using IShape
        # Reject vertical rotation - Impossible no need to test
        # Reject horizontal rotation
        tetro = tetrominoes.IShape(grid)  # initializes in the top row - 1
        self.assertEqual(tetro._current_rotation, 0)
        self.assertTrue(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 1)
        tetro._rotations = [
            p + 4 for p in tetro._rotations
        ]  # shift shape all the way to column 9
        print(tetro.current_position, flush=True)
        print(tetro._rotations, flush=True)
        self.assertFalse(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 1)

        ## Using TShape
        tetro = tetrominoes.IShape(grid)  # initializes in the top row - 1
        self.assertEqual(tetro._current_rotation, 0)
        for _ in range(3):
            self.assertTrue(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 3)
        tetro._rotations = [
            p + 4 for p in tetro._rotations
        ]  # shift shape all the way to column 9
        self.assertFalse(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 3)

    def test_bottom_blocks_rotation(self):
        """validate rotation rejected when no room at bottom"""
        grid = Grid(10, 20, 5)

        ## Using IShape
        # Reject vertical rotation
        tetro = tetrominoes.IShape(grid)  # initializes in the bottom row
        self.assertEqual(tetro._current_rotation, 0)
        self.assertFalse(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 0)

        # Reject horizontal rotation
        tetro = tetrominoes.IShape(Grid(10, 20, 45))
        self.assertEqual(tetro._current_rotation, 0)
        self.assertTrue(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 1)
        tetro._rotations = [
            p - 60 for p in tetro._rotations
        ]  # must create unreal situation by shifting beyond bottom of grid
        self.assertFalse(tetro.rotate())

        ## Using TShape
        tetro = tetrominoes.TShape(
            Grid(10, 20, 15)
        )  # initializes in the bottom row + 1
        self.assertEqual(tetro._current_rotation, 0)
        for _ in range(2):
            self.assertTrue(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 2)
        tetro._rotations = [
            p - 10 for p in tetro._rotations
        ]  # shift shape all the way to bottom row
        self.assertFalse(tetro.rotate())
        self.assertEqual(tetro._current_rotation, 2)

    def test_existing_block_blocks_rotation(self):
        """validate rotation rejected when there is a block in the way"""
        grid = Grid(10, 20, 95)

        ## Using IShape
        # check each possible blocking position individually
        tetro = tetrominoes.IShape(grid)
        for i in (115, 105, 95, 85):
            tetro._grid[i] = True
            self.assertFalse(tetro.rotate())
            self.assertEqual(tetro._current_rotation, 0)
            tetro._grid[i] = False
        self.assertTrue(tetro.rotate())
        for i in (103, 104, 105, 106):
            tetro._grid[i] = True
            self.assertFalse(tetro.rotate())
            self.assertEqual(tetro._current_rotation, 1)
            tetro._grid[i] = False

        ## Using TShape
        tetro = tetrominoes.IShape(grid)
        for i in (85, 95, 96, 105):
            tetro._grid[i] = True
            self.assertFalse(tetro.rotate())
            self.assertEqual(tetro._current_rotation, 0)
            tetro._grid[i] = False
        self.assertTrue(tetro.rotate())
        for i in (94, 95, 96, 105):
            tetro._grid[i] = True
            self.assertFalse(tetro.rotate())
            self.assertEqual(tetro._current_rotation, 1)
            tetro._grid[i] = False
        self.assertTrue(tetro.rotate())
        for i in (85, 94, 95, 105):
            tetro._grid[i] = True
            self.assertFalse(tetro.rotate())
            self.assertEqual(tetro._current_rotation, 2)
            tetro._grid[i] = False
        self.assertTrue(tetro.rotate())
        for i in (85, 94, 95, 96):
            tetro._grid[i] = True
            self.assertFalse(tetro.rotate())
            self.assertEqual(tetro._current_rotation, 3)
            tetro._grid[i] = False

    @unittest.skip("Seems redundant to I and T tests")
    def test_O_rotations(self):
        # check all rotations given valid space
        # check rotation rejected when no room at top
        # check rotation rejected when no room to the left
        # check rotation rejected when no room to the right
        # check rotation rejected when no room at bottom
        # check rotation rejected when there is a block in the way
        self.assertTrue(False)

    @unittest.skip("Seems redundant to I and T tests")
    def test_J_rotations(self):
        # check all rotations given valid space
        # check rotation rejected when no room at top
        # check rotation rejected when no room to the left
        # check rotation rejected when no room to the right
        # check rotation rejected when no room at bottom
        # check rotation rejected when there is a block in the way
        self.assertTrue(False)

    @unittest.skip("Seems redundant to I and T tests")
    def test_L_rotations(self):
        # check all rotations given valid space
        # check rotation rejected when no room at top
        # check rotation rejected when no room to the left
        # check rotation rejected when no room to the right
        # check rotation rejected when no room at bottom
        # check rotation rejected when there is a block in the way
        self.assertTrue(False)

    @unittest.skip("Seems redundant to I and T tests")
    def test_S_rotations(self):
        # check all rotations given valid space
        # check rotation rejected when no room at top
        # check rotation rejected when no room to the left
        # check rotation rejected when no room to the right
        # check rotation rejected when no room at bottom
        # check rotation rejected when there is a block in the way
        self.assertTrue(False)

    @unittest.skip("Seems redundant to I and T tests")
    def test_Z_rotations(self):
        # check all rotations given valid space
        # check rotation rejected when no room at top
        # check rotation rejected when no room to the left
        # check rotation rejected when no room to the right
        # check rotation rejected when no room at bottom
        # check rotation rejected when there is a block in the way
        self.assertTrue(False)

    @unittest.skip("Seems redundant to I and T tests")
    def test_T_rotations(self):
        # check all rotations given valid space
        # check rotation rejected when no room at top
        # check rotation rejected when no room to the left
        # check rotation rejected when no room to the right
        # check rotation rejected when no room at bottom
        # check rotation rejected when there is a block in the way
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
        for rotation in tetrominoes.Rotation:
            print(f"Rotation {rotation.value}")
            line = tetromino.get_visualization_str(rotation)
            print(line)


if __name__ == "__main__":
    # sanity_check()
    unittest.main()
