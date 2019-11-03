# Quick Sort
import random
import time
import sys

def main():
    sys.setrecursionlimit(1000000)
    # Variables used
    arrSize = int(input("How large would you like the array to be? ")) # Get user input for size of array

    #Random Array
    array = []
    randomArray(array, arrSize)
    start = time.time() 
    quickSort(array, 0, len(array) - 1)
    end = time.time()
    print("Quick sort for", arrSize, " elements of random array: ", end-start)

    #Sorted Array
    array = []
    sortedArray(array, arrSize)
    start = time.time() 
    quickSort(array, 0, len(array) - 1)
    end = time.time()
    print("Quick sort for", arrSize, " elements of sorted array: ", end-start)

    #Semi-Sorted Array
    array = []
    semiSortedArray(array, arrSize)
    start = time.time() 
    quickSort(array, 0, len(array) - 1)
    end = time.time()
    print("Quick sort for", arrSize, " elements of semi-sorted array: ", end-start)

def randomArray(array, arrSize):
    for _ in range(1, arrSize):
        array.append(random.randint(0,10000))
    return array

def sortedArray(array, arrSize):
    if(arrSize < 100000):
        for i in range(1, arrSize):
            array.append(i)
    else:
        for i in range(1,10000):
            for j in range(1,10):
                array.append(i)
    return array

def semiSortedArray(array, arrSize):
    if(arrSize < 100000):
        for i in range(1, arrSize):
            if(i % 10 == 0):
               array.append(random.randint(0,10000))
            else: 
                array.append(i)
    else:
        for i in range(1,10):
            for j in range(1,10000):
                if(j % 10 == 0):
                    array.append(random.randint(0,10000))
                else:
                    array.append(i)
    return array

def pivotElements(array,low,high):
    i = (low - 1)
    pivot = array[high]
    
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return( i + 1)

def quickSort(array, low, high):
    if low < high:
        partIndex = pivotElements(array, low, high)

        quickSort(array, low, partIndex - 1)
        quickSort(array, partIndex + 1, high)

main()