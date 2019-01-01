#!/bin/bash
echo "to use: ./split.sh numLastCardMade (k) < fileToSplit(k)"
n=$1
i=0
while read p; do
	s=$(($i%10))
	i=$(($i+1))
	if [ $s -eq 0 ]
	then n=$(($n+10))   
	fi
	echo "$p" >> "out/$n$2"	
done
