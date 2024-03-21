import heapq, sys

n, m = map(int, input().split())

k = int(input())

grape = [list() for _ in range(n+1)]

for _ in range(m):
    a, b, dist= map(int, input().split())
    grape[a].append((b,dist))
    grape[b].append((a,dist))

que = []
heapq.heappush(que, (0,k))
dist = [sys.maxsize for _ in range(n+1)]
dist[k] = 0
while que:
    min_dist, min_idx = heapq.heappop(que)
    # try:
    if min_dist != dist[min_idx]:
        continue
    # except:
    #     print(idx, " error")
    #     continue
    
    for idx, d in grape[min_idx]:
        new_dist = dist[min_idx] + d
        if dist[idx] > new_dist :
            dist[idx] = new_dist
            heapq.heappush(que, (new_dist,idx))

for i in range(1,n+1):
    if dist[i] == sys.maxsize:
        dist[i] = -1
    print(dist[i])