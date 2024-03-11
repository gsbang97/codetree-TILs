R,C = map(int, input().split())
mat = [input().split() for _ in range(R)]
color = mat[0][0]
cnt = 0
if color == mat[-1][-1]:
    print(cnt)
else:
    for i in range(1,R-2):
        for j in range(1,C-2):
            if mat[i][j] != color:
                for k in range(i+1,R-1):
                    for l in range(j+1, C-1):
                        if mat[k][l] == color:
                            cnt +=1

    print(cnt)