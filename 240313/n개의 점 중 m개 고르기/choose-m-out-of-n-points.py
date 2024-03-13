import math
import sys
# 가장 먼 두 점 사이의 거리값이 최소

n, m = map(int, input().split())

points = [tuple(map(int, input().split())) for _ in range(n)]
min_dist = sys.maxsize
point_list = []

def cal_dist(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )

def cal_max_dist(max_dist, p):
    for point in point_list:
        
        max_dist = max(max_dist, cal_dist(p,point))
    return max_dist
def choose(cnt, max_dist, idx):
    global min_dist
    if cnt == m:
        min_dist = min(min_dist, max_dist)
        return

    if cnt == 0:
        for i in range(idx+1, n):
            point_list.append(points[i])
            choose(cnt+1, 0,i)
            point_list.pop()
    else:
        for i in range(idx+1, n):
            max_value = cal_max_dist(max_dist,points[i])
            point_list.append(points[i])
            choose(cnt+1, max_value,i)
            point_list.pop()

choose(0,0,-1)

print(min_dist)