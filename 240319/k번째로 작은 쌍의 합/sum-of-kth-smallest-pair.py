import heapq

n,m,k = map(int, input().split())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

arr = []
ans = -1
for a in A:
    if ans != -1 and a > ans:
        break
    for b in B:
        if k > 0:
            heapq.heappush(arr, -(a+b))
            k -= 1
        else:
            if ans == -1:
                ans = -heapq.heappop(arr)
            
            if ans > a+b:
                # print(ans, a+b)
                heapq.heappush(arr,-(a+b))
                ans = -heapq.heappop(arr)
            else:
                break
                
            #     heapq.heappush(arr,-value)
# for _ in range(k-1):
#     heapq.heappop(arr)
if ans == -1:
    ans = -heapq.heappop(arr)
print(ans)