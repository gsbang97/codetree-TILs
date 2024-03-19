# 연속하는 k개의 원소들의 합 중 가장 큰 값

n,k = map(int, input().split())

numbers = list(map(int, input().split()))
sum_numbers = [0 for _ in range(n+1)]
max_num = 0
for i in range(1,n+1-k):
    sum_numbers[i] = sum_numbers[i-1]+numbers[i-1]
    if i >= k :
        number = sum_numbers[i] - sum_numbers[i-k]
        max_num = max(max_num, number)

print(max_num)