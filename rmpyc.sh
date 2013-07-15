#!/bin/bash
#Your Command Below!!!

files=`find . -name *.pyc`
for file in $files
    do rm $file
    echo 'rm file '$file
    done
