#!/bin/sh

files="./*.txt"
count=1
for file in ${files}
do
  nkf -w -Lu ${file} > m.txt
  touch dazai_$((count++)).txt
  cat m.txt | ruby -e 'puts ARGF.read.gsub(/｜/, "").gsub(/《.+?》/,"").gsub(/［.+?］/,"")' > dazai_$((count++)).txt
  rm -f m.txt
done


