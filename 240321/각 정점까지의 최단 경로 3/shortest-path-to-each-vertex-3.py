import sys
import heapq

n,m = map(int, input().split())

grape = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    start, end, dist = map(int, input().split())
    grape[start][end] = dist
min_dist = [sys.maxsize for _ in range(n+1)]
min_dist[1] = 0
visited = [False for _ in range(n+1)]
ans = 0
for _ in range(n):
    min_idx = (-1, sys.maxsize)
    # print(*min_dist)
    for j in range(1,n+1):
        if min_dist[j] < min_idx[1] and not visited[j]:
            min_idx = (j, min_dist[j])
    idx = min_idx[0]
    # print(idx)
    # print(*grape[idx])
    if idx == -1:
        # ans = -1
        break
    visited[idx] = True
    for i,dist in enumerate(grape[idx][1:], start = 1):
        if not visited[i] and dist != sys.maxsize:
            min_dist[i] = min(min_dist[i], min_dist[idx]+dist)
for i in range(2,n+1):
    if min_dist[i] == sys.maxsize:
        print(-1)
    else:
        print(min_dist[i])