#!/usr/bin/python

''' Mapper operation for calculating the movies ids and their average
 	USAGE: ./P4a_mapper.py < ../files/ml-latest-small/ratings1.csv | sort | ./P4a_reducer.py | ./P4b_mapper.py | sort | ./P4b_reducer.py '''

import sys
import re

for line in sys.stdin:
    line = re.sub(r'^\W+|\W+$', '', line)
    #Split by comma to get the movie id and rating
    words = line.split(',')

    print(words[1] + "\t" + words[2])
