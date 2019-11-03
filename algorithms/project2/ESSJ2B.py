# Insertion sort
import random
import time

def main():
    arrSize = int(input("How large would you like the array to be? ")) # Get user input for size of array

    # Random Array
    array = []
    randomArray(array, arrSize)
    start = time.time() 
    insertSort(array, arrSize)
    end = time.time()
    print("Time for Insert sort of ", arrSize, " random elements: ", end-start)

    #Sorted Array
    array = []
    sortedArray(array, arrSize)
    start = time.time() 
    insertSort(array, arrSize)
    end = time.time()
    print("Time for Insert sort of ", arrSize ,"sorted elements: ", end-start)

    # Semi-Sorted Array
    array = []
    semiSortedArray(array, arrSize)
    start = time.time() 
    insertSort(array, arrSize)
    end = time.time()
    print("Time for Insert sort of ", arrSize, " semi-sorted elements: ", end-start)



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