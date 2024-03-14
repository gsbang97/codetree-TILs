# 숫자 0과 1로만 이루어진 n * n 크기의 격자 상태
# 각 칸 중 상하좌우로 인접한 칸 중 숫자 1이 적혀 있는 칸의 수가 3개 이상인 곳의 개수
# 인접한 곳이 격자를 벗어나는 경우에는 숫자 1이 적혀있지 않은 것

n = int(input())

numbers = [list(map(int, input().split())) for _ in range(n)]

dxs,dys = [1,0,-1,0],[0,1,0,-1]

def in_range(x,y):
    return x>=0 and x < n and y >=0 and y < n
ans = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for dx,dy in zip(dxs,dys):
            x,y = dx+i, dy+j
            if in_range(x,y) and numbers[x][y] == 1:
                cnt += 1
        if cnt>=3:
            ans += 1

print(ans)