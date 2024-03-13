n = int(input())
points = [list(map(int, input().split()))+[i] for i in range(1,n+1)]

points.sort(key = lambda x: (abs(x[0])+abs(x[1]), x[2]))

for point in points:
    print(point[2])