# (0, 0)에서 시작하여 총 N번 움직임
# N번에 걸쳐 움직이려는 방향과 움직일 거리
# 1초에 한 칸씩 움직인다고 했을 때, 몇 초 뒤에 처음으로 다시 (0, 0)에 돌아오게 되는지를 판단
import sys

n = int(input())

commands = [input().split() for _ in range(n)]

direction = {}
direction['W'] = (0,-1)
direction['S'] = (-1,0)
direction['N'] = (1,0)
direction['E'] = (0,1)
x,y = 0,0
t = 0 

for command, dist in commands:
    for _ in range(int(dist)):
        dx,dy = direction[command]
        x,y = x+dx, y+dy
        t += 1
        if x == 0 and y == 0:
            print(t)
            sys.exit()

print(-1)