#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a = sum([1 for letter in s if letter == 'a'])
    result = a * int(n/len(s))
    left = s[:(n % len(s))]
    result += sum ([1 for letter in left if letter == 'a'])
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
