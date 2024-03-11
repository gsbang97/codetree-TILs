import sys

N = int(input())

checkpoints = [tuple(map(int, input().split())) for _ in range(N)]

min_dist = sys.maxsize
for i in range(1,N-1):
    x,y = checkpoints[0]
    dist = 0
    for j in range(1,N):
        if i == j :
            continue
        next_x, next_y = checkpoints[j]
        dist += abs(x-next_x) + abs(y-next_y)
        x,y = next_x,next_y
    min_dist = min(min_dist, dist)
print(min_dist)