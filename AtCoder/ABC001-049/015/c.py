from itertools import product
n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
for i in product(range(k), repeat=n):
  ans = 0
  for j, val in enumerate(i):
    ans = ans ^ t[j][val]
    if ans == 0:
      print("Found")
      exit()
print("Nothing")