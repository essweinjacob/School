#!/bin/bash
#
# Jacob Brandt
# 
#

if [ $# -eq 0 ]; then

    echo "Usage Message: Please enter a file and/or the a full directory to run this script"
    exit

elif [ $# -eq 1 ]; then

    echo "Usage Message: Please enter a full directory to run this script"
    exit

fi


#Name of script
echo "Name of script: $0"
echo

#Current date and time
echo "Current date and time: $(date '+%m/%d/%Y %H:%M:%S')"
echo

#The name of the user
echo "Name of User: $USER"
echo

#The name of current working directory;
echo "Name of Current Working Directory: $PWD"
echo

#The name of login shell
echo "Name of Login Shell: $SHELL"
echo

#The name of UNIX machine
echo "Name of UNIX Machine: $(uname)"
echo

#Contents of the Required File
echo "Contents of the $1:"
echo
cat $1
echo

#Number of Text Lines in the File
echo "Number of Text Lines in $1: $(wc -l < $1)"
echo

#Listing of the required directory
echo "Listing of the Required Directory: "
echo
ls $2
echo

#Total number of parameters of the script
echo "Total Number of Parameters of the Script: $#"
echo 

#Calendar for October of the current year
echo "Calendar for October for this year: "
echo
cal -m oct    

#Disk usage
echo "Disk Usage: "
echo
du
echo

#Current Number of Users in the System
echo "Current Number of Users in the System:"
echo
who
echo

#Current time
echo "Current Time: $(date '+%H:%M:%S')"
