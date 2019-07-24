#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    total = 0
    result = ''
    for i in range(0, len(q)):
        diff = abs((i + 1) - q[i])
        if diff >= 3:
            result = 'Too chaotic'
            break
        total += diff
    if result == '':
        print(int(total/2))
    else:
        print(result)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
