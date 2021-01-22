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
    counter += mergeSort(left).comparisions
    counter += mergeSort(right).comparisions
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

# getData
def getData(numbers,algo):
    data = []
    numberOfTestCases = 0
    testCases = []
    sampleSpaceSize = 1
    while numberOfTestCases != 100:
        random.shuffle(numbers)
        sampleSpaceSize = random.randint(1,1000)
        if sampleSpaceSize not in testCases:
            testCases.append(sampleSpaceSize)
            startIndex = random.randint(0,len(numbers)-sampleSpaceSize)
            sampleSpace = numbers[startIndex:startIndex+sampleSpaceSize]
            if algo == 1:
                avg = selectionSort(sampleSpace)
                best = selectionSort(sampleSpace)
                sampleSpace.reverse()
                worst = selectionSort(sampleSpace)
            elif algo == 2:
                avg = bubbleSort(sampleSpace)
                best = bubbleSort(sampleSpace)
                sampleSpace.reverse()
                worst = bubbleSort(sampleSpace)
            elif algo == 3:
                avg = insertionSort(sampleSpace)
                best = insertionSort(sampleSpace)
                sampleSpace.reverse()
                worst = insertionSort(sampleSpace)
            elif algo == 4:
                avg = mergeSort(sampleSpace)
                best = mergeSort(sampleSpace)
                sampleSpace.reverse()
                worst = mergeSort(sampleSpace)
            data.append(timeComplexity(avg,best,worst))
            numberOfTestCases += 1
    
    getComparisonCSV(data)
    getGraph()
    
    return 1

