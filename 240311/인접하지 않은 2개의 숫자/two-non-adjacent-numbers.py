import sys

n = int(input())
numbers = list(map(int, input().split()))
max_num = -sys.maxsize
for i in range(n-2):
    for j in range(i+2,n):
        max_num = max(max_num, numbers[i]+numbers[j])

print(max_num)