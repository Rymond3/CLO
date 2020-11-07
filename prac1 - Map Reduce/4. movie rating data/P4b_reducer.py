#!/usr/bin/python

#Reducer operation for calculating the ranges and the movies ids

import sys
import re

previous = None
ids = []


for line in sys.stdin:
	line = re.sub( r'^\W+|\W+$', '', line )
	rating, idMovie = line.split( '\t' )
    
	if rating != previous:
		if previous is not None:
			print 'Range ' + previous + ': ' + str(ids)
		previous = rating
		ids = [idMovie]
    
	if idMovie != ids[-1]:
		ids.append(idMovie)

print 'Range ' + previous + ': ' + str(ids)

