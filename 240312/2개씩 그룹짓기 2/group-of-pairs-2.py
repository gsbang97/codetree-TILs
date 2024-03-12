import sys
n = int(input())
number = list(map(int, input().split()))
min_num = sys.maxsize
number.sort()
for i in range(n):
    min_num = min(min_num, (number[i+n]-number[i]))
print(min_num)