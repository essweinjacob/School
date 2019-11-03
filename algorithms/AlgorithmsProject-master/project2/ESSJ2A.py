#Selection Sort
import random
import time

def main():
    # Variables used
    #arrSize = int(input("How large would you like the array to be? ")) # Get user input for size of array

    # Random Arrays
    array = []
    randomArray(array, 1000)
    start = time.time() 
    selectionSort(array)
    end = time.time()
    print("Time for Selection sort of 1000 random elements: ", end-start)

    array = []
    randomArray(array, 10000)
    start = time.time() 
    selectionSort(array)
    end = time.time()
    print("Time for Selection sort of 10000 random elements: ", end-start)

    array = []
    randomArray(array, 100000)
    start = time.time() 
    selectionSort(array)
    end = time.time()
    print("Time for Selection sort of 100000 random elements: ", end-start)

    # Sorted Array
    array = []
    sortedArray(array, 1000)
    start = time.time() 
    selectionSort(array)
    end = time.time()
    print("Time for Selection sort of 1000 sorted elements: ", end-start)

    array = []
    sortedArray(array, 10000)
    start = time.time() 
    selectionSort(array)
    end = time.time()
    print("Time for Selection sort of 10000 sorted elements: ", end-start)

    array = []
    sortedArray(array, 100000)
    start = time.time() 
    selectionSort(array)
    end = time.time()
    print("Time for Selection sort of 100000 sorted elements: ", end-start)

    # Semi-Sorted Array
    array = []
    semiSortedArray(array, 1000)
    start = time.time() 
    selectionSort(array)
    end = time.time()
    print("Time for Selection sort of 1000 semi sorted elements: ", end-start)

    array = []
    semiSortedArray(array, 10000)
    start = time.time() 
    selectionSort(array)
    end = time.time()
    print("Time for Selection sort of 10000 semi sorted elements: ", end-start)

    array = []
    semiSortedArray(array, 100000)
    start = time.time() 
    selectionSort(array)
    end = time.time()
    print("Time for Selection sort of 100000 semi sorted elements: ", end-start)


def selectionSort(array):
        # Go through elements of array
    for i in range(len(array)):
        # Find smallest element in array
        minIndex = i
        for j in range(i+1, len(array)):
            if array[minIndex] > array[j]:
                minIndex = j
    
        # Swap elements
        array[i], array[minIndex] = array[minIndex], array[i]

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

main()

