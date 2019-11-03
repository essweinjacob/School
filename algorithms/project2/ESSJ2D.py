# Quick Sort
import random
import time
import sys

def main():
    sys.setrecursionlimit(1000000)
    # Variables used
    arrSize = int(input("How large would you like the array to be? ")) # Get user input for size of array

    array = []
    randomArray(array, arrSize)
    start = time.time() 
    quickSort
    end = time.time()
    print("Time for Quick Sort sort of ", arrSize, " random elements: ", end-start)

    array = []
    sortedArray(array, arrSize)
    start = time.time() 
    quickSort
    end = time.time()
    print("Time for Quick Sort sort of ", arrSize, " random elements: ", end-start)

    array = []
    semiSortedArray(array, arrSize)
    start = time.time() 
    quickSort
    end = time.time()
    print("Time for Quick Sort sort of ", arrSize, " random elements: ", end-start)

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
'''
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
'''

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

main()