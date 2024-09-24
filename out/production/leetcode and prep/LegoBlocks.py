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


MOD = 1000000007

def legoBlocks(n, m):
    # Step 1: Find all possible options to reach m-length row using bricks of lengths 1 to 4
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(1, m + 1):
        for length in range(1, 5):
            if i >= length:
                dp[i] += dp[i - length]
                dp[i] %= MOD

    # Step 2: Find all possible permutations of stacking n rows, solid and unsolid
    dp2 = [0] * (m + 1)
    dp2[0] = 1
    for i in range(1, m + 1):
        dp2[i] = pow(dp[i], n, MOD)

    # Step 3: Subtract the number of invalid permutations from total permutations
    dp3 = [0] * (m + 1)
    dp3[0] = 1
    for i in range(1, m + 1):
        dp3[i] = dp2[i]
        for j in range(1, i):
            dp3[i] -= dp3[j] * dp2[i - j]
            dp3[i] %= MOD

    # Step 4: Return the result modulo 10^9 + 7
    return dp3[m]


if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
