#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    pairs = 0
    for i in range(1, len(s)):
        counts = dict()
        subs = list()
        for j in range(0, len(s) - i + 1):
            sub = list(s[j:j+i])
            sub.sort()
            sub = str(sub)
            if not sub in counts:
                counts[sub] = 0
            counts[sub] += 1
        for sub in counts:
            if not counts[sub] % 2:
                pairs += counts[sub] // 2
    return pairs # This undercounts if there's something like aaaa

        letters = list(s[])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
