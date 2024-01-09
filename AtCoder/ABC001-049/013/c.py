n, h = map(int, input().split())
a, b, c, d, e = map(int, input().split())
ans = float('inf')
for i in range(n+1):
    j = max(0, (n*e-h-i*(b+e))//(d+e)+1)
    calc = i*a + j*c
    ans = min(ans, calc)
print(ans)