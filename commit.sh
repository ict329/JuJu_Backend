#!/bin/bash

./rmpyc.sh
git checkout *.pyc

line=' ========= '
if [ -z "$1" ]; then
    echo "$line"" Commit message is empty. Can  not be comitted ""$line"
    exit 1
fi

echo ""
echo $line' add files (*.py *.sql *.zip)  '$line
git add *
git add *.jpg *.txt *.sh *.png
git add *.zip .gitignore 
git add *.sql *.py
git add commit.sh
echo ''

echo $line' auto checkout unuse files (*xcbkptlist *xcuserstate *DS_Store)  '$line
git checkout *DS_Store
echo ''

echo $line' oh, commit files. comment: '"$1"" "$line
git commit -m "$1"
echo ''

if [ x$2 = x ]
    then
        echo $line' hey, pull code from server '$line
        git pull
        echo ''
    else
        echo $line' Skip pull from server '$line
fi



echo $line' wow, push code to server '$line
git push

echo ''
echo $line' congratulations! hope there is no conflict! '$line
echo ''
