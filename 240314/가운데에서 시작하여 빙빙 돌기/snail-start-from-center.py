n = int(input())

x,y = n//2, n//2

dxs,dys = [0,-1,0,1], [1,0,-1,0]
numbers = [[0 for _ in range(n)] for _ in range(n)] 
numbers[x][y] = 1
d = 3
for i in range(2,n*n+1):
    nd = (d+1)%4
    nx,ny = x+dxs[nd], y+dys[nd]
    if numbers[nx][ny] == 0:
        d = (d+1)%4
    x,y = x+dxs[d], y+dys[d]
    numbers[x][y] = i
for i in range(n):
    print(*numbers[i])