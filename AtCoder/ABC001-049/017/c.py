n, m = map(int, input().split())
list = [0] * (m + 1)
sum = 0
for i in range(n):
    l, r, s = map(int, input().split())
    sum += s
    list[l-1] += s
    list[r] -= s

for i in range(m):
    list[i+1] += list[i]
ans = float('inf')
for i in range(m):
    ans = min(ans, list[i])

print(sum-ans)
