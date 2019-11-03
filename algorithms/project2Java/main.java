import java.util.Random;
import java.util.Arrays;

class main{
    public static void main(String args[]){
        SelectionSort ob = new SelectionSort();
        ob.selectionSort(randomArray(1000));
    }

    // Java program for implementation of Selection Sort 
    class SelectionSort 
    { 
        void selectionSort(int arr[]) 
        { 
            int n = arr.length; 
    
            // One by one move boundary of unsorted subarray 
            for (int i = 0; i < n-1; i++) 
            { 
                // Find the minimum element in unsorted array 
                int min_idx = i; 
                for (int j = i+1; j < n; j++) 
                    if (arr[j] < arr[min_idx]) 
                        min_idx = j; 
    
                // Swap the found minimum element with the first 
                // element 
                int temp = arr[min_idx]; 
                arr[min_idx] = arr[i]; 
                arr[i] = temp; 
            } 
        } 
    }

    class InsertionSort { 
        /*Function to sort array using insertion sort*/
        void insertSort(int arr[]) 
        { 
            int n = arr.length; 
            for (int i = 1; i < n; ++i) { 
                int key = arr[i]; 
                int j = i - 1; 
      
                /* Move elements of arr[0..i-1], that are 
                   greater than key, to one position ahead 
                   of their current position */
                while (j >= 0 && arr[j] > key) { 
                    arr[j + 1] = arr[j]; 
                    j = j - 1; 
                } 
                arr[j + 1] = key; 
            } 
        }
    } 
    
    class BubbleSort 
        { 
            void bubbleSort(int arr[]) 
            { 
                int n = arr.length; 
                for (int i = 0; i < n-1; i++) 
                    for (int j = 0; j < n-i-1; j++) 
                        if (arr[j] > arr[j+1]) 
                        { 
                            // swap arr[j+1] and arr[i] 
                            int temp = arr[j]; 
                            arr[j] = arr[j+1]; 
                            arr[j+1] = temp; 
                        } 
            } 
        }

    class GFG  
    { 
        // An optimized version of Bubble Sort 
        static void bubbleSort(int arr[], int n) 
        { 
            int i, j, temp; 
            boolean swapped; 
            for (i = 0; i < n - 1; i++)  
            { 
                swapped = false; 
                for (j = 0; j < n - i - 1; j++)  
                { 
                    if (arr[j] > arr[j + 1])  
                    { 
                         // swap arr[j] and arr[j+1] 
                        temp = arr[j]; 
                        arr[j] = arr[j + 1]; 
                        arr[j + 1] = temp; 
                        swapped = true; 
                    } 
                } 
          
                // IF no two elements were  
                // swapped by inner loop, then break 
                if (swapped == false) 
                    break; 
            } 
        }
    }

    // Java program for implementation of QuickSort 
    class QuickSort 
    { 
        /* This function takes last element as pivot, 
        places the pivot element at its correct 
        position in sorted array, and places all 
        smaller (smaller than pivot) to left of 
        pivot and all greater elements to right 
        of pivot */
        int partition(int arr[], int low, int high) 
        { 
            int pivot = arr[high];  
            int i = (low-1); // index of smaller element 
            for (int j=low; j<high; j++) 
            { 
                // If current element is smaller than the pivot 
                if (arr[j] < pivot) 
                { 
                    i++; 
    
                    // swap arr[i] and arr[j] 
                    int temp = arr[i]; 
                    arr[i] = arr[j]; 
                    arr[j] = temp; 
                } 
            } 
    
            // swap arr[i+1] and arr[high] (or pivot) 
            int temp = arr[i+1]; 
            arr[i+1] = arr[high]; 
            arr[high] = temp; 
    
            return i+1; 
        } 
    
    
        /* The main function that implements QuickSort() 
        arr[] --> Array to be sorted, 
        low  --> Starting index, 
        high  --> Ending index */
        void quickSort(int arr[], int low, int high) 
        { 
            if (low < high) 
            { 
                /* pi is partitioning index, arr[pi] is  
                now at right place */
                int pi = partition(arr, low, high); 
    
                // Recursively sort elements before 
                // partition and after partition 
                quickSort(arr, low, pi-1); 
                quickSort(arr, pi+1, high); 
            } 
        } 
    }
    
    /* Java program for Merge Sort */
    class MergeSort 
    { 
        // Merges two subarrays of arr[]. 
        // First subarray is arr[l..m] 
        // Second subarray is arr[m+1..r] 
        void merge(int arr[], int l, int m, int r) 
        { 
            // Find sizes of two subarrays to be merged 
            int n1 = m - l + 1; 
            int n2 = r - m; 
    
            /* Create temp arrays */
            int L[] = new int [n1]; 
            int R[] = new int [n2]; 
    
            /*Copy data to temp arrays*/
            for (int i=0; i<n1; ++i) 
                L[i] = arr[l + i]; 
            for (int j=0; j<n2; ++j) 
                R[j] = arr[m + 1+ j]; 
    
    
            /* Merge the temp arrays */
    
            // Initial indexes of first and second subarrays 
            int i = 0, j = 0; 
    
            // Initial index of merged subarry array 
            int k = l; 
            while (i < n1 && j < n2) 
            { 
                if (L[i] <= R[j]) 
                { 
                    arr[k] = L[i]; 
                    i++; 
                } 
                else
                { 
                    arr[k] = R[j]; 
                    j++; 
                } 
                k++; 
            } 
    
            /* Copy remaining elements of L[] if any */
            while (i < n1) 
            { 
                arr[k] = L[i]; 
                i++; 
                k++; 
            } 
    
            /* Copy remaining elements of R[] if any */
            while (j < n2) 
            { 
                arr[k] = R[j]; 
                j++; 
                k++; 
            } 
        } 
    
        // Main function that sorts arr[l..r] using 
        // merge() 
        void mergeSort(int arr[], int l, int r) 
        { 
            if (l < r) 
            { 
                // Find the middle point 
                int m = (l+r)/2; 
    
                // Sort first and second halves 
                mergeSort(arr, l, m); 
                mergeSort(arr , m+1, r); 
    
                // Merge the sorted halves 
                merge(arr, l, m, r); 
            } 
        } 
    }

    // Code for generating arrays
    public static int [] randomArray(int arrSize){

        Random rand = new Random();
        int[] array = new int[arrSize];
        for(int i = 0; i <= array.length; i++){
            array[i] = rand.nextInt();
        }

        return array;
    }

    public static int [] sortedArray(int arrSize){
        int[] array = new int[arrSize];
        if(arrSize < 100000){
            for(int i = 0; i <= array.length; i++){
                array[i] = i;
            }
        }else{
            for(int i = 0; i < 10; i++){
                for(int j = 0; j <= array.length; j++){
                    array[i] = i;
                }
            }
        }
        
        return array;
    }

    public static int[] semiSortedArray(int arrSize){
        Random rand = new Random();

        if(arrSize < 100000){
            for(int i = 0; i <= arrSize; i++){
                if(i % 10 == 0){
                    array[i] = rand.nextInt();
                }else{
                    array[i] = i;
                }
            }
        }else{
            for(int i = 0; i <= 10; i++){
                for(int j = 0; j <= arrSize; j++){
                    if(j % 10 == 0){
                        array[i] = rand.nextInt();
                    }else{
                        array[i] = i;
                    }
                }
            }
        }
    }
}