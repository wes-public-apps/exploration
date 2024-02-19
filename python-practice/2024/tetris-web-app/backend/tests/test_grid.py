import unittest

from app.grid import Grid, map_to_grid


class TestGrid(unittest.TestCase):

    def test_map_to_grid(self):
        """Validates the map to grid function properly handles mapping the small 2D grid onto the
        larger underlying data object.
        """
        self.assertEqual(map_to_grid(0, 10, 12), 1)
        self.assertEqual(map_to_grid(10, 10, 12), 13)
        self.assertEqual(map_to_grid(20, 10, 12), 25)
        self.assertEqual(map_to_grid(2, 10, 12), 3)
        self.assertEqual(map_to_grid(15, 10, 12), 18)
        self.assertEqual(map_to_grid(26, 10, 12), 31)
        self.assertEqual(map_to_grid(38, 10, 12), 45)
        self.assertEqual(map_to_grid(9, 10, 12), 10)
        self.assertEqual(map_to_grid(19, 10, 12), 22)
        self.assertEqual(map_to_grid(29, 10, 12), 34)

        self.assertRaises(AssertionError, map_to_grid, -1, 10, 12)

    def test_allowed_positions(self):
        """Validates wall boundaries are not allowed positions"""
        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
