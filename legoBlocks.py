#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m


def legoBlocks(n, m):
    # 1. we find all possible options to reach m-length row using breaks of lengths 1 to 4
    # 2. find all possible permutations of stacking n rows, solid and unsolid
    # 3. subtract the number of invalid permutations from total permutations
    # 4. return the result modulo 10^9 + 7

    # 1. find all possible options to reach m-length row using breaks of lengths 1 to 4
    # dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(1, m + 1):
        for j in range(1, 5):
            if i - j >= 0:
                dp[i] += dp[i - j]
                dp[i] %= 1000000007

    # 2. find all possible permutations of stacking n rows, solid and unsolid
    # dp2[i] = dp[i] ** n
    dp2 = [0] * (m + 1)
    dp2[0] = 1
    for i in range(1, m + 1):
        dp2[i] = pow(dp[i], n, 1000000007)

    # 3. subtract the number of invalid permutations from total permutations
    # dp3[i] = dp2[i] - sum(dp3[j] * dp2[i-j] for j in range(1, i))
    dp3 = [0] * (m + 1)
    dp3[0] = 1
    for i in range(1, m + 1):
        for j in range(1, i):
            dp3[i] += dp3[j] * dp2[i - j]
            dp3[i] %= 1000000007
        dp3[i] = (dp2[i] - dp3[i]) % 1000000007

    return dp3[m]
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
