# N×M 크기의 격자로 구성된 마을
# 격자마다 한 집을 의미하며, 각 집의 높이는 1이상 100이하의 숫자
# 비가 K(K≥1)만큼 온다고 한다면, 마을에 있는 집들 중 높이가 K 이하인 집들은 전부 물에 잠김
# 대책을 세우기 위해 미리 각 K에 따라 안전 영역의 개수가 어떻게 달라지는지를 보려고 함
# 안전 영역이란 잠기지 않은 집들로 이루어져 있으며, 잠기지 않은 집들끼리 서로 인접해 있는 경우 동일한 안전 영역

n,m = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(n)]
max_k = (max([max(height) for height in heights]))
safe_vilige = [[True for _ in range(m)] for _ in range(n)]
dxs,dys = [0,1,0,-1],[1,0,-1,0]
visited = [[False for _ in range(m)] for _ in range(n)]

def is_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < m

def check_safe(x,y,height):
    for dx,dy in zip(dxs, dys):
        nx,ny = x + dx, y + dy
        # print(nx,ny)
        if is_range(nx,ny) and heights[nx][ny] > height and not visited[nx][ny]:
            
            visited[nx][ny] = True
            check_safe(nx,ny,height)

max_cnt = [1,0]
for height in range(1,max_k):
    visited = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if heights[i][j] > height and not visited[i][j]:
                visited[i][j] = True
                check_safe(i,j,height)
                cnt += 1
    if cnt > max_cnt[1]:
        max_cnt[1] = cnt
        max_cnt[0] = height
print(*max_cnt)