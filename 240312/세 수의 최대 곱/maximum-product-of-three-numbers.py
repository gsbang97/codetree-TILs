# n과 n개의 수가 주어졌을 때, 3개의 숫자를 적절하게 골라 나올 수 있는 곱 중 최대값
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
# 음수 * 음수 * 양수
first = nums[0]*nums[1]*nums[-1]
# 양수 * 양수 * 양수
seconds = nums[-1]*nums[-2]*nums[-3]
# 음수 * 음수 * 음수 (양수가 없는 경우)
print(max(first,seconds))