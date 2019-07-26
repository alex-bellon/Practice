#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    totals = dict()
    for op in queries:
        if not op[0] in totals:
            totals[op[0]] = 0
        if not op[1] + 1 in totals:
            totals[op[1] + 1] = 0
        totals[op[0]] += op[2]
        totals[op[1] + 1] -= op[2]
    a = list()
    current = 0
    for i in range(1, n + 1):
        if i in totals.keys():
            current += totals[i]
        a.append(current)

    return max(a)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
