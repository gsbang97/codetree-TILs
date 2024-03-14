# 숫자 0, 1로만 이루어진 n * n 격자
# k개의 시작점으로부터 상하좌우 인접한 곳으로만 이동
# 도달 가능한 칸의 수를 구하는 프로그램
# 숫자 0 : 이동할 수 있는 곳
# 숫자 1 : 이동할 수 없는 곳
from collections import deque

def is_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x,y):
    if not is_range(x,y):
        return False
    if visited[x][y]:
        return False
    if numers[x][y] == 1:
        return False
    return True

def bfs(x,y):
    global cnt
    que = deque([(x,y)])
    dxs, dys = [0,1,0,-1],[1,0,-1,0]    
    while que:
        cx,cy = que.popleft()
        for dx,dy in zip(dxs, dys):
            nx, ny = cx+dx, cy+dy
            if can_go(nx,ny):
                visited[nx][ny] = True
                cnt += 1
                que.append((nx,ny))

n,k = map(int, input().split())
numers = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n) ]
cnt = 0
for _ in range(k):
    r,c = map(int, input().split())
    r,c = r-1, c-1
    if can_go(r,c):
        visited[r][c] = True
        cnt += 1
        bfs(r,c)

print(cnt)