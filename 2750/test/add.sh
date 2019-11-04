#!/bin/bash

echo "Enter a number"
read num1
echo "Enter a number"
read num2
echo "Enter a number"
read num3
echo "Enter a number"
read num4
echo "Enter a number"
read num5

sum=$(expr $num1 '+' $num2 '+' $num3 '+' $num4 '+' $num5) 
 
echo $sum
