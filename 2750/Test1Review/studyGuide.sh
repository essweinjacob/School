#!/bin/bash

#1. Change permissions of file so that user can read, write, execute and nobody can do anything else
chmod 700 script.bash
#2. Display all lines in the files in current directory that contain the word int
grep -wl 'int' ./*
#3. Display all the lines in the file redme,txt that start with a captial letter A or S
grep ^[AS] readme.txt
#4. Display all the lines in the file readme.txt that end with a comma.
grep -n,$ readme.txt
#5. Display all the lines in the file prog.c that contain int or float.
grep -w 'int|float' prog.c
#6. List all the text files in the current directory
grep
#7. Create a tar file called test.tar that archives everything in the directory dir1.
tar -cvf test.tar dir/
#8. Unpack the archived file test.tar into the current directory
tar -xvf text.tar
#9. List all the files that have the permission rxr--r-- in the current directory or any of its subdirectories and then have them remove those files
find -perm 744 -delete
#10. Assuming bash shell. what is the output of the echo?
    # a=100
    # A="$a students"
    # echo '$A'
$A (because its in single quotes)
#11. Write a bash shell function that takes a single parameter and returns the queare of its value.
fn(){
    a=$(expr $1 '*' $1)
    echo $a
}
fn $1
#12. Assuming bash shell, how do you suspended but not terminate the foreground process
bg
#13. Assuming bash shell,  what does the following command do? And what would the benefit of doing this?
    # alias rm= 'rm -i'
It will make rm interactive will ask user for confirmation
#14. Assuing bash shell, write the output of the echo
    # verb=sing
    # verbing=dancing
    # echo ${verb}ing
singing
#15. Assuming bash shell,  explain what the following command does/
    # head -${howmany:-10} file.txt
Showing the top 10 lines
#16 Display every line in test.c that does not contain the word 'int'
grep -v int test.c
#17. Display each line in the file poem.txt that starts with a capital letter
grep ^[A-Z] poem.txt
#18. Displau the list of files in the current or subdirectories that either have .c or .cpp as their extensions
find -type f -regex".\.[c]\(pp\)?$"
#19. Given the following shell scripts named scripts.sh
    # #!/bin/sh
    # echo $1 $3
    
    # Write the output of the following command
    # scripts.sh this is just a test
this just
#20. Write an awk command that display each line in a file readme.txt that has more than 5 words in it.

