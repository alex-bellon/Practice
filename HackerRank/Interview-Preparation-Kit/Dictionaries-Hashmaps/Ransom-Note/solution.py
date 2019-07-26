#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    words = dict()
    for word in magazine:
        if not word in words.keys():
            words[word] = 0
        words[word] += 1
    for word in note:
        if not word in words.keys() or not words[word]:
            print('No')
            return
        words[word] -= 1
    print('Yes')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
