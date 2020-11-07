#!/usr/bin/python

#Reducer operation for calculating the movies ids and their average

import sys

previous = None
sum = 0
cnt = 0

for line in sys.stdin:
    key, value = line.split('\t')
    
    if key != previous:
        if previous is not None:
            print previous + '\t' + str(sum/cnt)
        previous = key
        sum = 0
        cnt = 1
    
    sum = sum + float(value)
    cnt += 1

print previous + '\t' + str(sum/cnt)

