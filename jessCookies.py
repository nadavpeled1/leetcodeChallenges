#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/one-month-preparation-kit-jesse-and-cookies/
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#
def cookies(k, A):
    # Write your code here
    # until all cookies are sweet enough do:
    # sort the cookies
    # combine the 2 smallest coockies
    
    #1st approach:
    # result = sorted(A, reverse=True)
    # count = 0
    # while result[-1] < k:
    #     if len(result) == 1:
    #         return -1
    #     c0, c1 = result.pop(), result.pop()
    #     result.append(c0 + c1*2)
    #     count += 1
    # problem is we dont know if the last cookie now is the min, which possible need to sort again
    
    #2nd approach: use a min heap
    import heapq
    heapq.heapify(A)
    count = 0
    while A[0] < k:
        if len(A) == 1:
            return -1
        c0, c1 = heapq.heappop(A), heapq.heappop(A)
        heapq.heappush(A, c0 + c1*2)
        count += 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
