x1, y1, x2, y2, x3, y3 = map(int, input().split())
diffx = -x1
diffy = -y1
x1 += diffx
y1 += diffy
x2 += diffx
y2 += diffy
x3 += diffx
y3 += diffy
print(abs(x2*y3-y2*x3)/2)