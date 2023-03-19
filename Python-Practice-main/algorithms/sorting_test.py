# Wesley Murray
# 2/10/2021
# This file is for unit testing lastStoneWeight.

import unittest
import sorting as Sort
import random

class TestSorting(unittest.TestCase):

    #test quicksort algorithm
    def test_quicksort(self):
        print("Testing Quicksort")
        self.__test_sort(Sort.quicksort)
    
    def test_mergesort(self):
        print("Testing Mergesort")
        self.__test_sort(Sort.mergesort)
    
    def __test_sort(self,sortFunc):
        #edge cases
        self.assertEqual(sortFunc([]),[])
        self.assertEqual(sortFunc(None),None)
        self.assertEqual(sortFunc([1]),[1])
        self.assertEqual(sortFunc([1]),[1])
        self.assertEqual(sortFunc([1,2,1]),[1,1,2])
        self.assertEqual(sortFunc([65,39,86]),[39,65,86])
        self.assertEqual(sortFunc([30,75,69,16,47]),[16,30,47,69,75])
        self.assertEqual(sortFunc([60,80,74,8,77,1,60,33,70,29]),[1,8,29,33,60,60,70,74,77,80])

        #normal cases
        for _ in range(20):
            temp=[]
            tempSort=[]
            before=[]
            testLen = random.randint(1,10)
            for _ in range(0,testLen):
                randNum = random.randint(0,100)
                before.append(randNum)
                temp.append(randNum)
                tempSort.append(randNum)
            tempSort.sort()
            sortFunc(temp)
            self.assertEqual(temp,tempSort)

if __name__ == '__main__':
    random.seed(3)
    unittest.main()