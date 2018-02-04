#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    count = 0
    maxi = max(ar)
    # Complete this function
    for i in range(0,len(ar)):
        if(ar[i]==maxi):
            count = count + 1
    return count
        
        

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
