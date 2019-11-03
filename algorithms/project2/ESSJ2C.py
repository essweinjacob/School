# Both Bubble sort variation
import random
import time

def main():
    # Variables used
    arrSize = int(input("How large would you like the array to be? ")) # Get user input for size of array

    # Random Array Without swaps counting
    array = []
    randomArray(array, arrSize)
    start = time.time() 
    bubbleSortNoSwapCounting(array)
    end = time.time()
    print("Time for Bubble without swaps counting sort of", arrSize, " random elements: ", end-start)

    # Sorted Array Without swaps counting
    array = []
    sortedArray(array, 1000)
    start = time.time() 
    bubbleSortNoSwapCounting(array)
    end = time.time()
    print("Time for Bubble without swaps counting sort of ", arrSize ," sorted elements: ", end-start)

    # Semi-Sorted Array Without swaps counting
    array = []
    semiSortedArray(array, 1000)
    start = time.time() 
    bubbleSortNoSwapCounting(array)
    end = time.time()
    print("Time for Bubble without swaps counting sort of " , arrSize , " semi-sorted elements: ", end-start)

    #Random Array With swaps counting
    array = []
    randomArray(array, 1000)
    start = time.time() 
    bubbleSortSwapCounting(array)
    end = time.time()
    print("Time for Bubble with swaps counting sort of ", arrSize, " random elements: ", end-start)

    # Sorted Array With swaps counting
    array = []
    sortedArray(array, 1000)
    start = time.time() 
    bubbleSortSwapCounting(array)
    end = time.time()
    print("Time for Bubble with swaps counting sort of ",arrSize," sorted elements: ", end-start)

    # Semi-Sorted Array With swaps counting
    array = []
    semiSortedArray(array, 1000)
    start = time.time() 
    bubbleSortSwapCounting(array)
    end = time.time()
    print("Time for Bubble with swaps counting sort of ",arrSize," semi-sorted elements: ", end-start)


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

def bubbleSortNoSwapCounting(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]
                
    return array


def bubbleSortSwapCounting(array):
    for i in range(len(array)):
        swapped = False

        for j in range(0, len(array) - i -1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if swapped == False:
            break
    
    return array

main()