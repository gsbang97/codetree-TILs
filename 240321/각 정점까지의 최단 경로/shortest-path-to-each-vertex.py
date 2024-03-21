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
    value, idx = heapq.heappop(que)
    # try:
    if value != dist[idx]:
        continue
    # except:
    #     print(idx, " error")
    #     continue
    
    for num, d in grape[idx]:
        if dist[num] > (dist[idx] + d) :
            dist[num] = dist[idx] + d
            heapq.heappush(que, (dist[num],d))

for i in range(1,n+1):
    if dist[i] == sys.maxsize:
        dist[i] = -1
    print(dist[i])