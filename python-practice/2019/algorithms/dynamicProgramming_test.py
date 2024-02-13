# Wesley Murray
# 2/16/2021
# This file is for testing the dynamic programming class and all of its
# supporting classes.

import unittest, logging, sys

from dynamicProgramming import Item,OptimizationProblem,TwoDList

logging.basicConfig(stream=sys.stderr,level=logging.DEBUG) #debug logging is not working like I would like

class TestDynamicProgrammingHelpers(unittest.TestCase):

    def test_ItemClass(self):
        #verify input validation
        self.assertRaises(ValueError,Item,1,"e",2)
        self.assertRaises(ValueError,Item,"e",1,2)
        self.assertRaises(ValueError,Item,1,2,"e")
    
    def test_TwoDListClass(self):
        table=TwoDList(2,2)

        #validate initialization
        self.assertEqual(len(table),4)

        table.replace(0,0,1)
        table.replace(-1,-1,3)
        table.replace(-1,-2,2)

        #validate indexing
        self.assertEqual(table.get(1,0),2)
        self.assertEqual(table.get(1,1),3)
        self.assertEqual(table.get(-2,-2),1)

        #validate col and row limit access
        table=TwoDList(4,8)
        self.assertEqual(table.getNumCols(),8)
        self.assertEqual(table.getNumRows(),4)

class TestDynamicProgramming(unittest.TestCase):
    
    #test ancilary functionality
    def test_OptimizationProblemClass_General(self):
        #Test Input Validation
        self.assertRaises(ValueError,OptimizationProblem.validateInput,None,[1])
        self.assertRaises(ValueError,OptimizationProblem.validateInput,[1],None)
        self.assertRaises(ValueError,OptimizationProblem.validateInput,[],[1])
        self.assertRaises(ValueError,OptimizationProblem.validateInput,[1],[])
        self.assertRaises(ValueError,OptimizationProblem.validateInput,[1,2],[1])
        OptimizationProblem.validateInput([1,2],[1,2.0])
        self.assertRaises(ValueError,OptimizationProblem.createItemCollection,None,[1])
        self.assertRaises(ValueError,OptimizationProblem.createItemCollection,[1,"e"],[1,2])

        #normal cases
        weight=[3,4,5,2]
        value=[2,5,6,1]
        items=OptimizationProblem.createItemCollection(weight,value)
        for i in range(len(value)):
            self.assertEqual(items[i].getCost(),weight[i])
            self.assertEqual(items[i].getValue(),value[i])
            self.assertEqual(items[i].getId(),i)

    #test method that constructs table
    def test_OptimizationProblemClass_Tabulation(self):
        #edge cases
        pass

        #normal cases
        self.__tabulationHelp(self.pbs[0]._createTable,[0,0,0,100])
        self.__tabulationHelp(self.pbs[1]._createTable,[0]*8+[10]*6+[0]+[10]*2+[20]*4+[0]+[10,10]+[20]*3+[30])

    #helper method for testing expected table structure
    def __tabulationHelp(self,tableFunc,expected):
        table=tableFunc()
        for i in range(len(expected)):
            self.assertEqual(table[i],expected[i])

    #test method that constructs table
    def test_OptimizationProblemClass_OptimizedTabulation(self):
        #edge cases
        pass

        #normal cases
        for i in range(len(self.pbs)):
            table=self.pbs[i]._createOptimizedTable({})
            self.assertEqual(self.pbs[i].getMaxValue(),self.pbsExpVal[i])

    #test solver
    def test_OptimizationProblemClass_solve(self):
        #edge case
        pass

        #normal
        logging.debug("")
        logging.debug("Solver. Show calculated solution and expected sibe by side below:")
        for i in range(len(self.pbs)):
            solution=self.pbs[i].solve()
            logging.debug(str(solution)+" "+str(self.pbsExp[i]))
            self.assertEqual(solution,self.pbsExp[i])

    #test memory optimize solver
    def test_OptimizationProblemClass_optimizedSolve(self):
        #edge case
        pass

        #normal
        logging.debug("")
        logging.debug("Optimized Solver. Show calculated solution and expected sibe by side below:")
        for i in range(len(self.pbs)):
            solution=self.pbs[i].optimizedSolve()
            logging.debug(str(solution)+" "+str(self.pbsExp[i]))
            self.assertEqual(solution,self.pbsExp[i])

    #define some common data for testing
    @classmethod
    def setUpClass(self):
        self.pbs=[]
        #create dynamic programming problems
        self.pbs.append(self.__createDP(self,[1],[100],1))
        self.pbs.append(self.__createDP(self,[1,2,3],[10,10,10],6))
        self.pbs.append(self.__createDP(self,[4,1,2,3,1],[2,7,11,11,5],5))
        self.pbs.append(self.__createDP(self,[23,31,29,44,53,38,63,85,89,82],[92,57,49,68,60,43,67,84,87,72],165))
        #define solutions to problems
        self.pbsExp=[
            [0],
            [0,1,2],
            [1,2,4],
            [0,1,2,3,5]
        ]
        self.pbsExpVal=[100,30,23,309]
    
    #helper method for creating a dynamic programming problem instance
    def __createDP(self,costs,values,limit):
        items=OptimizationProblem.createItemCollection(costs,values)
        return OptimizationProblem(items,limit)

if __name__ == '__main__':
    unittest.main()