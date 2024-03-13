# n : 격자판의 크기 (n*n)
n = int(input())
# mat : 폭탄의 정보(1이 폭탄 위치)
mat = [list(map(int, input().split())) for _ in range(n)]
# 폭탄 종류 
# 1. (-2,0), (-1,0), (0,0), (1,0), (2,0)
# 2. (-1,0), (0,-1), (0,0), (0,1), (1,0)
# 3. (-1,-1), (-1,1), (0,0), (1,-1), (1,1)
bombs = [
    ((-2,0), (-1,0), (0,0), (1,0), (2,0)),
    ((-1,0), (0,-1), (0,0), (0,1), (1,0)),
    ((-1,-1), (-1,1), (0,0), (1,-1), (1,1))
]

bomb_map = [[0 for _ in range(n)] for _ in range(n)]
bomb_xy = []
for x in range(n):
    for y in range(n):
        if mat[x][y] == 1:
            bomb_xy.append((x,y))
max_cnt = 0
def check_bomb():
    cnt = 0
    for x in range(n):
        for y in range(n):
            if bomb_map[x][y] > 0:
                cnt += 1
    return cnt
bomb_cnt = len(bomb_xy)
def choose_bomb(bomb_cnt):
    global max_cnt
    if bomb_cnt == 0:
        cnt = check_bomb()
        max_cnt = max(max_cnt, cnt)
    else:
        x,y = bomb_xy[bomb_cnt-1]
        for bomb in bombs:
            for (i,j) in bomb:
                dx,dy = x+i, y+j
                if dx>=0 and dx<n and dy >= 0 and dy < n:
                    bomb_map[dx][dy]+=1
            choose_bomb(bomb_cnt-1)
            for i,j in bomb:
                dx,dy = x+i, y+j
                if dx>=0 and dx<n and dy >= 0 and dy < n:
                    bomb_map[dx][dy]-=1

choose_bomb(bomb_cnt)


print(max_cnt)