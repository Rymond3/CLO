#!/usr/bin/python

''' Mapper operation for calculating the ranges and the movies ids
 	USAGE: ./P4a_mapper.py < ../files/ml-latest-small/ratings1.csv | sort | ./P4a_reducer.py | ./P4b_mapper.py | sort | ./P4b_reducer.py '''

import sys

for line in sys.stdin:
    idMovie, average = line.split('\t')
    ratingClass = 0

    average = float(average)
    if(average <= 1):
    	ratingClass = 1
    elif(average <= 2):
    	ratingClass = 2
    elif(average <= 3):
    	ratingClass = 3
    elif(average <= 4):
    	ratingClass = 4
    elif(average <= 5):
    	ratingClass = 5

    print(str(ratingClass) + "\t" + idMovie)
