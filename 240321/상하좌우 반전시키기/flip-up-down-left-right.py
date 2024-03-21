import sys
n = int(input())
numbers = [list(map(int, input().split())) for _ in range(n)]

if n == 1:
    print(0 if numbers[0][0] == 1 else -1)
    sys.exit()

min_push = n*n
dxs,dys = [0,1,0,-1],[1,0,-1,0]
def next_choose(x,y, push_cnt):
    if y == n-1:
        choose(x+1,y, push_cnt)
    else:
        choose(x,y+1, push_cnt)

def is_push(x,y):
    if x > 0:
        if numbers[x-1][y] == 1:
            return False
    if x == n-1 and y > 0:
        if numbers[x][y-1] == 1:
            return False
    return True
def is_not_push(x,y):
    if x > 0:
        if numbers[x-1][y] == 0:
            return False
    if x == n-1 and y > 0:
        if numbers[x][y-1] == 0:
            return False
    return True
def is_range(x,y):
    return x < n and x >= 0 and y < n and y >= 0
def push(x,y):
    for dx,dy in zip(dxs,dys):
        nx, ny = x + dx, y + dy
        if is_range(nx,ny):
            numbers[nx][ny] = 1 if numbers[nx][ny] == 0 else 0
def choose(x,y, push_cnt):
    global min_push
    if x == n-1 and y == n-1:
        if numbers[x][y] == 1 and numbers[x-1][y] == 1 and numbers[x][y-1] == 1:
            min_push = min(min_push, push_cnt)
        elif numbers[x][y] == 0 and numbers[x-1][y] == 0 and numbers[x][y-1] == 0:
            min_push = min(min_push, push_cnt + 1)
        return
    if is_push(x,y):
        push(x,y)
        next_choose(x,y, push_cnt+1)
        push(x,y)
    if is_not_push(x,y):
        next_choose(x,y, push_cnt)
choose(0,1,0)
if min_push == n*n:
    min_push = -1
print(min_push)