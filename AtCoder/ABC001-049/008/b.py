from collections import defaultdict

n = int(input())
dict = defaultdict(int)
for i in range(n):
    s = input()
    dict[s] += 1
print(max(dict, key=dict.get))