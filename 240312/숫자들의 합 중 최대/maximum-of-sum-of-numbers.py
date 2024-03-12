x,y = map(int, input().split())
max_num = 0
for i in range(x,y+1):
    nums = list(map(int, str(i)))
    max_num = max(max_num, sum(nums))
print(max_num)