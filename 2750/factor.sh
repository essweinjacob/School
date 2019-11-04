#/bin/bash
#
# Jacob Brandt
# 
#
# This Bash shell script prompts a user to enter an integer n from 10 to 100. 
# It then finds the smallest (prime) factor for that number.
# If the number has no factors other than itself, it will output “This number is prime”.

echo "Please enter a number between 10-100"
read userInput

if [ $userInput -lt 10 ]; then
    echo "Usage: Please enter a number in the range."
    exit
elif [ $userInput -gt 100 ]; then
    echo "Usage: Please enter a number in the range."
    exit
fi    

if [ $(($userInput % 2)) -eq 0 ]; then
 
    echo "The smallest factor is 2"
    exit
fi

counter=1
declare -a factorArray
index=0

while [ $counter -lt $userInput ]; do

    if [ $(($userInput % $counter)) -eq 0 ]; then
        factorArray[index]=$counter
        index=$(($index + 1))
    fi

    counter=$(($counter + 1))

done

if [ ${#factorArray[*]} -eq 1 ]; then
    echo "This number is the smallest prime factor!"
else
    echo "The smallest factor is ${factorArray[1]}"
fi

