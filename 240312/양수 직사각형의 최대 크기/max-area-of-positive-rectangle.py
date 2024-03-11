n,m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
result = -1
for i in range(n):
    for j in range(m):
        for r in range(n-i):
            for c in range(m-j):
                if mat[i+r][j+c] > 0:
                    result = max(result, (r+1) * (c+1))
print(result)