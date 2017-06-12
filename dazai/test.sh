#!/bin/sh

files="./*"
count=1
for file in ${files}
do
   echo ${file}
   echo $((count++))
done

