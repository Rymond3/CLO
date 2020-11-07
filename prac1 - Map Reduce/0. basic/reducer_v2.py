#!/usr/bin/python

''' Reducer operation for inverted index of words '''

import sys
import re

previous = None
doc_id = []


for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    key, value = line.split( '\t' )
    
    if key != previous:
        if previous is not None:
            print previous + '\t' + str(doc_id)
        previous = key
        doc_id = [value]
    
    if value != doc_id[-1]:
        doc_id.append(value)

print previous + '\t' + str(doc_id)