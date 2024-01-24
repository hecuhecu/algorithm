#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    cnt = Counter(a)
    integer = sorted(cnt.keys())
    ans = cnt[integer[-1]]
    for i in range(len(integer)-1):
        ans = max(ans, cnt[integer[i]])
        if abs(integer[i] - integer[i+1]) <= 1:
            ans = max(ans, cnt[integer[i]]+cnt[integer[i+1]])
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
