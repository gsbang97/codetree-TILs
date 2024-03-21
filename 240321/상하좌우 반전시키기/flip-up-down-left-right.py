import sys
n = int(input())
# sys.setrecursionlimit(max(1000,n**3)) 
numbers = [list(map(int, input().split())) for _ in range(n)]

if n == 1:
    print(0 if numbers[0][0] == 1 else -1)
    sys.exit()
def is_range(x,y):
    return x < n and x >= 0 and y < n and y >= 0
def push(x,y):
    numbers[x][y] = 1 if numbers[x][y] == 0 else 0
    dxs, dys = [0,0,1],[1,-1,0]
    for dx,dy in zip(dxs,dys):
        nx, ny = x + dx, y + dy
        if is_range(nx,ny):
            numbers[nx][ny] = 1 if numbers[nx][ny] == 0 else 0
answer = 0
for i in range(1,n):
    for j in range(n):
        if i == n-1 and j > 0:
           if numbers[i-1][j] != numbers[i][j-1] :
            answer = -1
            break
        if numbers[i-1][j] == 0:
            answer += 1  
            push(i,j)
        
print(answer)