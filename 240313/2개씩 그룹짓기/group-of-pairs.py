n = int(input())
arr = list(map(int, input().split()))
arr.sort()
max_num = 0
for i in range(n):
    max_num = max(max_num, (arr[i]+ arr[-1-i]))

print(max_num)