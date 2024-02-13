# Wesley Murray
# 2/11/2021
# This file is for unit testing the insert algorithms

import unittest
import inserting as Insertion

class TestInserting(unittest.TestCase):

    #test the method that inserts a value into a sorted list 
    #using binary search
    def test_insertInOrderBinary(self):
        self.assertEqual(Insertion.insertInOrderBinary(None,3),[3])
        self.assertEqual(Insertion.insertInOrderBinary([],3),[3])
        self.assertEqual(Insertion.insertInOrderBinary([1,2,4,5,7],3),[1,2,3,4,5,7])
        self.assertEqual(Insertion.insertInOrderBinary([8,10,13],3),[3,8,10,13])
        self.assertEqual(Insertion.insertInOrderBinary([8,10,13],14),[8,10,13,14])

    #test the method that inserts a value into a sorted list 
    def test_insertInOrder(self):
        self.assertEqual(Insertion.insertInOrder(None,3),[3])
        self.assertEqual(Insertion.insertInOrder([],3),[3])
        self.assertEqual(Insertion.insertInOrder([1,2,4,5,7],3),[1,2,3,4,5,7])
        self.assertEqual(Insertion.insertInOrder([8,10,13],3),[3,8,10,13])
        self.assertEqual(Insertion.insertInOrder([8,10,13],14),[8,10,13,14])

if __name__ == '__main__':
    unittest.main()