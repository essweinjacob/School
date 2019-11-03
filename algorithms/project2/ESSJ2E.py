#Merge Sort
import random
import time

def main():
    # Variables used
    arrSize = int(input("How large would you like the array to be? ")) # Get user input for size of array

    #Random Array
    array = []
    randomArray(array, arrSize)
    start = time.time() 
    mergeSort(array)
    end = time.time()
    print("Merge sort time for ", arrSize, " elements of a random array: ", end-start)

    # Sorted Array
    array = []
    randomArray(array, arrSize)
    start = time.time() 
    mergeSort(array)
    end = time.time()
    print("Merge sort time for ", arrSize, " elements of a sorted array: ", end-start)

    # Semi-Sorted Array
    array = []
    randomArray(array, arrSize)
    start = time.time() 
    mergeSort(array)
    end = time.time()
    print("Merge sort time for ", arrSize, " elements of a semi sorted array: ", end-start)

    

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

def mergeSort(array):
    if len(array) > 1:
        middle = len(array) // 2 # Find middle of array using integer division ( wont return a decimal number)
        leftArray = array[:middle]
        rightArray = array[middle:]

        mergeSort(leftArray)
        mergeSort(rightArray)

        i = 0
        j = 0
        k = 0

        while (i < len(leftArray) and j < len(rightArray)):
            if (leftArray[i] < rightArray[j]):
                array[k] = leftArray[i]
                i += 1
            else:
                array[k] = rightArray[j]
                j += 1
            k += 1

        while i < len(leftArray):
            array[k] = leftArray[i]
            i += 1
            k += 1
        
        while j < len(rightArray):
            array[k] = rightArray[j]
            j += 1
            k += 1

main()
