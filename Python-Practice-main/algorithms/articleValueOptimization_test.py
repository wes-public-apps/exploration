# Wesley Murray
# 2/15/2021
# This file is for testing the program that optimizes article value

import unittest
import articleValueOptimization as avo
import random
import time

class TestArticleValueOptimization(unittest.TestCase):

    #test dynamic programming solution
    def test_dynamicProgramming(self):

        #edge cases
        self.assertEqual(avo.dynamicProgrammingSolution([3,5,6],[1,2,4],2),[])
        self.assertEqual(avo.dynamicProgrammingSolution([3,2],[1,4],2),[1])
        self.assertEqual(avo.dynamicProgrammingSolution([3,9,2,13,5,6],[1,60,4,100,24,0],8),[2,4])
        self.assertEqual(avo.dynamicProgrammingSolution([1,2,3],[10,10,10],6),[0,1,2])
        #not handling ties. if both options are equal it does not matter which one is returned.

        #normal cases
        self.assertEqual(avo.dynamicProgrammingSolution([2,5,2,7],[14,10,11,30],10),[0,3])
        self.assertEqual(avo.dynamicProgrammingSolution([2,5,9,2,7],[14,10,4,11,30],18),[0,1,3,4])
        for _ in range(15):
            pages=[]
            IQ=[]
            numArticles=random.randint(1,20)
            pageLimit=random.randint(1,100)
            for _ in range(numArticles):
                pages.append(random.randint(1,100))
                IQ.append(random.randint(1,100))
            bruteForceRes=avo.bruteForceSolution(pages,IQ,pageLimit)
            dynamicRes=avo.dynamicProgrammingSolution(pages,IQ,pageLimit)
            self.assertEqual(bruteForceRes,dynamicRes)

    def test_greedyByIQ(self):
        #expected failure cases
        pages=[5,5,5,11]
        IQ=[5,5,5,14]
        pageLimit = 15
        self.assertNotEqual(avo.greedyByIQ(pages,IQ,pageLimit),avo.bruteForceSolution(pages,IQ,pageLimit))
        self.assertEqual(avo.greedyByIQ(pages,IQ,pageLimit),[3])

        #edge cases
        self.assertEqual(avo.greedyByIQ([3,5,6],[1,2,4],2),[])
        self.assertEqual(avo.greedyByIQ([3,9,2,13,5,6],[1,60,4,100,24,0],8),[2,4])
        self.assertEqual(avo.greedyByIQ([1,2,3],[10,10,10],6),[0,1,2])

        #normal cases
        self.assertEqual(avo.greedyByIQ([2,5,2,7],[14,10,11,30],10),[0,3])
        self.assertEqual(avo.greedyByIQ([32,18,26,12],[40,12,12,24],32),[0])

        #relative accuracy
        numTestCases=15
        countCorrect=0
        for _ in range(numTestCases):
            pages=[]
            IQ=[]
            numArticles=random.randint(1,20)
            pageLimit=random.randint(1,100)
            for _ in range(numArticles):
                pages.append(random.randint(1,100))
                IQ.append(random.randint(1,100))
            bruteForceRes=avo.bruteForceSolution(pages,IQ,pageLimit)
            greedyRes=avo.greedyByIQ(pages,IQ,pageLimit)
            if(greedyRes==bruteForceRes):
                countCorrect+=1
        print('greedy highest IQ accuracy (%): '+str(countCorrect/numTestCases*100))

    def test_greedyByPage(self):
        #expected failure cases
        pages=[5,5,5,11]
        IQ=[5,5,5,17]
        pageLimit = 15
        self.assertNotEqual(avo.greedyByPage(pages,IQ,pageLimit),avo.bruteForceSolution(pages,IQ,pageLimit))
        self.assertEqual(avo.greedyByPage(pages,IQ,pageLimit),[0,1,2])

        #edge cases
        self.assertEqual(avo.greedyByPage([3,5,6],[1,2,4],2),[])
        self.assertEqual(avo.greedyByPage([3,9,2,13,5,6],[1,60,4,100,24,0],8),[0,2])
        self.assertEqual(avo.greedyByPage([1,2,3],[10,10,10],6),[0,1,2])

        #normal cases
        self.assertEqual(avo.greedyByPage([2,5,2,7],[14,10,11,30],10),[0,1,2])
        self.assertEqual(avo.greedyByPage([32,18,26,12],[40,12,12,24],32),[1,3])

        #relative accuracy
        numTestCases=15
        countCorrect=0
        for _ in range(numTestCases):
            # print('test case: '+str(i))
            pages=[]
            IQ=[]
            numArticles=random.randint(1,20)
            pageLimit=random.randint(1,100)
            for _ in range(numArticles):
                pages.append(random.randint(1,100))
                IQ.append(random.randint(1,100))
            bruteForceRes=avo.bruteForceSolution(pages,IQ,pageLimit)
            greedyRes=avo.greedyByPage(pages,IQ,pageLimit)
            if(greedyRes==bruteForceRes):
                countCorrect+=1
        print('greedy lowest pages accuracy (%): '+str(countCorrect/numTestCases*100))

    def test_greedyByIQPerPage(self):
        #expected failure cases
        pages=[5,5,5,11]
        IQ=[5,5,5,14]
        pageLimit = 15
        self.assertNotEqual(avo.greedyByIQPerPage(pages,IQ,pageLimit),avo.bruteForceSolution(pages,IQ,pageLimit))
        self.assertEqual(avo.greedyByIQPerPage(pages,IQ,pageLimit),[3])

        #edge cases
        self.assertEqual(avo.greedyByIQPerPage([3,5,6],[1,2,4],2),[])
        self.assertEqual(avo.greedyByIQPerPage([3,9,2,13,5,6],[1,60,4,100,24,0],8),[2,4])
        self.assertEqual(avo.greedyByIQPerPage([1,2,3],[10,10,10],6),[0,1,2])

        #normal cases
        self.assertEqual(avo.greedyByIQPerPage([2,5,2,7],[14,10,11,30],10),[0,1,2])
        self.assertEqual(avo.greedyByIQPerPage([32,18,26,12],[40,12,12,24],32),[1,3])

        #relative accuracy
        numTestCases=15
        countCorrect=0
        for _ in range(numTestCases):
            pages=[]
            IQ=[]
            numArticles=random.randint(1,20)
            pageLimit=random.randint(1,100)
            for _ in range(numArticles):
                pages.append(random.randint(1,100))
                IQ.append(random.randint(1,100))
            bruteForceRes=avo.bruteForceSolution(pages,IQ,pageLimit)
            greedyRes=avo.greedyByIQPerPage(pages,IQ,pageLimit)
            if(greedyRes==bruteForceRes):
                countCorrect+=1
        print('greedy IQ density accuracy (%): '+str(countCorrect/numTestCases*100))

    #test brute force solution
    def test_bruteforce(self):
        #edge cases
        self.assertEqual(avo.bruteForceSolution([3,5,6],[1,2,4],2),[])
        self.assertEqual(avo.bruteForceSolution([3,9,2,13,5,6],[1,60,4,100,24,0],8),[2,4])
        self.assertEqual(avo.bruteForceSolution([1,2,3],[10,10,10],6),[0,1,2])
        #not handling ties. if both options are equal it does not matter which one is returned.

        #normal cases
        self.assertEqual(avo.bruteForceSolution([2,5,2,7],[14,10,11,30],10),[0,3])
        self.assertEqual(avo.bruteForceSolution([2,5,9,2,7],[14,10,4,11,30],18),[0,1,3,4])

    #test input validation
    def test_inputValidation(self):
        self.assertFalse(avo.inputValid(None,None,0))
        self.assertFalse(avo.inputValid([],[],0))
        self.assertFalse(avo.inputValid([],[],2))
        self.assertFalse(avo.inputValid([1,3],[4,13,6],2))
        self.assertTrue(avo.inputValid([1,4,3],[4,13,6],2))

if __name__ == '__main__':
    unittest.main()