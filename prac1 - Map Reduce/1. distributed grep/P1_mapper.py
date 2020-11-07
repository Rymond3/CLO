#!/usr/bin/python

''' Mapper operation for searching all the lines where a specific word appears
	USAGE: ./P1_mapper.py word < ../files/input.txt | sort | ./P1_reducer.py '''

import sys
import re

argument = sys.argv[1]

for line in sys.stdin:
    line = re.sub(r'^\W+|\W+$', '', line)
    words = re.split(r"\W+", line)
    
    for word in words:
    	if(word == argument):
        	print(line)
