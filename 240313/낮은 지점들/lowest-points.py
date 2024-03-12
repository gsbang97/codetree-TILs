n = int(input())
points = {}
for _ in range(n):
    x,y = map(int, input().split())
    if x in points.keys():
        if y < points[x]:
            points[x] = y
    else:
        points[x] = y
s = 0
for _,v in points.items():
    s += v
print(s)