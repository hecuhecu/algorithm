#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    plus = 0
    minus = 0
    zero = 0
    for val in arr:
        if val > 0:
            plus += 1
        elif val < 0:
            minus += 1
        else:
            zero += 1
    print(plus/len(arr))
    print(minus/len(arr))
    print(zero/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

