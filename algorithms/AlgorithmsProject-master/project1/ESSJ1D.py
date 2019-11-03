def main():
    #Initialize arrays
    f1 = []     #Think of as f-1
    f2 = []     #Think of as f-2
    fn = []     #Think of as fn
    
    #Fill array with 0s
    for i in range(0,100):
        f1.append(0)
        f2.append(0)
        fn.append(0)

    #Arrays are going to be filled from right to left, make 'first' element in each be 1 
    f1[99] = 1
    f2[99] = 1
    
    while True:     #Recursive loop will go until if statement is reached
        fn = add(f1,f2)
        f1 = f2     #Swaps
        f2 = fn
        if(fn[0] == 8):     #If the 100th digit/first element has been reached/filled
            print("ERROR: 100th digit has been reached")
            break       #Break out of while loop

    print("Sum of array: ", fn)


# This function will add the elements of the two arrays
def add(f1,f2):
    #Create new array fn
    fn = []
    #Fill 100 elements of it wil 0s
    for i in range(0,100):
        fn.append(0)
    
    remainder = 0   #Remainder variable if f2+f1 > 10 we know to carry a number to the left element

    for x in range(len(f1)-1, -1 ,-1):      #for loop, using the length of f1 down to 0
        var = f1[x] + f2[x] + remainder     #var = sum, sum is a keyword in Python, but this is the sum of f1[x], f2[x] and the remainder
        
        fn[x] = var % 10        #Store the mod 10 of the sum in to fn[x]

        if((var/10) < 1):       #Tests for remainder
            remainder = 0

        else:
            remainder = 1
    
    return fn       #Returns the array

main()
