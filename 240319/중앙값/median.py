import heapq

t = int(input())

for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))
    mid = - 1
    left = []
    right = []
    tmp = []
    for i,num in enumerate(arr, start = 1):
        if i == 1:
            mid = num
            print(mid, end=" ")
            continue
        if i == 2: continue
        if i == 3:
            sorted_arr = sorted(arr[:3])
            mid = sorted_arr[1]
            heapq.heappush(left,-sorted_arr[0])
            heapq.heappush(right, sorted_arr[2])
            print(mid, end=" ")
            continue
        heapq.heappush(tmp, num)
        if i%2 == 1:
            heapq.heappush(tmp, -heapq.heappop(left))
            heapq.heappush(tmp, heapq.heappop(right))
            heapq.heappush(tmp, mid)
            # heapq.heappush(tmp, arr[i-2])
            # heapq.heappush(tmp, arr[i-1])
            # print(tmp,i)
            heapq.heappush(left, -heapq.heappop(tmp))
            heapq.heappush(left, -heapq.heappop(tmp))
            mid = heapq.heappop(tmp)
            heapq.heappush(right, heapq.heappop(tmp))
            heapq.heappush(right, heapq.heappop(tmp))
            print(mid, end=" ")
    print()