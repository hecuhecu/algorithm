xa, ya, xb, yb, t, v = map(int, input().split())
n = int(input())
can_move = t * v
for i in range(n):
    x, y = map(int, input().split())
    dist = ((x-xa)**2 + (y-ya)**2)**0.5 + ((xb-x)**2 + (yb-y)**2)**0.5
    if can_move >= dist:
        print("YES")
        exit()
print("NO")