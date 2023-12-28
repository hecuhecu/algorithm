from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
graph = [input() for _ in range(r)]
seen = [[-1]*c for _ in range(r)]
seen[sy-1][sx-1] = 0
deq = deque([[sy-1, sx-1]])
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
while deq:
    y, x = deq.popleft()
    for dy, dx in d:
        if 0 <= y+dy < r and 0 <= x+dx < c and seen[y+dy][x+dx]==-1 and graph[y+dy][x+dx]=='.':
            deq.append([y+dy, x+dx])
            seen[y+dy][x+dx] = seen[y][x] + 1
print(seen[gy-1][gx-1])