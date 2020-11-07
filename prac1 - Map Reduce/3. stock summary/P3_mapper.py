#!/usr/bin/python

''' Mapper operation for calculating the average daily stock price at close
 	USAGE: ./P3_mapper.py < ../files/GOOGLE1.csv | sort | ./P3_reducer.py '''

import sys
import re

for line in sys.stdin:
    line = re.sub(r'^\W+|\W+$', '', line)
    #Split by dash to get the year
    words = re.split(r'[-,]', line)

    print(words[0] + "\t" + words[-2])
