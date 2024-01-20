#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    ans = ""
    if "AM" in s and s[0:2] == "12":
        ans = f"00{s[2:-2]}"
    elif "AM" in s:
        ans = s[0:-2]
    elif "PM" in s and s[0:2] == "12":
        ans = s[0:-2]
    else:
        h = int(s[0:2]) + 12
        ans = f"{h}:{s[3:-2]}"
    return ans
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
