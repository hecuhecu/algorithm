n = int(input())
if n == 1:
    print(0)
    exit()
if n == 2:
    print(0)
    exit()
if n == 3:
    print(1)
    exit()
dp = [0] * (n)
dp[2] = 1
for i in range(3, n):
    dp[i] += (dp[i-1] + dp[i-2] + dp[i-3]) % 10007
print(dp[-1])