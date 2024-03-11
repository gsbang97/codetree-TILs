N,M = map(int, input().split())
words = [input() for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if words[i][j] == 'L':
            if i < N-2: # 정방향 가로
                if words[i+1][j] == 'E' and words[i+2][j] == 'E':
                    cnt +=1
            if j < M-2: # 정방향 세로
                if words[i][j+1] == 'E' and words[i][j+2] == 'E':
                    cnt +=1
            if i > 1 : # 역방향 가로
                if words[i-1][j] == 'E' and words[i-2][j] == 'E':
                    cnt +=1
            if j > 1: # 역방향 세로
                if words[i][j-1] == 'E' and words[i][j-2] == 'E':
                    cnt +=1
            if i < N-2 and j < M-2: # \ 정방향
                if words[i+1][j+1] == 'E' and words[i+2][j+2] == 'E':
                    cnt +=1 
            if i > 1 and j > 1: # \ 역방향
                if words[i-1][j-1] == 'E' and words[i-2][j-2] == 'E':
                    cnt +=1
            if i < N-2 and j > 1: # / 정방향
                if words[i+1][j-1] == 'E' and words[i+2][j-2] == 'E':
                    cnt +=1
            if i > 1 and j < M-2: # / 역방향
                if words[i-1][j+1] == 'E' and words[i-2][j+2] == 'E':
                    cnt +=1

print(cnt)