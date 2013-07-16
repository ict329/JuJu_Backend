#!/bin/bash
#Your Command Below!!!

l=`cat constant.py`

for ll in $l
    do sp=`echo $ll | tr "[a-z]" "[A-Z]"`
    echo $ps = $ll
    
done

