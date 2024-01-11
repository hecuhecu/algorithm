import math

n = int(input())
a = list(map(int, input().split()))
total = 0
cnt = 0
for i in a:
    if i == 0:
        continue
    else:
        total += i
        cnt += 1
print(math.ceil(total/cnt))