# n * n크기의 이차원 영역에 사람 혹은 벽
# 상하좌우의 인접한 영역에 있는 사람들은 같은 마을에 있는 것으로 간주
# 총 마을의 개수와 같은 마을에 있는 사람의 수를 오름차순으로 정렬

n = int(input())
vilige_map = [list(map(int, input().split())) for _ in range(n)]
vilige_cnt = 0
peoples = []
dxs,dys = [0,1,0,-1],[1,0,-1,0]
def can_go(x,y):
    return x >= 0 and x < n and y >= 0 and y < n and vilige_map[x][y] == 1
def find_vilige(x,y):
    
    for dx,dy in zip(dxs,dys):
        nx,ny = x+dx, y+dy

        if can_go(nx,ny):
            vilige_map[nx][ny] = 0
            peoples[-1] += 1
            find_vilige(nx,ny)
for i in range(n):
    for j in range(n):
        if vilige_map[i][j] == 1 :
            peoples.append(1)
            vilige_map[i][j] = 0
            find_vilige(i,j)
peoples.sort()
print(len(peoples))
for man in peoples:
    print(man)