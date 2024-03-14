# n * m크기의 직사각형에 숫자 1부터 순서대로 증가시키며 달팽이 모양으로 채우는 코드

n,m = map(int, input().split())

dx,dy = [1,0,-1,0],[0,1,0,-1]

numbers = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < m

numbers[0][0] = 1
d = 0
x,y = 0,0
for i in range(2,n*m +1):
    nx,ny = x+dx[d], y+dy[d]
    if not in_range(nx,ny) or numbers[nx][ny] != 0:
        d = (d+1)%4
    x,y = x+dx[d], y+dy[d]
    numbers[x][y] = i
for i in range(n):
    print(*numbers[i])