n = int(input())
ans = 100
for i in range(n):
  t = int(input())
  ans = min(ans, t)
print(ans)