alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # 26

n,m = map(int, input().split())

square = [['-' for _ in range(m)] for _ in range(n)]

dxs, dys = [0,1,0,-1],[1,0,-1,0]
x,y = 0,0
d = 0
square[x][y] = 'A'
def is_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < m
for i in range(1,n*m): 
    nx,ny = x+dxs[d], y+dys[d]
    if not is_range(nx,ny) or square[nx][ny] != '-':
        d = (d+1)%4
    x,y = x+dxs[d], y+dys[d]
    square[x][y] = alpha[i%26]
for i in range(n):
    print(*square[i])