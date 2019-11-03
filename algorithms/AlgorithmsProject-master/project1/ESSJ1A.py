def main():
    userNum = -1        #Initilaize user input variable and set it to -1
    while userNum < 0:      #Verification loop to make sure user inputs a valid number
        userNum = int(input("Enter a positive number: "))
        if userNum < 0:
            print("Invalid number")
    print(fib(userNum))     #Run code

def fib(userNum):
    if userNum == 0:        #First fib number is 0
        return 0
    elif userNum == 1:      #Second fib bumber is 1
        return 1
    elif userNum == 2:      #Third fib number is 1
        return 1
    else:
        return(fib(userNum - 1) + fib(userNum - 2))     #Fib equation with recursion

main()
