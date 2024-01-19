s = list(input())
n = int(input())
tmp = ''
for i in range(n):
    l, r = map(int, input().split())
    s[l-1:r] = reversed(s[l-1:r])
print(''.join(s))