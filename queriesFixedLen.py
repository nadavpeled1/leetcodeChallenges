#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#
# from collections import deque
def solve(arr, queries):
    result = []
    
    for d in queries:
        deq = deque()
        max_in_window = []
        
        for i in range(len(arr)):
            # Remove elements not within the window
            if deq and deq[0] == i - d:
                deq.popleft()
            
            # Remove elements smaller than the current element
            while deq and arr[deq[-1]] <= arr[i]:
                deq.pop()
            
            deq.append(i)
            
            # Append the maximum for the current window
            if i >= d - 1:
                max_in_window.append(arr[deq[0]])
        
        result.append(min(max_in_window))
    
    return result
    
def solve(arr, queries):
    result = []
    
    for d in queries:
        maxs = []
        for i in range(len(arr)-d):
            maxs.append(max(arr[i:i+d]))
        result.append(min(maxs))
    
    return result
            
                
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
