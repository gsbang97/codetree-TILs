import sys

N,S = map(int, input().split())
numbers = list(map(int, input().split()))

min_dist = sys.maxsize

s = sum(numbers)
for i in range(N):
    for j in range(i+1,N):
        tmp = s - numbers[i] - numbers[j]
        min_dist = min(abs(tmp-S), min_dist)
print(min_dist)