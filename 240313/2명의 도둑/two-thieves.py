# N : 방의 크기 (N x N)
# M : 도둑이 훔칠 수 있는 영역의 수 
# C : 도둑이 가져갈 수 있는 무게
N,M,C = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
max_score = 0
max_calc_score = 0
def calc_score(cnt, x,y,c,s):
    global max_calc_score
    if cnt == M:
        max_calc_score = max(max_calc_score, s)
        return
    w = room[x][y+cnt]
    if c >= w:
        calc_score(cnt+1,x,y,c-w, s + w**2)
    calc_score(cnt+1,x,y,c,s)


def choose(cnt, x,y,score):
    global max_score, max_calc_score
    # print(cnt, score)
    if cnt == 2:
        max_score = max(max_score, score)
        return
    for i in range(x,N):
        if i == x:
            for j in range(y,N-M):
                max_calc_score = 0
                calc_score(0,i,j,C,0)
                choose(cnt+1, i,j+M, score + max_calc_score)
        else:
            for j in range(N-M):
                max_calc_score = 0
                calc_score(0,i,j,C,0)
                choose(cnt+1, i,j+M, score + max_calc_score)

    
choose(0,0,0,0)

print(max_score)