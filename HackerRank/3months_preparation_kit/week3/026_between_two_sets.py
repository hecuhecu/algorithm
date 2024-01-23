import math

def getTotalX(a, b):
    # Write your code here
    lcm = math.lcm(*a)
    ans = 0
    b.sort()
    x = lcm
    while x <= b[0]:
        ok = True
        for val in b:
            if val % x != 0:
                ok = False
                break
        if ok:
            ans += 1
        x += lcm
    return ans