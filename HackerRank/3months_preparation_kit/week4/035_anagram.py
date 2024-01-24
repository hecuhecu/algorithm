#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    n = len(s)
    if n % 2 != 0:
        return -1
    
    s1 = s[:n//2]
    s2 = s[n//2:]
    cnt = defaultdict(int)
    for i in s1:
        cnt[i] += 1
    ans = 0
    for i in s2:
        if cnt[i] != 0:
            cnt[i] -= 1
        else:
            ans += 1
    return ans
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
