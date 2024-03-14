# 숫자 0, 1로만 이루어진 n * n 격자
# 주어진 돌 중 m개의 돌만 적절하게 치워 k개의 시작점으로부터 상하좌우 인접한 곳으로만 이동
# 도달 가능한 칸의 수를 최대로 하는 프로그램
from collections import deque

n,k,m = map(int, input().split())

numbers = [list(map(int, input().split())) for _ in range(n)]
starts = [list(map(int, input().split())) for _ in range(k)]
visited = [[False for _ in range(n)] for _ in range(n)]
stones = []
for i in range(n):
    for j in range(n):
        if numbers[i][j] == 1:
            stones.append([i,j])
stone_cnt = len(stones)
# stone_cnt중 m개의 돌 선택해서 치우기
def clear_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def is_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x,y):
    return is_range(x,y) and numbers[x][y] == 0 and not visited[x][y]

def bfs(x,y):
    if not can_go(x,y):
        return
    global dist
    dist += 1
    que = deque([(x,y)])
    visited[x][y] = True
    dxs, dys = [0,1,0,-1],[1,0,-1,0]
    while que:
        cx,cy = que.popleft()
        for dx,dy in zip(dxs, dys):
            nx,ny = cx + dx, cy + dy
            if can_go(nx,ny):
                visited[nx][ny] = True
                dist += 1
                que.append((nx,ny))

max_dist = 0
dist = 0
def clean_stone(cnt,num):
    global max_dist, dist
    if cnt == m:
        
        clear_visited()
        dist = 0
        for start in starts:
            x,y = start[0] - 1 , start[1] - 1
            bfs(x,y)

        max_dist = max(max_dist, dist)
        return
    for i in range(num+1,stone_cnt):
        x,y = stones[i]
        numbers[x][y] = 0
        clean_stone(cnt+1, i)
        numbers[x][y] = 1
    if num+1 < stone_cnt:
        clean_stone(cnt, num+1)

    
clean_stone(0,-1)
print(max_dist)