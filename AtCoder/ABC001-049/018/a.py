a = int(input())
b = int(input())
c = int(input())
x = [a, b, c]
y = sorted(x, reverse=True)
for i in x:
    print(y.index(i) + 1)