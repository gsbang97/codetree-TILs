# BFS

# n * m 크기의 이차원 영역의 좌측 상단에서 출발하여 우측 하단까지 뱀에게 물리지 않고 탈출
# 이동을 할 때에는 반드시 상하좌우에 인접한 칸으로만 이동할 수 있음
# 뱀이 있는 칸으로는 이동을 할 수 없습니다
from collections import deque

n,m = map(int, input().split())
snake_map = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]
dxs,dys = [0,1,0,-1],[1,0,-1,0]
def is_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < m
def can_go(x,y):
    if not is_range(x,y):
        return False
    if visited[x][y]:
        return False
    if snake_map[x][y] == 0:
        return False
    return True
que = deque([[0,0]])
visited[0][0] = True
while que:
    (x,y) = que.popleft()
    if x == n-1 and y == m-1:
        break
    for dx,dy in zip(dxs,dys):
        nx,ny = x+dx, y+dy
        if can_go(nx,ny):
            visited[nx][ny] = True
            que.append([nx,ny])

if visited[-1][-1]:
    print(1)
else:
    print(0)