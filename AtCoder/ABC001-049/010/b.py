n = int(input())
a = list(map(int, input().split()))
list = [2, 4, 5, 6, 8]
ans = 0
for i in a:
    if i in list:
        while i in list:
            i -= 1
            ans += 1
print(ans)
