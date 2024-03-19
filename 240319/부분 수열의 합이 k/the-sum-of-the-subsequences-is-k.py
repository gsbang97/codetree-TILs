n,k = map(int, input().split())
numbers = list(map(int, input().split()))
sum_arr = [0 for _ in range(n+1)]
cnt = 0
for i,number in enumerate(numbers, start = 1):
    sum_arr[i] = sum_arr[i-1] + number
    for j in range(i):
        if sum_arr[i]-sum_arr[j] == k:
            cnt += 1

print(cnt)