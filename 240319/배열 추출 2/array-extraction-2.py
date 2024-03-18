import heapq

n = int(input())
numbers = [int(input()) for _ in range(n)]

arr = []
for number in numbers:
    if number == 0:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print(0)
    else:
        heapq.heappush(arr, (abs(number),number))