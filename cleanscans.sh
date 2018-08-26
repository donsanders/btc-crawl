#!/bin/sh
#Clean json files, throw away final line as it may have been partially written and then fix up final line ending
#Don’t modify input files, creates new "cleaned" files in prefix directory
scans=100
prefix="scans/Satoshi-0-16-3-"

#1. Delete last line of file
#2. If the last character in the file is a comma then delete it.
#3. Append ‘]’ character
echo "]" > $prefix"-cb.txt"
for i in $(seq 1 $scans) ; do cp $prefix$i".json" $prefix"copy-"$i".json" ; done
for i in $(seq 1 $scans) ; do ghead -n -1 $prefix"copy-"$i".json" > $prefix"copy2-"$i".json" ; done
for i in $(seq 1 $scans) ; do rm $prefix"copy-"$i".json" ; done
for i in $(seq 1 $scans) ; do gsed -zr 's/,([^,]*$)/\1/' $prefix"copy2-"$i".json" > $prefix"copy3-"$i".json" ; done
for i in $(seq 1 $scans) ; do rm $prefix"copy2-"$i".json" ; done
for i in $(seq 1 $scans) ; do cat $prefix"copy3-"$i".json" $prefix"-cb.txt" > $prefix"cleaned-"$i".json" ; done
for i in $(seq 1 $scans) ; do rm $prefix"copy3-"$i".json" ; done
rm $prefix"-cb.txt"
