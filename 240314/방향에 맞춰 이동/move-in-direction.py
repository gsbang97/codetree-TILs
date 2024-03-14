# (0, 0)에서 시작하여 총 N번 움직임
# N번에 걸쳐 움직이려는 방향과 움직일 거리가 주어졌을 때, 최종 위치를 출력하는 프로그램

# dx, dy 테크닉 활용

n = int(input())

point = [0,0]
where = {
    'N' : (0,1),
    'E' : (1,0),
    'S' : (0,-1),
    'W' : (-1,0)
}
for _ in range(n):
    direction, dist = input().split()
    dist = int(dist)
    point[0] += dist * where[direction][0]
    point[1] += dist * where[direction][1]
print(*point)