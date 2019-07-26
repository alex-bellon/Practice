#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap = 0
    for i in range(0, len(arr) - 1):
        num = i + 1
        while not arr[i] == num:
            temp = arr[i]
            arr[i] = arr[temp - 1]
            arr[temp - 1] = temp
            swap += 1
    return swap


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
