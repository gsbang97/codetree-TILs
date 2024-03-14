# n * m크기의 직사각형에 숫자 1부터 순서대로 증가시키며 달팽이 모양으로 채우는 코드
# n : 행(row), m : 열(column)을 의미

n,m = map(int, input().split())

def in_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < m

dx,dy = [0,1,0,-1], [1,0,-1,0]
d = 0
ans = [[0 for _ in range(m)] for _ in range(n)]
cx,cy = 0,0
ans[0][0] = 1
for i in range(2,n*m+1):
    nx, ny = cx+dx[d], cy+dy[d]
    if (not in_range(nx,ny)) or ans[nx][ny] != 0:
        d += 1
        if d == 4:
            d = 0
    cx += dx[d]
    cy += dy[d]
    ans[cx][cy] = i
for i in range(n):
    print(*ans[i])