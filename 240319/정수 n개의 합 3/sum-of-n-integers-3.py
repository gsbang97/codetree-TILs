n,k = map(int, input().split())

total_sum = [[0 for _ in range(n+1)] for _ in range(n+1)]
number_map = [list(map(int, input().split())) for _ in range(n)]
max_num = 0


for i in range(1,n+1):
    for j in range(1, n+1):
        total_sum[i][j] = total_sum[i-1][j] + total_sum[i][j-1]- total_sum[i-1][j-1] + number_map[i-1][j-1]
        if i >= k and j >= k:
            number = total_sum[i][j] - total_sum[i-k][j] - total_sum[i][j-k] + total_sum[i-k][j-k]
            max_num = max(max_num, number)

print(max_num)