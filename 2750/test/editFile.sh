#!/bin/bash

for file in *
    do if grep -q "$1" matches $file
        then vim $file
    fi
done
