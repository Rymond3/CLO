#!/usr/bin/python

''' Mapper operation for calculating the average mass per type of meteorite.
 	USAGE: ./P5_mapper.py < ../files/Meteorite_Landings.csv | sort -V | ./P5_reducer.py '''

import sys
import re

for line in sys.stdin:
    line = re.sub(r'^\W+|\W+$', '', line)
    #Split by comma to get the type in case it's "Pallastine, PMG", becaus e if you split by commas you lose part of the name
    words = line.split('"')

    if(len(words) > 2): #metType = Pallastine, PMG
    	metType = words[1]
    	words = words[2].split(',')
    	mass = words[1]
    else:				#metType != Pallastine, PMG
    	words = words[0].split(',')
    	metType = words[3]
    	mass = words[4]

    print(metType + "\t" + mass)
