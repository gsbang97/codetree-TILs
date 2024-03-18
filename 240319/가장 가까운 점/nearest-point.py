# 이때 원점에서 가장 가까운 점을 하나 골라, 해당 점의 x, y 값에 2씩 더해주는 작업을 m번 반복
import heapq

n, m = map(int, input().split())

points = []
for _ in range(n):
    x,y = map(int, input().split())
    dist = abs(x)+abs(y)
    heapq.heappush(points, (dist,x,y))
for _ in range(m):
    dist,x,y = heapq.heappop(points)
    dist,x,y = (abs(x+2)+abs(y+2)),x+2,y+2
    heapq.heappush(points,(dist,x,y))
_,x,y = heapq.heappop(points)
print(x,y)