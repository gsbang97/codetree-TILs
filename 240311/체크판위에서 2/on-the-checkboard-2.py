R,C = map(int, input().split())
mat = [input().split() for _ in range(C)]
color = mat[0][0]
cnt = 0
for i in range(1,R-2):
    for j in range(1,C-2):
        if mat[i][j] != color:
            for k in range(i+1,R-1):
                for j in range(j+1, C-1):
                    if mat[k][j] == color:
                        cnt +=1

print(cnt)