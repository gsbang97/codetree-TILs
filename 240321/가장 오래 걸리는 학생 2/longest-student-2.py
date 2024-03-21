import sys, heapq

# n : 학교 위치
n,m = map(int, input().split())

grape = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,d = map(int, input().split())
    grape[e].append((s,d))

pq = [(0,n)]
dist = [sys.maxsize for _ in range(n+1)]
dist[n] = 0

while pq:
    min_dist, min_idx = heapq.heappop(pq)

    if dist[min_idx] != min_dist :
        continue
    
    for i, d in grape[min_idx]:
        new_dist = dist[min_idx] + d
        
        if new_dist < dist[i]:
            dist[i] = new_dist
            heapq.heappush(pq, (new_dist, i))
    
print(max(dist[1:]))