import sys

n = int(input())
number_map = [list(map(int, input().split())) for _ in range(n)]

prefix_sum = [[0 for _ in range(n+1)] for _ in range(n+1)]
max_value = -sys.maxsize

for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_sum[i][j] = number_map[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
        for k in range(i+1):
            for l in range(j+1):
                value = prefix_sum[i][j] - prefix_sum[k][j] - prefix_sum[i][l] + prefix_sum[k][l]
                max_value = max(max_value,value)

print(max_value)