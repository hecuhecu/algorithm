n = int(input())
a = [int(input()) for _ in range(n)]
a.sort(reverse=True)
tmp = a[0]
for i in a:
    if i != tmp:
        print(i)
        exit()