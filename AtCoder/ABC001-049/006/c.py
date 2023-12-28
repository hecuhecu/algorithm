n, m = map(int, input().split())
for child in range(n+1):
    # 2a+3b+4c=M
    # a+b+c=N
    # 連立方程式を解くには変数文の式が必要。cをfor文で与えるとすると、
    # a = -M + 3N + c'
    # b = M - 2N - 2c'
    # で計算できる。
    adult = -m + 3*n + child
    roujin = m -2*n - 2*child
    if roujin >= 0 and adult >= 0:
        print(adult, roujin, child)
        exit()
print(-1, -1, -1)