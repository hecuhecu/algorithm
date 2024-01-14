n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

for i in range(n):
  friends = set()
  for v in graph[i]:
    for vv in graph[v]:
      friends.add(vv)
  friends.discard(i)
  for v in graph[i]:
    friends.discard(v)
  print(len(friends))