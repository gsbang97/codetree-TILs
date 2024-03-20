n = int(input())
numbers = dict()
for _ in range(n):
    x,y = map(int, input().split())
    numbers[y] = x
keys = sorted(list(numbers.keys()))
max_idx = len(keys)-1
min_idx = 0
max_num = 0
while min_idx <= max_idx:
    max_key = keys[max_idx]
    min_key = keys[min_idx]
    max_cnt = numbers[max_key]
    min_cnt = numbers[min_key]
    
    max_num = max(max_num, max_key + min_key)
    if max_cnt < min_cnt:
        numbers[min_key] -= max_cnt
        numbers[max_key] = 0
        max_idx -= 1
        if numbers[min_key] <= 0:
            min_key += 1
    else:
        numbers[max_key] -= min_cnt
        numbers[min_key] = 0
        min_idx += 1
        if numbers[max_key] <= 0:
            max_idx -= 1

print(max_num)