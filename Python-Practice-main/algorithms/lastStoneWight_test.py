# Wesley Murray
# 2/11/2021
# This script is for testing my code for the last rock size problem.

import unittest
import lastStoneWeight as lsw

class LastRockSizeTest(unittest.TestCase):

    #test program that determines final rock size
    def test_rockSize(self):
        self.assertEqual(lsw.determineSizeOfLastRock(None),0)
        self.assertEqual(lsw.determineSizeOfLastRock([]),0)
        self.assertEqual(lsw.determineSizeOfLastRock([7]),7)
        self.assertEqual(lsw.determineSizeOfLastRock([7,7]),0)
        self.assertEqual(lsw.determineSizeOfLastRock([7,3,7]),3)
        self.assertEqual(lsw.determineSizeOfLastRock([7,3,7,1,1]),1)
        self.assertEqual(lsw.determineSizeOfLastRock([2,7,4,1,8,1]),1)

if __name__ == "__main__":
    unittest.main()

