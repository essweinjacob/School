#!/bin/bash
#clear

if [ -f /etc/passwd ]
    then
        echo "/etc/passwd exists."
fi

let a=2
name=2

if [ $name -eq $a ]
    then echo "equal"
else
    echo "different"
fi

echo
echo "...done."
