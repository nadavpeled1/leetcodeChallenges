#!/bin/python3

import math
import os
import random
import re
import sys


# https://www.hackerrank.com/challenges/one-month-preparation-kit-qheap1
# Enter your code here. Read input from STDIN. Print output to STDOUT


# This question is designed to help you get a better understanding of basic heap operations.

# There are  types of query:

# "1 v" - Add an element  to the heap.
# "2 v " - Delete the element  from the heap.
# "3" - Print the minimum of all the elements in the heap.
# NOTE: It is guaranteed that the element to be deleted will be there in the heap. Also, at any instant, only distinct elements will be in the heap.

# Input Format

# The first line contains the number of queries, .
# Each of the next  lines contains one of the  types of query.

# Constraints
# 1 <= q <= 10^5
# -10^9 <= v <= 10^9
# The element to be deleted will be in the heap.
# element will be distinct in the heap.
# Output Format
# For each query of type , print the minimum value on a single line.
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    #init the heap:
    min_heap = []
    def add(n: int):
        # Add the element to the end of the heap
        min_heap.append(n)
        pos = len(min_heap) - 1
        
        # Bubble up the new element to maintain the heap property
        while pos > 0:
            parent_pos = (pos - 1) // 2
            parent = min_heap[parent_pos]
            if parent > n:
                # Move the parent down to the current position of the added element
                min_heap[pos] = parent
                pos = parent_pos
            else:
                break
        min_heap[pos] = n

    def delete(n: int):
        # Find the position of the element to be deleted
        pos = min_heap.index(n)
        min_heap[pos] = min_heap[-1]
        min_heap.pop()
        
        # Bubble down the element to maintain the heap property
        while pos < len(min_heap):
            left_child_pos = 2 * pos + 1
            right_child_pos = 2 * pos + 2
            if left_child_pos >= len(min_heap):
                break
            if right_child_pos >= len(min_heap):
                min_child_pos = left_child_pos
            else:
                min_child_pos = left_child_pos if min_heap[left_child_pos] < min_heap[right_child_pos] else right_child_pos
            if min_heap[pos] > min_heap[min_child_pos]:
                min_heap[pos], min_heap[min_child_pos] = min_heap[min_child_pos], min_heap[pos]
                pos = min_child_pos
            else:
                break
        
    # take the amount of queries:
    q = input().strip()
    # for each query:
    for i in range(q):
        # split input to a list:
        query = input().strip().split()
        qType = int(query[0])
        if qType == 1:
            add(int(query[1]))
        elif qType == 2:
            delete(int(query[1]))
        elif qType == 3:
            print(min_heap[0])