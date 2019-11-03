import time

def main():
    var = 0
    x = 35
    file1 = open("recursiveData.txt", "a")
    file1.write(str(x))
    file1.write("\n")
    for _ in range(0,5):
        start = time.time()     # All start and end variables are to track time for execution
        fibIter(x)
        end = time.time()
        file1.write(str(end-start))       #Recursive function call and reporting time
        file1.write("\n")
        var = var + end-start

    avg = var / 5
    file1.write("Average: ")
    file1.write(str(avg))
    file1.write("\n")
    file1.close()
'''
    start = time.time()
    fibIter(x)      
    end = time.time()
    print("Time elapsed for Fibonacii Iterative for", x,": ", end-start)        #Iterative function call and reporting time
'''
#Same code as in parts A and B
def fib(x): 
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return(fib(x - 1) + fib(x - 2))

def fibIter(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x == 2:
        return 1
    elif x == 3:
        return 2
    elif x > 3:
        fn = 0
        fn1 = 1
        fn2 = 2
        for i in range(3, x):
            fn = fn1 + fn2
            fn1 = fn2
            fn2 = fn
        return fn
    else:
        return -1

main()
