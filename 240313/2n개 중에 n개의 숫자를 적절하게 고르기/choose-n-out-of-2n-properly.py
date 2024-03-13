n = int(input())

numbers = list(map(int, input().split()))
m = len(numbers)
sum_v = sum(numbers)
min_value = sum_v
def choose(cnt, v, idx):
    global min_value
    if cnt == n:
        value = abs(sum_v - v * 2)
        min_value = min(min_value, value)
        return 
    for i in range(idx+1, m):
        choose(cnt + 1, v + numbers[i], i)

choose(0,0,-1)

print(min_value)