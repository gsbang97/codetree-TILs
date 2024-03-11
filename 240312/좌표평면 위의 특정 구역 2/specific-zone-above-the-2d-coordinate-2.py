N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

min_width = 40000*40000
for i in range(N):
    min_x = 40000
    max_x = 1
    min_y = 40000
    max_y = 1
    for j in range(N):
        if i == j:
            continue
        x,y = points[j]
        min_x = min(min_x,x)
        max_x = max(max_x,x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    width = (max_x-min_x) * (max_y - min_y)
    min_width = min(min_width, width)
print(min_width)