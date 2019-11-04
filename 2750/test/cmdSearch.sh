#!/bin/bash
## Finds a given comand on the search path

cmd="$1"
# First argument given
path=$(echo $PATH | tr ":" " ")
for dir in $path
    do
        if [[ -x "$dir/$cmd" ]]
            then
                echo "FOUND: $dir/$cmd"
                exit 0
        fi
    done
echo "$cmd not on $PATH"
