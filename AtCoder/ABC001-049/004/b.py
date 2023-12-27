c = [input() for i in range(4)]
for i in range(len(c)-1, -1, -1):
  for j in range(len(c[0])-1, -1, -1):
    print(c[i][j], end='')
  print()