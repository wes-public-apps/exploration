# Wesley Murray
# 2/10/2021
# Library for different sorting algorithms

#sort arrays using quicksort algorithm
def quicksort(arr):
    if(arr==None): return None
    return __quickSort(arr,0,len(arr)-1)

#private quicksort helper
def __quickSort(arr,low,high):
    #handle edge/base cases
    if(high-low<1): return arr

    pivotVal=arr[high]
    pivotInd=high

    #arrange values arround the pivot point
    currPos=0
    while(currPos<pivotInd):
        if(arr[currPos]>pivotVal):
            arr.insert(pivotInd+1,arr[currPos])
            del arr[currPos]
            pivotInd-=1
        else:
            currPos+=1

    #quick sort both sides of pivot
    __quickSort(arr,low,pivotInd-1)
    __quickSort(arr,pivotInd+1,high)

    return arr

#sort arrays using merge sort algorithm
def mergesort(arr):
    #handle edge cases
    if arr==None: return None

    __mergesort(arr,0,len(arr)-1)
    return arr

#private merger sort helper method
def __mergesort(arr,left,right):
    #handle base case
    if (right-left)<1: return

    #normal case
    middle = (left+right)//2
    __mergesort(arr,left,middle)
    __mergesort(arr,middle+1,right)
    __merge(arr,left,middle,right)

#sort arrays being merged
def __merge(arr,left,middle,right):
    i=left
    j=middle+1
    k=i
    while i<j and j<=right:
        if arr[i]<arr[j]:
            i+=1
        else:
            arr.insert(k,arr[j])
            j+=1
            i+=1
            del arr[j]
        k+=1
