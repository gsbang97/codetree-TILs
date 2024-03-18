import heapq

n = int(input())
arr =list(map(int, input().split()))

que = []
for number in arr:
    heapq.heappush(que, -number)

while n >= 2 : # 2개 이상의 숫자가 남아있는 경우
    n -= 2
    n1 = -heapq.heappop(que)
    n2 = -heapq.heappop(que)
    dist = abs(n1-n2)
    if dist != 0:
        heapq.heappush(que, -dist)
        n += 1
# print(que)
if que:
    print(-que.pop())
else:
    print(-1)