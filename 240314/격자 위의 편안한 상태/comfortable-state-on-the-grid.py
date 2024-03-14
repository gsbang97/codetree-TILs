# N * N 크기의 격자 위에 총 M번에 걸쳐 색칠
# 한 번에 한 칸만 색칠하며, 색칠을 한 직후 해당 칸이 '편안한 상태'에 놓여 있는지를 확인
# ‘편안한 상태’
# - 위 아래 양옆으로 인접한 4개의 칸 중 격자를 벗어나지 않는 칸에 색칠되어 있는 칸이 정확히 3개인 경우
# 색칠할 칸이 주어질 때마다 해당 칸을 칠한 직후 막 칠한 칸이 편안한 상태에 있는지를 계속 알아내는 프로그램

n, m = map(int, input().split())
dxs,dys = [0,1,0,-1],[1,0,-1,0]
board = [[0 for _ in range(n+1)] for _ in range(n+1)]

def in_range(x,y):
    return x > 0 and x <= n and y > 0 and y <= n
for _ in range(m):
    r,c = map(int, input().split())
    cnt = 0
    for dx,dy in zip(dxs,dys):
        x,y = r+dx, c+dy
        if in_range(x,y) and board[x][y] == 1:
            cnt += 1
    board[r][c] = 1
    if cnt == 3:
        print(1)
    else:
        print(0)