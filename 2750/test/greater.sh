#!/bin/bash

echo "Enter a num"
read num1
echo "Enter a num"
read num2

if [[ $num1 > $num2 ]]
    then
    echo $num1
else
    echo $num2
fi
