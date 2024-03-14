# N×M 크기의 격자안에 빙하의 정보가 주어짐
# 격자의 가장 바깥 부분은 항상 빙하가 아니고, 빙하를 제외한 나머지 위치에는 전부 물이 채워져 있습니다.
# 숫자 1 : 빙하, 숫자 0 : 물
# 빙하는 1초에 한 번씩 물에 닿아있는 부분들이 동시에 녹습니다
# 빙하로 둘러싸여있는 물의 경우에는 붙어있는 빙하를 녹이지 못합니다. 
# 닿아있다 : 말은 상하좌우로 인접한 경우
from collections import deque

n,m = map(int, input().split())

ice = [list(map(int, input().split())) for _ in range(n)]

ice_cnt = sum([sum(i) for i in ice])
ans = 0
cnt = 0
visited = [[False for _ in range(m)] for _ in range(n)]
def init_visit(cnt):
    for i in range(cnt,n-cnt):
        for j in range(cnt, m-cnt):
            visited[i][j] = False
dxs,dys = [0,1,0,-1],[1,0,-1,0]

def is_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < m

def can_go(x,y):
    return is_range(x,y) and not visited[x][y]

while(ice_cnt != 0):
    ans = 0
    init_visit(cnt)
    visited[cnt][cnt] = True
    que = deque([(cnt, cnt)])
    cnt += 1
    while que:
        x,y = que.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx, y+dy
            if can_go(nx,ny):
                visited[nx][ny] = True
                if ice[nx][ny] == 1:
                    ans+=1
                    ice_cnt-=1
                    ice[nx][ny] = 0
                else:
                    que.append((nx,ny))
    
print(cnt, ans)