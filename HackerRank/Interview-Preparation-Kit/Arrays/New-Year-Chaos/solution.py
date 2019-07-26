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
        diff = q[i] - (i + 1)
        if diff >= 3:
            print('Too chaotic')
            return
        else:
            for j in range(i, min(q[i] + 3, len(q))):
                if q[j] < q[i]:
                    total += 1
    print(total)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
