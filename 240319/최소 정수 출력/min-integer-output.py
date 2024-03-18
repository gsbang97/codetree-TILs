import heapq

n = int(input())

que = []
for _ in range(n):
    number = int(input())
    if number == 0:
        if que:
            print(heapq.heappop(que))
        else:
            print(0)
    else:
        heapq.heappush(que, number)