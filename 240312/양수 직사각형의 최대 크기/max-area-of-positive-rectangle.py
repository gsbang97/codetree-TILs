n,m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
result = -1

for i in range(n):
    for j in range(m):
        x_c = m
        for r in range(n-i):
            for c in range(m-j):
                if mat[i+r][j+c] > 0 and c < x_c:
                    # if r*c > 0:
                    # print(i,j,r,c)
                    result = max(result, (r+1) * (c+1))
                else :
                    x_c = c             
                    break
print(result)