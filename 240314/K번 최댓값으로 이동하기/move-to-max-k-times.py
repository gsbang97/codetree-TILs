# n*n 크기의 격자에 1이상 100이하의 숫자
# 특정 위치에서 시작
# 이동하기 위한 조건
# 1. 시작 위치에 적혀있는 숫자를 x라고 했을 때, 
# 시작 위치에서 출발하여 인접한 칸들 중 적혀있는 숫자가 x보다 작은 곳으로는 전부 이동이 가능합니다.
# 1-1. 하지만 만약에 아래 시작 위치의 상하좌우가 시작 숫자보다 큰 숫자들로 둘러싸여져 있으면 이동이 불가
# 2. 1번 조건을 만족하며 도달할 수 있는 칸들에 적혀있는 숫자 중 최댓값으로 이동합니다.
# 3. 2번 조건을 만족하는 숫자가 여러개 일경우, 행 번호가 가장 작은 곳으로 이동합니다.
# 4. 2번 조건을 만족하고, 행 번호도 같은 숫자가 여러개 일경우, 열 번호가 가장 작은 곳으로 이동
# k번 반복한 이후의 위치를 구하는 프로그램
from collections import deque

# n : 격자 크기, k : 반복 횟수
n,k = map(int, input().split())

# numbers : 격자
numbers = [list(map(int, input().split())) for _ in range(n)]

# 시작위치
r,c = map(int, input().split())
r ,c = r-1, c-1
visited = [[False for _ in range(n)] for _ in range(n)] 
def clear_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def is_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x,y,number):
    return is_range(x,y) and not visited[x][y] and numbers[x][y] < number

def bfs(x,y):
    que = deque([(x,y)])
    dxs, dys = [0,1,0,-1],[1,0,-1,0]
    max_num = [n,n,-1]
    clear_visited()
    visited[x][y] = True
    number = numbers[x][y]
    while que:
        cx,cy = que.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy

            if can_go(nx, ny, number):
                if numbers[nx][ny] > max_num[2]:
                    max_num = [nx,ny,numbers[nx][ny]]
                elif numbers[nx][ny] == max_num[2]:
                    if nx < max_num[0]:
                        max_num = [nx,ny,numbers[nx][ny]]
                    elif nx == max_num[0]:
                        if ny < max_num[1]:
                            max_num = [nx,ny,numbers[nx][ny]]
                visited[nx][ny] = True
                que.append((nx,ny))
    return max_num[0], max_num[1]
# k번 반복
for _ in range(k):
    nr,nc = bfs(r,c)
    if nr == r and nc == c:
        break
    r,c = nr,nc

print(r+1, c+1)