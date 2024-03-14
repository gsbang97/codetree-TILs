# N x N크기의 정사각형 모양의 격자 정보
# 가운데 위치에서 북쪽을 향한 상태로 움직이는 것을 시작
# T개의 명령에 따라 움직이며, 명령어는 L,R,F
# L은 왼쪽으로 90도 방향 전환
# R은 오른쪽으로 90도 방향 전환
# F가 주어지면 바라보고 있는 방향으로 한칸 이동
n,t = map(int, input().split())

commands = input()

numbers = [list(map(int, input().split())) for _ in range(n)]

dx,dy = [-1,0,1,0],[0,1,0,-1]
x,y = n//2, n//2
ans = numbers[x][y]
d = 0
def is_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < n
for command in commands:
    if command == 'L': # 왼쪽으로 
        d = (d+3)%4
    elif command == 'R': # 오른쪽으로 
        d = (d+1)%4
    elif command == 'F': # 앞으로 직진
        nx,ny = x+dx[d], y+dy[d]
        if is_range(nx,ny):
            x,y = nx,ny
            ans += numbers[x][y]
print(ans)