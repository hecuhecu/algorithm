n = int(input()) % 30
list = [1, 2, 3, 4, 5, 6]
for i in range(n):
  list[i%5+1-1], list[i%5+2-1] = list[i%5+2-1], list[i%5+1-1]
print(*list, sep='')