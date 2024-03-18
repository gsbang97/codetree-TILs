import heapq

arr = []
n = int(input())
for _ in range(n):
    number = int(input())
    if number == 0:
        if arr:
            print(-heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, -number)