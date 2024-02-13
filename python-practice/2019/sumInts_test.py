# Wesley Murray
# 2/9/2021
# Unit test for sum-ints.py

#import libraries
import unittest
import sys
import sumInts as si

class TestSumInts(unittest.TestCase):

    #define globals for unit tests
    def setUp(self):
        si.START=0
        si.STOP=0

    #test arg validation
    def test_arg_validation(self):
        #number of args
        sys.argv = ['test.py']
        self.assertEqual(si.commandLineArgValidation(),"Error: Provide exacly two arguments.", "Failed to catch too few args.")
        sys.argv = ['test.py',1,2,3]
        self.assertEqual(si.commandLineArgValidation(),"Error: Provide exacly two arguments.", "Failed to catch too many args.")
        #invalid types
        sys.argv = ['test.py','a','2']
        self.assertEqual(si.commandLineArgValidation(),"Error: The provided arguments are not integers.", "Failed to catch invalid type.")
        sys.argv = ['test.py','1','B']
        self.assertEqual(si.commandLineArgValidation(),"Error: The provided arguments are not integers.", "Failed to catch invalid type.")
        sys.argv = ['test.py','1','3.02']
        self.assertEqual(si.commandLineArgValidation(),"Error: The provided arguments are not integers.", "Failed to catch invalid type.")
        #valid case
        sys.argv = ['test.py','1','2']
        self.assertEqual(si.commandLineArgValidation(),None, "A valid config got rejected.")
        #reorder case
        sys.argv = ['test.py','3','2']
        self.assertEqual(si.commandLineArgValidation(),None, "A valid config got rejected.")
        self.assertEqual(si.START,2)
        self.assertEqual(si.STOP,3)

    #test range summer
    def test_range_sum(self):
        self.assertEqual(si.summer(1,1),1,"Did not handle start and stop being the same.")
        self.assertEqual(si.summer(1,3),6,"Should be 6")

if __name__ == '__main__':
    unittest.main()