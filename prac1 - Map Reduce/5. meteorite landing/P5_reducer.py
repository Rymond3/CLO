#!/usr/bin/python

#Reducer operation for calculating the average daily stock price at close

import sys

previous = None
sum = 0
cnt = 0

for line in sys.stdin:
    metType, value = line.split('\t')
    
    if metType != previous:
        if previous is not None:
            print previous + '\t' + str(sum/cnt)
        previous = metType
        sum = 0
        cnt = 1
    
    #Some don't have value, so I won't take them into account
    if value != "\n":
    	sum = sum + float(value)
    	cnt += 1

print previous + '\t' + str(sum/cnt)

