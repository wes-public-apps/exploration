# Wesley Murray
# 2/15/2021
# This file is for solving the article value optimization problem.

# The problem:
# You have a list of articles. Each article has a page count and an
# intelligence value. You are given a page limit and must find the 
# combination of articles that maximizes the intelligence value while
# meeting the total page limit constraint.

import math
import sorting as Sort
import dynamicProgramming as DynamicProgramming

#use a greedy algorithm based on highest IQ to determine the best article combination
#O(n log n)
def greedyByIQ(pages,IQ,pageLimit):
    if not inputValid(pages,IQ,pageLimit): return []

    # track article index for sorting
    articleInds=list(range(len(pages)))
    
    #sort list of data by IQ density values to have the highest value first
    IQ,articleInds,pages = [list(pair) for pair in zip(*sorted(zip(IQ,articleInds,pages),reverse=True))]

    # add the most dense material first
    return __buildArticleList(pages,articleInds,pageLimit,len(pages))

#use a greedy algorithm based on lowest page length to determine the best article combination
#O(n log n)
def greedyByPage(pages,IQ,pageLimit):
    if not inputValid(pages,IQ,pageLimit): return []

    # track article index for sorting
    articleInds=list(range(len(pages)))
    
    #sort list of data by IQ density values to have the highest value first
    pages,articleInds = [list(pair) for pair in zip(*sorted(zip(pages,articleInds)))]

    # add the most dense material first
    return __buildArticleList(pages,articleInds,pageLimit,len(pages))

#use a greedy algorithm based on IQ density to determine the best article combination
#O(n log n)
def greedyByIQPerPage(pages,IQ,pageLimit):
    if not inputValid(pages,IQ,pageLimit): return []

    # create list of IQ density per page
    articleInds=[]
    IQperPage=[]
    for i in range(len(pages)):
        IQperPage.append(IQ[i]/pages[i])
        articleInds.append(i)

    #sort list of data by IQ density values to have the highest value first
    IQperPage,articleInds,pages,IQ = [list(pair) for pair in zip(*sorted(zip(IQperPage,articleInds,pages,IQ),reverse=True))]

    # add the most dense material first
    return __buildArticleList(pages,articleInds,pageLimit,len(pages))

def __buildArticleList(pages,articleInds,pageLimit,numArticles):
    articles = []
    numPages=0
    for i in range(numArticles):
        numPages+=pages[i]
        if numPages>pageLimit:
            numPages-=pages[i]
            continue
        articles.append(articleInds[i])
    Sort.quicksort(articles)

    return articles

#This function solves the article value optimization problem using dynamic programming
#This program experiences O(n*m) time complexity but O(m) memory complexity. m is the page limit.
def dynamicProgrammingSolution(pages,IQs,pageLimit):
    if not inputValid(pages,IQs,pageLimit): return []

    items=DynamicProgramming.OptimizationProblem.createItemCollection(pages,IQs)
    problem = DynamicProgramming.OptimizationProblem(items,pageLimit)
    return problem.optimizedSolve()

#This function solves the article value optimization problem using brute force.
#This does not handle ties. That functionality could easily be added but is unnecessary. 
#This algorithm gets very costly as the input size (n) increases. 2^n combinations to check.
#O(2^N)
def bruteForceSolution(pages,IQ,pageLimit):
    if not inputValid(pages,IQ,pageLimit): return []

    numArticles = len(pages)

    #for all possible article combinations
    combination =[0]*numArticles
    maxScore=0
    articles=[]
    while True:
        #score combination
        pageTot=0
        IQTot=0
        for i in range(numArticles):
            if combination[i]:
                pageTot+=pages[i]
                IQTot+=IQ[i]
        
        #record articles if page count is less than limit and score is higher than past
        if pageTot<=pageLimit and IQTot>maxScore:
            maxScore=IQTot
            articles=[]
            for j in range(numArticles): 
                if combination[j]: 
                    articles.append(j)

        # break loop when last combination has been reached
        if sum(combination)==numArticles:
            break

        #create next combination
        ind=0
        while True:
            combination[ind]=(combination[ind]+1)%2
            if combination[ind]==1:
                break
            ind+=1

    return articles

#validate input
def inputValid(pages,IQ,pageLimit):
    #handle nonetypes
    if pages==None or IQ==None: return False

    #handle non matching lengths
    lenIQ=len(IQ)
    lenPages=len(pages)
    if lenPages<1 or lenIQ<1 or lenPages!=lenIQ: return False

    #handle invalid pagelimit
    try: 
        pageLimit=int(pageLimit) 
        if pageLimit<1: return False
    except TypeError: 
        print("invalid page number: "+pageLimit)
        return False

    return True

#helper class to make working with 2D lists easier.
class TwoDList(list):
    #constructor
    def __init__(self,numRows,numCols):
        self.__numRows=numRows
        self.__numCols=numCols
        super().__init__([0]*numRows*numCols)

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