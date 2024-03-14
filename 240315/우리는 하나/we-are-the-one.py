# n * n 크기의 격자로 이루어져 있는 나라의 정보
# 각 칸마다 하나의 도시가 있고, 각 도시마다의 높이 정보가 주어짐
# k개의 도시를 겹치지 않게 적절하게 골라, 
# 골라진 k개의 도시로부터 갈 수 있는 서로 다른 도시의 수를 최대화
# 이동은 상하좌우로 인접한 도시간의 이동만 가능
# 두 도시간의 높이의 차가 u 이상 d 이하인 경우에만 가능
from collections import deque
import sys

n,k,u,d = map(int, input().split())
sys.setrecursionlimit(1000*n)
heights = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]
starts = []

city_cnt = 0
max_cnt = 0

def init_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def is_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x,y,height):
    return is_range(x,y) and abs(heights[x][y] - height) >= u and abs(heights[x][y] - height) <= d and not visited[x][y]

def bfs(x,y):
    if visited[x][y]:
        return
    global city_cnt
    city_cnt += 1
    que = deque([(x,y)])
    visited[x][y] = True
    dxs,dys = [0,1,0,-1],[1,0,-1,0]
    while que:
        cx,cy = que.pop()
        height = heights[cx][cy]
        for dx,dy in zip(dxs, dys):
            nx,ny = cx+dx, cy+dy
            if can_go(nx,ny,height):
                city_cnt += 1
                visited[nx][ny] = True
                que.append((nx,ny))
def choose_city(cnt,num):
    # print(cnt, num)
    global city_cnt, max_cnt
    if cnt == k:
        city_cnt = 0
        init_visited()
        for start in starts:
            bfs(start//n, start%n)
        max_cnt = max(max_cnt, city_cnt)
        # print(max_cnt,city_cnt, num)
        return
    
    for i in range(num+1,n*n):
        
        starts.append(i)
        choose_city(cnt+1, i)
        starts.pop()
    if num<n*n:
        choose_city(cnt,num+1)

choose_city(0,0)

print(max_cnt)