import heapq

n,m,k = map(int, input().split())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

arr = []
for a in A:
    for b in B:
        if k > 0:
            heapq.heappush(arr, -(a+b))
            k -= 1
        else:
            value = -heapq.heappop(arr)
            if value > a+b:
                heapq.heappush(arr,-(a+b))
                break
            else:
                heapq.heappush(arr,-value)
# for _ in range(k-1):
#     heapq.heappop(arr)
print(-heapq.heappop(arr))