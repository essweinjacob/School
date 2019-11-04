#!/bin/bash

## This script outputs various information 
## Jacob Esswein

## Usage message
if [ $# -eq 0 ]
    then
        echo "Usage Message: Enter a file or the full directory to run this script"
        exit
elif [ $# -eq 1 ]
    then
        echo "Usage Message: Plese enter a full directory to run this script"
        exit

## Name of script
echo `basename "$0"`
##Date and time
date
# Name of user
whoami
# Print current directory
pwd
#print name of unix machine
hostname
## Print login shell
echo $SHELL
#CONTENTS OF THE REQUIRED FILE
echo "Listing of the required directory: "
echo
ls $2
echo
## Number of lines in script
wc -l lines.txt
# Listing of the required directory
for file in .* *; do echo $file; done
#Number of argumens
echo $# arguments
# Calander for October
cal -m October
#Disk USage
du
# Number of users in system
w -h | wc -l
#Time
echo "Current Time: $(date '+%H:%M:%S')"
