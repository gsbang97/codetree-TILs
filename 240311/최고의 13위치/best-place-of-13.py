import sys

N = int(input())
max_coin = -sys.maxsize
mat = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N-3+1):
        max_coin = max(max_coin, sum(mat[i][j:j+3]))
print(max_coin)