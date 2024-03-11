N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
max_num = 0
for i in range(N):
    for j in range(N-2):
        first = sum(mat[i][j:j+3])
        for k in range(i, N):
            if k == i:
                for l in range(j+1,N-2):
                    second = sum(mat[k][l:l+3])
                    s = first + second
                    # print(i,j,k,l)
                    max_num = max(s, max_num)
            else:
                for l in range(N-2):
                    second = sum(mat[k][l:l+3])
                    # print(i,j,k,l)
                    s = first + second
                    max_num = max(s, max_num)

print(max_num)