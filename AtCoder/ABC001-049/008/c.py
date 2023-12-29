n = int(input())
c = list(int(input()) for _ in range(n))
ans = 0
for i in range(n):
    num = 0
    for j in range(n):
        if i == j:
            continue
        if c[i] % c[j] == 0:
            num += 1
    ans += ((num + 2) // 2) / (num + 1)
print(ans)