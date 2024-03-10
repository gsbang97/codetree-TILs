import sys
min_num = sys.maxsize

n = int(input())
nums = list(map(int, input().split()))

for idx in range(n):
    dist = 0
    for i,num in enumerate(nums):
        dist += abs(idx-i)*num
    min_num = min(dist, min_num)

print(min_num)