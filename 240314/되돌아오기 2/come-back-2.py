# 좌표평면 위 (0, 0)에서 북쪽을 향한 상태에서 움직이는 것을 시작
# N개의 명령에 따라 총 N번 움직임
# L이 주어지면 왼쪽으로 90도 방향 전환
# R이 주어지면 오른쪽으로 90도 방향전환
# F가 주어지면 바라보고 있는 방향으로 한칸 이동
# 1초에 한 칸씩 움직이며, 회전에도 1초의 시간이 걸린다
# 몇 초 뒤에 처음으로 다시 (0, 0)에 돌아오게 되는지 출력
import sys

x,y = 0,0

dx,dy = [1,0,-1,0],[0,1,0,-1]
d = 0
for t,command in enumerate(input(), start = 1):
    if command == 'L': # 왼쪽 90도 방향 전환
        d -=1
        if d < 0:
            d = 3
    elif command == 'R': # 오른쪽 90도 방향 전환
        d = (d+1)%4
    elif command == 'F': # 한 칸 이동
        x,y = x+dx[d], y+dy[d]
        if x == 0 and y == 0:
            print(t)
            sys.exit()

print(-1)