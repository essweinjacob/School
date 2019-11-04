Script started on Wed 17 Oct 2018 03:11:19 PM CDT
[daj356 ~/Projects $ ] cat listEmptyDir.sh 
#!/bin/bash
## Daniel Janis 9/26/2018
## This script will take in a directory as $1,
## Loop through all files in this directory and display their names
## If a directory is empty, add the name of this empty directory to "EmptyDir.txt"
## If the number of parameters is not 1, or not a directory,
## Displays usage message and exits non-zero


USAGE="$0 DIRECTORY"

if [[ $# > 1 || $# < 1 ]]       ## Checks to see if 1 and only 1 parameter
  then
    echo -n "Number of parameters is not 1, Usage: "; echo $USAGE
    exit 1
elif [[ -d "$1" ]]              ## Checks to see if parameter is a directory
  then
    if [ -z "$(ls -A "$1")" ]       ## If there is nothing in the DIR, this sends name to EmptyDir.txt
      then
        echo "$1 [This directory is empty]" >> EmptyDir.txt
        date --rfc-822 >> EmptyDir.txt; echo "" >> EmptyDir.txt
        echo -n "Empty directory, usage: "; echo $USAGE
        exit 1
      else
        :
    fi
    for file in $1/* $1/.*      ## For every file in the directory, print the filename
      do echo $file
    done
  else                          ## Prints usage line if $1 is not a directory
    echo -n "Parameter must be a directory, Usage: "; echo $USAGE
    exit 1
fi

[daj356 ~/Projects $ ] cat test_directory/
cat: test_directory/: Is a directory
[daj356 ~/Projects $ ] ./listEmptyDir.sh test_directory/
test_directory//file.txt
test_directory//.
test_directory//..
[daj356 ~/Projects $ ] cat empty_directory/
cat: empty_directory/: Is a directory
[daj356 ~/Projects $ ] ./listEmptyDir.sh empty_directory/
Empty directory, usage: ./listEmptyDir.sh DIRECTORY
[daj356 ~/Projects $ ] cat EmptyDir.txt 
empty_directory/ [This directory is empty]
Sun, 14 Oct 2018 17:39:53 -0500

empty_directory/ [This directory is empty]
Wed, 17 Oct 2018 14:58:36 -0500

empty_directory/ [This directory is empty]
Wed, 17 Oct 2018 15:11:55 -0500

[daj356 ~/Projects $ ] ./listEmptyDir.sh EmptyDir.txt 
Parameter must be a directory, Usage: ./listEmptyDir.sh DIRECTORY
[daj356 ~/Projects $ ] ./listEmptyDir.sh CEnames test_directory/
Number of parameters is not 1, Usage: ./listEmptyDir.sh DIRECTORY
[daj356 ~/Projects $ ] ./listEmptyDir.sh DirectoryDoesNotExist
Parameter must be a directory, Usage: ./listEmptyDir.sh DIRECTORY
[daj356 ~/Projects $ ] exit

Script done on Wed 17 Oct 2018 03:12:53 PM CDT
Script started on Sun 14 Oct 2018 05:50:10 PM CDT
[daj356 ~/Projects $ ] cat contact_one.sh 
#!/bin/bash
## Daniel Janis ## 9/27/2018
## consults myContactList and searches for patterns
## If a pattern exists the program will continue
## If the pattern is not relevant, the program exits

echo "Contact list:"
cat myContactList

while echo -n "Please enter a name to search for: "     ## Prompts the user for a pattern
  do read PATTERN                                       ## Reads the users pattern input
     grep -i $PATTERN << myContactList                  ## Searches myContactList for the pattern
John Doe, jdoe@great.com, 800-555-1111, California
Jane Doe, jand@super.edu, 876-555-1321, New York
John Smith, bsmith@fast.net, 780-555-1234, Florida
Paul Wang, pwang@cs.kent.edu, 330-672-9050, Ohio
myContactList

     if [[ $? == 1 ]]                                   ## If the pattern is not relevant
       then                                             ## Display error message
         echo "That name was not found."
     fi

     echo ""
     echo -n "Would you like to search again (y/n)? "   ## Asks if the user wants to search again
     read YES_NO
     if [[ $YES_NO == y* ]]
       then
         echo ""
     else
       exit 1
     fi 
done

[daj356 ~/Projects $ ] ./contact_one.sh
Contact list:
John Doe, jdoe@great.com, 800-555-1111, California
Jane Doe, jand@super.edu, 876-555-1321, New York
John Smith, bsmith@fast.net, 780-555-1234, Florida
Paul Wang, pwang@cs.kent.edu, 330-672-9050, Ohio

Please enter a name to search for: John
John Doe, jdoe@great.com, 800-555-1111, California
John Smith, bsmith@fast.net, 780-555-1234, Florida

Would you like to search again (y/n)? y

Please enter a name to search for: Jne
That name was not found.

Would you like to search again (y/n)? y

Please enter a name to search for: Jane
Jane Doe, jand@super.edu, 876-555-1321, New York

Would you like to search again (y/n)? y

Please enter a name to search for: Bob
That name was not found.

Would you like to search again (y/n)? y

Please enter a name to search for: Doe
John Doe, jdoe@great.com, 800-555-1111, California
Jane Doe, jand@super.edu, 876-555-1321, New York

Would you like to search again (y/n)? y

Please enter a name to search for: 5
John Doe, jdoe@great.com, 800-555-1111, California
Jane Doe, jand@super.edu, 876-555-1321, New York
John Smith, bsmith@fast.net, 780-555-1234, Florida
Paul Wang, pwang@cs.kent.edu, 330-672-9050, Ohio

Would you like to search again (y/n)? n
[daj356 ~/Projects $ ] exit

Script done on Sun 14 Oct 2018 05:51:29 PM CDT
Script started on Sun 14 Oct 2018 06:05:50 PM CDT
[daj356 ~/Projects $ ] cat fileInfo.sh
#!/bin/bash
## Daniel Janis ## 9/27/2018 ## fileInfo.sh ##
## Presents information about a given file or directory
## If file/directory exists, prints that. If not, exits
## Detects parameter, if none prints the usage line and exits

USAGE="$0 file [ or directory ]"

function checkParameter ()              ## Checks if file/directory
{
if [[ -f "$1" || -d "$1" ]]
then
  if [[ -f "$1" ]]                      ## If a regular file, print that
  then
    echo "Regular file $1 exists"
  else                                  ## else, its a regular directory
    echo "Regular directory $1 exists"
  fi
elif [[ -z "$1" ]]                      ## If the parameter $1 does not exist, exit
then
  echo "Please refer to the usage line"
  echo $USAGE
  exit 1
elif [[ -c "$1" ]]
then
  echo "Special file $1 exists"         ## The parameter is a special file
else
  echo "Please refer to the usage line"         ## Parameter isn't a special/regular file/directory
  echo $USAGE
  exit 1
fi
}

if test $# -gt 0                ## If number of parameters > 0
then                            ## then it will iterate through all parameters
  while test $# -gt 0           ## unless there are no parameters, then exit
  do
    echo $1
    checkParameter $1
    shift
  done
else
  echo $USAGE
  exit 1
fi
[daj356 ~/Projects $ ] ./fileInfo.sh
./fileInfo.sh file [ or directory ]
[daj356 ~/Projects $ ] ./fileInfo.sh fileInfo.sh
fileInfo.sh
Regular file fileInfo.sh exists
[daj356 ~/Projects $ ] ./fileInfo.sh ex04
ex04
Regular directory ex04 exists
[daj356 ~/Projects $ ] ./fileInfo.sh test_directory/ ex04 fileInfo.sh
test_directory/
Regular directory test_directory/ exists
ex04
Regular directory ex04 exists
fileInfo.sh
Regular file fileInfo.sh exists
[daj356 ~/Projects $ ] ./fileInfo.sh test_directory/ ex04 blahblahblah
test_directory/
Regular directory test_directory/ exists
ex04
Regular directory ex04 exists
blahblahblah
Please refer to the usage line
./fileInfo.sh file [ or directory ]
[daj356 ~/Projects $ ] ./fileInfo.sh specialFile
specialFile
Please refer to the usage line
./fileInfo.sh file [ or directory ]
[daj356 ~/Projects $ ] exit

Script done on Sun 14 Oct 2018 06:07:07 PM CDT
Script started on Tue 16 Oct 2018 07:03:15 PM CDT
[daj356 ~/Projects $ ] cat awkDonors.awk
#!/bin/bash
## Daniel Janis
## This script will work using the donors file. The script will use awk commands
## to present information based on the given heading from the project description.
## The name 'Savage' is changed to 'Savauge', the list of donors with the area code
## 916 have been placed in the file "specialAreaCode". The lines with first names
## that start with C or E have been placed in "CEnames" and finally, those who
## donated $500 to the campaign have been listed in the file "over500" which is sorted
## based on last names and telephone numbers.

## The echo below sets the heading line to format this script
echo "NAME                  PHONE           JAN |  FEB |  MAR |"

## This awk command changes the word 'Savage' to 'Savauge' and prints the columns of relevant info
awk -F: '{sub(/Savage/, "Savauge");printf("%-20s %-16s $%-5s $%-5s $%-5s\n", $1, $2, $3 ,$4 ,$5)}' donors

## This awk command lists those with the area code 916 into the file "specialAreaCode"
awk -F: '$2 ~/916/' donors >> "specialAreaCode"

## This awk command lists those with first names that start with C or E in the file "CEnames"
awk -F: '$1 ~/[CE]/' donors >> "CEnames"

## Prints a header line to format the following donors list
echo "NAME                  PHONE           DONATION"

## Sorts the list of donors by their last names
sort -k 2,2 donors >| indexDonors.tmp

## Uses the file indexDonors.awk sort only show those who donated more than $500
awk -F: -f indexDonors.awk indexDonors.tmp > over500

## Prints those who donated over $500
cat over500
[daj356 ~/Projects $ ] cat indexDonors.awk
## Daniel Janis ## 10/16/2018
BEGIN { i = 0; }

$1 == pre { printf("%-20s %-16s $%-5s\n", $1, $2, $3+$4+$5); }

$1 != pre { 
if($3+$4+$5>500)
  { printf( "%-20s %-16s $%-5s\n", $1, $2, $3+$4+$5); }
else
  pre = $1; 
}

END { printf("\n"); }
[daj356 ~/Projects $ ] ./awkDonors.awk
NAME                  PHONE           JAN |  FEB |  MAR |
Mike Harrington      (510) 548-1278   $250   $100   $175                   
Christian Dobbins    (408) 538-2358   $155   $90    $201                   
Susan Dalsass        (206) 654-6279   $250   $60    $50   
Archie McNichol      (206) 548-1348   $250   $100   $175  
Jody Savauge         (206) 548-1278   $15    $188   $150  
Guy Quigley          (916) 343-6410   $250   $100   $175  
Dan Savauge          (406) 298-7744   $450   $300   $275  
Nancy McNeil         (206) 548-1278   $250   $80    $75   
John Goldenrod       (916) 348-4278   $250   $100   $175  
Chet Main            (510) 548-5258   $50    $95    $135  
Tom Savauge          (408) 926-3456   $250   $168   $200  
Elizabeth Stachelin  (916) 440-1763   $175   $75    $300  
NAME                  PHONE           DONATION
John Goldenrod       (916) 348-4278   $525  
Mike Harrington      (510) 548-1278   $525  
Archie McNichol      (206) 548-1348   $525  
Guy Quigley          (916) 343-6410   $525  
Dan Savage           (406) 298-7744   $1025 
Tom Savage           (408) 926-3456   $618  
Elizabeth Stachelin  (916) 440-1763   $550  

[daj356 ~/Projects $ ] ./showAwkDonors.sh


over500:
John Goldenrod       (916) 348-4278   $525  
Mike Harrington      (510) 548-1278   $525  
Archie McNichol      (206) 548-1348   $525  
Guy Quigley          (916) 343-6410   $525  
Dan Savage           (406) 298-7744   $1025 
Tom Savage           (408) 926-3456   $618  
Elizabeth Stachelin  (916) 440-1763   $550  



CEnames:
Christian Dobbins:(408) 538-2358:155:90:201                   
Chet Main:(510) 548-5258:50:95:135 
Elizabeth Stachelin:(916) 440-1763:175:75:300


specialAreaCode:
Guy Quigley:(916) 343-6410:250:100:175 
John Goldenrod:(916) 348-4278:250:100:175 
Elizabeth Stachelin:(916) 440-1763:175:75:300


[daj356 ~/Projects $ ] exit

Script done on Tue 16 Oct 2018 07:03:52 PM CDT
