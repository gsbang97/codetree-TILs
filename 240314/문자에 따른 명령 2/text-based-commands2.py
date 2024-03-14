# 좌표평면 위 (0, 0)에서 북쪽을 향한 상태에서 움직이는 것을 시작
# N개의 명령에 따라 총 N번 움직임
# 명령 L이 주어지면 왼쪽으로 90도 방향 전환
# 명령 R이 주어지면 오른쪽으로 90도 방향전환
# 명령 F가 주어지면 바라보고 있는 방향으로 한칸 이동

point = [0,0]

dx,dy = [0,1,0,-1], [1,0,-1,0]
orientation = 0
for command in input():
    if command == 'L': # 왼쪽으로 방향전환
        orientation -= 1
        if orientation < 0 :
            orientation = 3
    elif command == 'R': # 오른쪽으로 방향전환
        orientation += 1
        if orientation > 3:
            orientation = 0
    elif command == 'F':
        point[0] += dx[orientation]
        point[1] += dy[orientation]
print(*point)