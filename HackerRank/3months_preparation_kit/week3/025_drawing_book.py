#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    ans = 0
    st_page = 1
    ed_page = n if n%2==0 else n-1
    if st_page == p or ed_page <= p:
        return ans
        
    for i in range(n):
        st_page += 2
        ed_page -= 2
        ans += 1
        if st_page >= p or ed_page <= p:
            break
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
