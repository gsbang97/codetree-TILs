# n * n 크기의 격자에 1이상 100이하의 숫자가 각 칸에 하나씩 주어짐
# 상하좌우로 인접한 칸끼리 같은 숫자로 이루어져 있는 경우 하나의 블럭으로 생각
# 블럭을 이루고 있는 칸의 수가 4개 이상인 경우 해당 블럭은 터지게 됩니다.

# 초기 상태가 주어졌을 때 터지게 되는 블럭의 수와, 최대 블럭의 크기를 구하는 프로그램

n = int(input())

numbers = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]
blocks = []
dxs,dys = [0,1,0,-1],[1,0,-1,0]

def is_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < n

def block_check(x,y):
    for dx,dy in zip(dxs,dys):
        nx,ny = x+dx, y+dy
        if is_range(nx,ny) and not visited[nx][ny] and numbers[nx][ny] == numbers[x][y]:
            visited[nx][ny] = True
            blocks[-1] += 1
            block_check(nx,ny)

bomb_cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            blocks.append(1)
            visited[i][j] = True
            block_check(i,j)
            if blocks[-1] >= 4:
                bomb_cnt += 1

print(bomb_cnt, max(blocks))