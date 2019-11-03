# Insertion sort
import random
import time

def main():
    #arrSize = int(input("How large would you like the array to be? ")) # Get user input for size of array

    # Random Array
    array = []
    randomArray(array, 1000)
    start = time.time() 
    insertSort(array, 1000)
    end = time.time()
    print("Time for Insert sort of 1000 random elements: ", end-start)

    array = []
    randomArray(array, 10000)
    start = time.time() 
    insertSort(array, 10000)
    end = time.time()
    print("Time for Insert sort of 10000 random elements: ", end-start)

    array = []
    randomArray(array, 100000)
    start = time.time() 
    insertSort(array, 100000)
    end = time.time()
    print("Time for Insert sort of 100000 random elements: ", end-start)

    #Sorted Array
    array = []
    sortedArray(array, 1000)
    start = time.time() 
    insertSort(array, 1000)
    end = time.time()
    print("Time for Insert sort of 1000 sorted elements: ", end-start)

    array = []
    sortedArray(array, 10000)
    start = time.time() 
    insertSort(array, 10000)
    end = time.time()
    print("Time for Insert sort of 10000 sorted elements: ", end-start)

    array = []
    sortedArray(array, 100000)
    start = time.time() 
    insertSort(array, 100000)
    end = time.time()
    print("Time for Insert sort of 100000 sorted elements: ", end-start)

    # Semi-Sorted Array
    array = []
    semiSortedArray(array, 1000)
    start = time.time() 
    insertSort(array, 1000)
    end = time.time()
    print("Time for Insert sort of 1000 semi-sorted elements: ", end-start)

    array = []
    semiSortedArray(array, 10000)
    start = time.time() 
    insertSort(array, 10000)
    end = time.time()
    print("Time for Insert sort of 10000 semi-sorted elements: ", end-start)

    array = []
    semiSortedArray(array, 100000)
    start = time.time() 
    insertSort(array, 100000)
    end = time.time()
    print("Time for Insert sort of 100000 semi-sorted elements: ", end-start)


def insertSort(array, arrSize):
    for i in range(len(array)):
        index = array[i]

        j = i - 1
        while (j >= 0 and index < array[j]):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = index

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