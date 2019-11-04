#!/bin/bash

## This program will have the user input their first and last name and numbers
## if the average of those numbers is more then 70 then it will display a success message
## if the average is below 70 it will show a failure message
## This does not work with decimals as bash doesnt work with floating decimal points

## Jacob Esswein


name=$1" "$2
average=0

shift 2

for arg in $@; do
    
    average=$(( $average + $arg))

done


average=$(( $average / $# ))

if [ $average -gt 70 ]; then
    echo "Congratulations $name, you passed with an average of $average!"
fi
if [ $average -lt 70 ]; then
    echo "Sorry, $name, but you will have to retake the class! Your average was $average."
fi
