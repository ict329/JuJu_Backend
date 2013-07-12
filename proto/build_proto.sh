#!/bin/bash

DST_DIR=../pbmodels
SRC_DIR=.


cd $SRC_DIR
Files=`ls *.proto`

echo "Start to build proto files for Python"

for file in $Files
    do 
        echo "Build file: $file"
        protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/$file
    done

echo "Done"
