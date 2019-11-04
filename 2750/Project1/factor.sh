#! /bin/bash

## This script with take a users number and will output the smallest prime number, if the number itself is
## prime then it will display that number

## Jacob Esswein

echo "Enter a number between 10-100"
read userNum
if [[ "$userNum" -lt 10 || "$userNum" -gt 100 ]]
    then
        echo "You did not enter a valid number"
else
    numFacs=`factor $userNum | wc -w`
    if [[ "$numFacs" -gt 2 ]]
        then
            if [[ $((userNum%2)) -eq 0 ]]
                then
                    echo "The smallest prime is 2"
            else
                counter=1
                declare -a factorArray
                index=0

                while [ $counter -lt $userNum ]
                    do
                        if [ $(($userNum % $counter)) -eq 0 ]
                            then
                                factorArray[index]=$counter
                                index=$(($index + 1))
                        fi

                        counter=$(($counter + 1))
                    done
                    #Minor "feature" happening here that I dont understand
                if [ ${#factorArray[*]} -eq 1]
                    then
                        echo "This is the smalles prime factor!"
                else
                    echo "The smallest factor is ${factorArray[1]}"
                fi
            fi
    else
        echo "The number is prime"
    fi
fi
