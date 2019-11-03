def main():

    userNum = -1        #Initialize variable for user input

    while userNum < 0:      #Verification loop for user input
        userNum = int(input("Enter a positive number: "))
        if userNum < 0:
            print("Invalid number")

    
    print(fibIter(userNum))     #fibIter functuion call

def fibIter(userNum):
    if userNum == 0:        #first fib number is 0
        return 0            
    elif userNum == 1:      #Second fib number is 1
        return 1
    elif userNum == 2:      #Third fib number is 1
        return 1
    elif userNum == 3:      #4th fib number is 2
        return 2
    elif userNum > 3:       # Iterative loop for fib sequence
        fn = 0
        fn1 = 1
        fn2 = 2
        for i in range(3, userNum):     #Loop for numbers between 3 and user input
            fn = fn1 + fn2              #Fib sequence definition
            fn1 = fn2                   #Swap
            fn2 = fn
        return fn
    else:
        return -1

main()
