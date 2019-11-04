#!/bin/sh

x=1
until [ $x -gt 3 ]
do
    echo x = $x
    x=$((x + 1))
done

