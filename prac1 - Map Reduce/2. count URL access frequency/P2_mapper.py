#!/usr/bin/python

''' Mapper operation for calculating the frequency of each URL 
 	USAGE: ./P2_mapper.py < ../files/access_log | sort | ./P2_reducer.py '''

import sys
import re

for line in sys.stdin:
    line = re.sub(r'^\W+|\W+$', '', line)
    #Split by double commas to get the GET sentence
    words = line.split('"')

    #Avoid the "-" URL's
    if(words[1] != '-'):
	    #Split by space to get the URL
	    URL = words[1].split(' ')

    print(URL[1] + "\t1")
