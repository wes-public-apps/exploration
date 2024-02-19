import logging
import unittest

from app.grid import Grid, map_to_grid, map_from_grid


class TestGrid(unittest.TestCase):

    def test_map_to_grid(self):
        """Validates the map to grid function properly handles mapping the small 2D grid onto the
        larger underlying data object.
        """
        self.assertEqual(map_to_grid(0, 10, 12), 13)
        self.assertEqual(map_to_grid(10, 10, 12), 25)
        self.assertEqual(map_to_grid(20, 10, 12), 37)
        self.assertEqual(map_to_grid(2, 10, 12), 15)
        self.assertEqual(map_to_grid(15, 10, 12), 30)
        self.assertEqual(map_to_grid(26, 10, 12), 43)
        self.assertEqual(map_to_grid(38, 10, 12), 57)
        self.assertEqual(map_to_grid(9, 10, 12), 22)
        self.assertEqual(map_to_grid(19, 10, 12), 34)
        self.assertEqual(map_to_grid(29, 10, 12), 46)

        self.assertEqual(map_to_grid(195, 10, 12), 246)

        self.assertRaises(AssertionError, map_to_grid, -1, 10, 12)

    def test_map_from_grid(self):
        """Validate the map from grid functions properly handles mapping the grid onto the smaller
        view region.
        """
        self.assertEqual(map_from_grid(13, 12, 10), 0)
        self.assertEqual(map_from_grid(25, 12, 10), 10)
        self.assertEqual(map_from_grid(15, 12, 10), 2)
        self.assertEqual(map_from_grid(30, 12, 10), 15)
        self.assertEqual(map_from_grid(43, 12, 10), 26)
        self.assertEqual(map_from_grid(57, 12, 10), 38)
        self.assertEqual(map_from_grid(22, 12, 10), 9)
        self.assertEqual(map_from_grid(34, 12, 10), 19)
        self.assertEqual(map_from_grid(46, 12, 10), 29)

        self.assertEqual(map_from_grid(246, 12, 10), 195)

        self.assertRaises(AssertionError, map_from_grid, -1, 12, 10)
        self.assertRaises(AssertionError, map_from_grid, 10, 12, 10)

    def test_initialization(self):
        """Validate grid initialization"""
        grid = Grid(10, 20, 195)
        for i in (
            list(range(12))
            + list(range(252, 264))
            + list(range(12, 252, 12))
            + list(range(11, 264, 12))
        ):
            self.assertTrue(grid[i])
        for i in range(1, grid.raw_row_count - 1):
            for j in range(i * 12 + 1, i * 12 + 11):
                self.assertFalse(grid[j], msg=f"Index: {j}.")
        logging.debug(grid.get_visualization_str())

    def test_allowed_positions(self):
        """Validates wall boundaries are not allowed positions"""
        grid = Grid(10, 20, 195)
        logging.debug(f"Initial 10x20: \n%s", grid.get_visualization_str())

        for i in (
            list(range(12))
            + list(range(252, 264))
            + list(range(12, 252, 12))
            + list(range(11, 264, 12))
        ):
            self.assertFalse(grid.is_position_allowed(i))
        for i in range(1, grid.raw_row_count - 1):
            for j in range(i * 12 + 1, i * 12 + 11):
                self.assertTrue(
                    grid.is_position_allowed(j),
                    msg=f"Index: {j}. Position should be allowed",
                )

        grid[105] = True
        logging.debug(f"Initial 10x20 + 105: \n%s", grid.get_visualization_str())
        self.assertFalse(grid.is_position_allowed(105))
        self.assertFalse(grid.is_position_allowed(-1))
        self.assertFalse(grid.is_position_allowed(300))


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    unittest.main()
