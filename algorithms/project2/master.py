import random
import time

def main():
    # Variables used
    arrSize = int(input("How large would you like the array to be? ")) # Get user input for size of array

    for _ in range(0, 3):
        # Random Arrays
        array = []
        randomArray(array, arrSize)
        start = time.time() 
        selectionSort(array)
        end = time.time()
        print("Time for Selection sort of ", arrSize, " random elements: ", end-start)

        # Sorted Array
        array = []
        sortedArray(array, arrSize)
        start = time.time() 
        selectionSort(array)
        end = time.time()
        print("Time for Selection sort of", arrSize, " sorted elements: ", end-start)

        # Semi-Sorted Array
        array = []
        semiSortedArray(array, arrSize)
        start = time.time() 
        selectionSort(array)
        end = time.time()
        print("Time for Selection sort of ", arrSize, " semi sorted elements: ", end-start)

    for _ in range(0, 3):
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

    for _ in range(0, 3):
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

    for _ in range(0, 3):
        # Random
        array = []
        randomArray(array, arrSize)
        start = time.time() 
        quickSort
        end = time.time()
        print("Time for Quick Sort sort of ", arrSize, " random elements: ", end-start)

        # Sorted
        array = []
        sortedArray(array, arrSize)
        start = time.time() 
        quickSort
        end = time.time()
        print("Time for Quick Sort sort of ", arrSize, " sorted elements: ", end-start)

        # Semi Sorted
        array = []
        semiSortedArray(array, arrSize)
        start = time.time() 
        quickSort
        end = time.time()
        print("Time for Quick Sort sort of ", arrSize, " semi-sorted elements: ", end-start)

    for _ in range(0, 3):
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
        

def insertSort(array, arrSize):
    for i in range(len(array)):
        index = array[i]

        j = i - 1
        while (j >= 0 and index < array[j]):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = index

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