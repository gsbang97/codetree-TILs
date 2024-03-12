# 1부터 n까지의 수들이 정확히 한 개씩 들어있는 수열
# 움직임 : 시작위치를 정하면 그 위치에 들어있는 원소값을 다시 위치값으로 하여 이동하는것
# 시작 위치를 하나 잘 골라 '움직임'을 m번 반복 했을 때, '원소값들의 합'이 최대가 되도록 하는 프로그램

n, m = map(int, input().split())
nums = list(map(int, input().split()))
max_sum = 0

for start in range(1,n+1):
    s = 0
    for _ in range(m):
        next_num = nums[start-1]
        s += next_num
        start = next_num
    max_sum = max(s, max_sum)
print(max_sum)