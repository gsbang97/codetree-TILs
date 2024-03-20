import sys

n = int(input())
numbers = list(map(int, input().split()))
max_number = -sys.maxsize
sum = 0

for num in numbers:
    sum += num
    if sum < num:
        sum = num
    max_number = max(max_number, sum)
print(max_number)