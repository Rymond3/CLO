#!/usr/bin/python

''' Mapper operation for inverted index of words '''

import sys
import re

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(r"\W+", line)

    for word in words[1:]:
    	print(word.lower() + "\t" + words[0])

