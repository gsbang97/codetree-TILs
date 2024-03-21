import heapq, sys

n,m = map(int, input().split())

grape = [[] for _ in range(n+1)]

for _ in range(m):
    n1, n2, dist = map(int, input().split())

    grape[n1].append((n2, dist))
    grape[n2].append((n1, dist))

A,B = map(int, input().split())

dist = [sys.maxsize for _ in range(n+1)]
prev_index = [-1 for _ in range(n+1)]

pq = [(0,A)]
dist[A] = 0
while pq:
    min_dist, min_index = heapq.heappop(pq)

    if min_dist != dist[min_index]:
        continue
    

    for target_index, target_dist in grape[min_index]:
        new_dist = dist[min_index] + target_dist
        if new_dist < dist[target_index]:
            dist[target_index] = new_dist
            prev_index[target_index] = min_index
            heapq.heappush(pq, (new_dist, target_index))
idx = B
road = []
while idx != -1:
    road.append(idx)
    idx = prev_index[idx]
print(dist[B])
while road:
    print(road.pop(), end= " ")