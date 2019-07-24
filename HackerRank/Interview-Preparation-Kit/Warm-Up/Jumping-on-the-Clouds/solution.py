#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    result = 0
    index = 0
    while index < len(c) - 1:
        if index + 2 < len(c) and c[index + 2] == 0:
            index += 2
        elif c[index + 1] == 0:
            index += 1
        result += 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
