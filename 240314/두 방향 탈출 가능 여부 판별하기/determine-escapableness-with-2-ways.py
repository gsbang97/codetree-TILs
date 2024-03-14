# n * m 크기의 이차원 영역
# 좌측 상단(0,0)에서 출발하여 우측 하단(n-1,m-1)까지 뱀에게 물리지 않고 탈출
# 이동을 할 때에는 반드시 아래와 오른쪽 2방향 중 인접한 칸으로만 이동할 수 있음
# 뱀이 있는 칸으로는 이동할 수 없음
import sys

n,m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
d = [(1,0),(0,1)]
def is_range(x,y):
    return x<n and y<m
def escape(x,y):
    if x == n-1 and y == m-1:
        print(1)
        sys.exit()
    for dx,dy in d:
        nx,ny = x+dx, y+dy
        if is_range(nx,ny) and not visited[nx][ny] and board[nx][ny] == 1:
            visited[nx][ny] = True
            escape(nx,ny)

visited[0][0] = True
escape(0,0)
print(0)