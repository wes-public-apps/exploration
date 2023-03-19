# Wesley Murray
# 2/11/2021
# This file is for insertion algorithms

#simple insert
#O(n)
def insertInOrder(arr,val):
    #handle edge cases
    if(arr==None): return [val]

    #handle normal cases
    ind=0
    arr.append(val)
    while(arr[ind]<val): ind+=1
    if(ind<len(arr)-1): 
        arr.insert(ind,val)
        del arr[len(arr)-1]
    
    return arr

#insert using binary search logic
#O(log2n)
def insertInOrderBinary(arr,val):
    #handle edge cases
    if(arr==None): 
        arr=[val]
        return arr
    if(arr==[]):
        arr.append(val) 
        return arr

    #handle normal cases
    arrLen=len(arr)
    start=0
    end=arrLen-1
    midPoint=0
    while end!=start:
        midPoint=(end+start)//2

        #exit if val is equal to array value in question
        if(arr[midPoint]==val):
            break
        
        #determine array section to check next
        if(arr[midPoint]<val):
            start=midPoint+1
        else:
            end=midPoint-1

    if arr[start]>val:
        arr.insert(start,val)
    else:
        arr.insert(start+1,val)

    return arr