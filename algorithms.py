from helper import *

# Insertion Sort
def insertionSort(n):
    counter = 0
    start = time.time()
    for i in range(1,len(n)):
        key = n[i]
        j = i-1
        while j >= 0:
            counter += 1
            if(n[j] > key):
                n[j+1] = n[j]
                j -= 1
            else:
                break
        n[j+1] = key
    end = time.time()
    runningTime = round(end-start,5)
    return sortedList(n,counter,runningTime)

# Merge Sort
def merge(left,right,original):
    counter = 0
    i = j = k = 0 
    while(i < len(left) and j < len(right)):
        if(left[i] <= right[j]):
            counter += 1
            original[k] = left[i]
            i += 1
        else:
            counter += 1
            original[k] = right[j]
            j += 1
        k += 1
    while(i < len(left)):
        original[k] = left[i]
        i += 1
        k += 1
    while(j < len(right)):
        original[k] = right[j]
        j += 1
        k += 1
    return counter

def mergeSort(n):
    counter = 0
    if len(n) == 1:
        return sortedList(n,0,0)
    start = time.time()
    left = n[0:len(n)//2]
    right = n[len(n)//2:]
    counter += mergeSort(left).comparisons
    counter += mergeSort(right).comparisons
    counter += merge(left,right,n)
    end = time.time()
    runningTime = round(end-start)
    return sortedList(n,counter,runningTime)

# Selection Sort
def selectionSort(n):
    start = time.time()
    counter = 0
    l = len(n)
    for i in range(0,l-1,1):
        swapIndex = i
        for j in range(i+1,l,1):
            counter += 1
            if(n[j] < n[swapIndex]):
                swapIndex = j
        if(swapIndex != i):
            n[i],n[swapIndex] = n[swapIndex],n[i]
    end = time.time()
    runningTime = round(end-start,5)
    return sortedList(n,counter,runningTime)


# Bubble Sort
def bubbleSort(n):
    start = time.time()
    counter = 0
    l = len(n)
    for i in range(l-1):
        for j in range(l-i-1):
            counter += 1
            if(n[j] > n[j+1]):
                n[j], n[j+1] = n[j+1], n[j]
    end = time.time()
    runningTime = round(end-start,5)
    return sortedList(n,counter,runningTime)

# Quick Sort
def quickSort(A,p,r):
    comparison = 0
    start = time.time()
    if p < r:
        fromPartition = partition(A,p,r) 
        q = fromPartition[0]
        comparison += fromPartition[1]
        comparison += quickSort(A,p,q-1).comparisons
        comparison += quickSort(A,q+1,r).comparisons
    end = time.time()
    runningTime = round(end - start)
    return sortedList(A,comparison,runningTime)
    

def partition(A,p,r):
    # toExchange = random.randint(p,r)
    # A[toExchange],A[r] = A[r],A[toExchange]
    comparison = 0
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            comparison += 1
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1,comparison

# Heap Sort
class heap:
    def __init__(self,h):
        self.h = h
        self.heapSize = len(self.h)
    
    def __str__(self):
        return str(self.h)

def buildMaxHeap(A):
    comparision = 0
    for i in range((A.heapSize - 1)//2, -1, -1):
        comparision += maxHeapify(A,i)
    return comparision

def maxHeapify(A, i):
    comparisons = 0
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if(left < A.heapSize and A.h[left] > A.h[i]):
        largest = left
    
    if(right < A.heapSize and A.h[right] > A.h[largest]):
        largest = right
    
    if(largest != i):
        comparisons += 1
        temp = A.h[i]
        A.h[i] = A.h[largest]
        A.h[largest] = temp
        comparisons += maxHeapify(A,largest)
    return comparisons

def heapSort(A):
    comparisons = 0
    start = time.time()
    comparisons += buildMaxHeap(A)
    for i in range(A.heapSize -1, -1 ,-1):
        A.h[i], A.h[0] = A.h[0], A.h[i]
        A.heapSize -= 1
        comparisons += maxHeapify(A,0)
    end = time.time()
    runningTime = round(end-start)
    return sortedList(A.h,comparisons,runningTime)