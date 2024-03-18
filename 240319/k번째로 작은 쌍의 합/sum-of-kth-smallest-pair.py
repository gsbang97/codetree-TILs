import heapq

n,m,k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

arr = []
for a in A:
    for b in B:
        heapq.heappush(arr, a+b)

for _ in range(k-1):
    heapq.heappop(arr)
print(heapq.heappop(arr))