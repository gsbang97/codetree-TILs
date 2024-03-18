import heapq

n,m = map(int, input().split())
hq = []
for number in list(map(int, input().split())):
    heapq.heappush(hq, -number)
for i in range(m):
    number = heapq.heappop(hq)
    heapq.heappush(hq, number+1)

print(-heapq.heappop(hq))