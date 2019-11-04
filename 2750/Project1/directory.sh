#!/bin/bash

if [[ -e $# && -d $# ]]
    then
    echo "Directory exists"
else
    echo "directory does not exist"
fi
