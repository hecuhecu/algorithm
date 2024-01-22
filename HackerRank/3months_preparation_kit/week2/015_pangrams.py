#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    dict = defaultdict(int)
    ans = 'pangram'
    s = s.lower()
    for c in s:
        dict[c] += 1
    for i in "abcdefghijklmnopqrstuvwxyz":
        if dict[i] == 0:
            ans = 'not pangram'
            break
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
