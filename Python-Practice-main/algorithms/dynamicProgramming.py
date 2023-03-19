# Wesley Murray
# 2/16/2021
# This file was created to house dynamic programming utilities.
# This goal is to have a program that can solve any dynamic programming problem.
# It will define a standard template that problems will be transformed into.
# This file contains both my original and optimized solutions.

#Set up the dynamic programming problem
class OptimizationProblem():

    #Create a collection of items to be the input for the problem
    @staticmethod
    def createItemCollection(costs,values):
        OptimizationProblem.validateInput(costs,values)

        items =[]
        for i in range(len(costs)):
            items.append(Item(i,costs[i],values[i]))
        return items

    #Validate problem input data
    @staticmethod
    def validateInput(costs,values):
        if type(costs)!=list or type(values)!=list: raise ValueError("Args must be lists")
        if costs==[] or values==[]: raise ValueError("Args cannot be []")
        if len(costs)!=len(values): raise ValueError("Args cannot be of different length")

    def __init__(self,items,limit):
        self.__items=items
        self.__numItems=len(items)
        self.__limit=limit
        self.__solution=None
        self.__maxValue=0

    #memory optimized tabularization
    #O(n) space complexity
    #O(n*m) time complexity
    def optimizedSolve(self):
        #define a dictionary to store relevant table values so a solution can be reconstructed
        sparseMem={}

        table=self._createOptimizedTable(sparseMem)
        return self._determineOptimizedSolution(table,sparseMem)

    #generate sparse table
    def _createOptimizedTable(self,sparseMem):
        #define a 2D list that only has two rows 
        #only the previous and current row are needed to determine to perform calculations for dynamic programming
        table = TwoDList(2,self.__limit+1)

        #loop over all rows and columns. 
        #There is a row per item and an additional buffer row.
        #Since only two rows are kept in memory, each iteration 
        # the current row starts overwriting the row with oldest edits
        for i in range(1,self.__numItems+1):
            for j in range(1,table.getNumCols()):

                #determine current element value
                valueAbove=table.get((i-1)%2,j)
                valueWithCurrObject=table.get((i-1)%2,j-self.__items[i-1].getCost())+self.__items[i-1].getValue() if j-self.__items[i-1].getCost()>=0 else 0
                table.replace(i%2,j,max(valueAbove,valueWithCurrObject))

                #add relevant elements to the spares memory structure
                if table.get(i%2,j)>table.get(i%2,j-1) and table.get(i%2,j)>table.get((i-1)%2,j): 
                    sparseMem[table.get(i%2,j)]=i
        self.__maxValue=table.get(self.__numItems%2,-1)
        return table
    
    #determine solution from sparse table
    def _determineOptimizedSolution(self,table,sparseMem):
        #construct solution from sparse memory
        value=self.__maxValue
        solution=[]
        while value!=0:
            itemInd = sparseMem[value]-1
            solution.append(itemInd)
            value-=self.__items[itemInd].getValue()
        solution.reverse()
        self.__solution=solution
        return solution

    #solve the dynamic programming problem
    #O(n*m) space complexity
    #O(n*m) time complexity
    def solve(self):
        table=self._createTable()
        return self.determineSolution(table)
    
    #generate a table to solve the problem
    def _createTable(self):
        #use helper class to create a 2D list a 1D
        table = TwoDList(self.__numItems+1,self.__limit+1)
        for i in range(1,table.getNumRows()):
            for j in range(1,table.getNumCols()):
                #determine element value
                valueAbove=table.get(i-1,j)
                valueWithCurrObject=table.get(i-1,j-self.__items[i-1].getCost())+self.__items[i-1].getValue() if j-self.__items[i-1].getCost()>=0 else 0
                table.replace(i,j,max(valueAbove,valueWithCurrObject))
        self.__maxValue=table.get(-1,-1)
        return table

    #retrace steps through table to determine solution
    def determineSolution(self,table):
        solution=[]
        row=-1
        col=-1
        value=table.get(row,col)
        
        #loop until that last possible item that can fit is selected
        while value>0:
            #if the value in the row above is equal move to that element
            if table.get(row-1,col)==value:
                row-=1
                continue
            
            #account for item being included
            solution.append(self.__items[row].getId())
            value-=self.__items[row].getValue()

            #find the next item to include
            while table.get(row,col)!=value: 
                if col%table.getNumCols()!=0:
                    col-=1
                else:
                    row -=1
                    col+=table.getNumCols()-1
                if row<(-table.getNumRows()):
                    value=0
                    break
        #reorder solution.
        solution.reverse()

        self.__solution=solution
        return solution
    
    def getMaxValue(self):
        return self.__maxValue

    def getSolution(self):
        return self.__solution

def isNum(val):
    return type(val)==int or type(val)==float

#create a class to represent items in a dynamic programming problem
class Item():
    def __init__(self,itemId,cost,value):
        #minor input validation
        if not isNum(itemId) or not isNum(cost) or not isNum(value):
            raise ValueError("args must be a number")
             
        self.__id=itemId
        self.__cost=cost
        self.__value=value

    def getCost(self):
        return self.__cost

    def getValue(self):
        return self.__value

    def getId(self):
        return self.__id

#helper class to make working with 2D lists easier.
class TwoDList(list):
    def __init__(self,numRows,numCols):
        self.__numRows=numRows
        self.__numCols=numCols
        super().__init__([0]*numRows*numCols) #initialize 1D list

    #convert 2D index to 1D
    #Support negative indices
    def __2Dto1DIndex(self,row,col):
        adj=0 if col>=0 else self.__numCols
        return row*self.__numCols+adj+col

    #get item from list
    def get(self,row,col):
        return super(TwoDList,self).__getitem__(self.__2Dto1DIndex(row,col))

    #replace item in list
    def replace(self,row,col,val):
        list.__setitem__(self,self.__2Dto1DIndex(row,col),val)

    def getNumCols(self):
        return self.__numCols

    def getNumRows(self):
        return self.__numRows