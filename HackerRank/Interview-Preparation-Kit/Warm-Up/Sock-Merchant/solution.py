#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = dict()
    for sock in ar:
        if sock in pairs.keys():
            pairs[sock] += 1
        else:
            pairs[sock] = 1
    print(pairs)
    result = 0
    for key in pairs:
        result += math.floor(pairs[key]/2)
    return int(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
