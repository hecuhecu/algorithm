#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    for i in range(1, len(s)//2+1):
        sub = s[:i]
        st = num = int(sub)
        while len(sub) < len(s):
            num += 1
            sub += str(num)
        if sub == s:
            print("YES", st)
            return
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
