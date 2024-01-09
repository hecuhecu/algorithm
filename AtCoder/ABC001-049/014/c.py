n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
h = [0] * (1000002)
for i in range(n):
    h[ab[i][0]] += 1
    h[ab[i][1]+1] -= 1

for i in range(1000001):
    h[i+1] += h[i]
print(max(h))