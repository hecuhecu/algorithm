n, k = map(int, input().split())
r = list(map(int, input().split()))
ans = 0
r.sort()
for i in range(n-k, n):
  ans = (ans + r[i]) / 2
print(ans)