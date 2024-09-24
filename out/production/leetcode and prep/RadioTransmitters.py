#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    # Write your code here
    travesre_q = []  # a queue to traverse the graph.
    dist = {}  # will hold how many steps required to reach a node from s using BFS
    unreached = set()
    for i in range(1, n+1):
        if i != s:
            unreached.append(i)
            dist[i] = -1
    
    def add_edges(v):
        # gets a vertice and append the possible edges to the trav_q
        for e in edges:
            if v in e:
                travesre_q.append(e)
                # we can use every edge once
                edges.remove(e)
    
    add_edges(s)
    step = 0
    
    while travesre_q and unreached:  # while still have possible edges to traverse, and unreached edges
        e = travesre_q.pop(0)
        step += 1
        v1, v2 = e[0], e[1]
        if v1 in unreached:
            dist[v1] == step
            add_edges(v1)
        if v2 in unreached:
            dist[v2] == step
            add_edges(v2)
    
    return dist
            

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
