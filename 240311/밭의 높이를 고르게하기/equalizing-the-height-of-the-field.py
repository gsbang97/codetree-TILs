import sys
N, H, T = map(int, input().split())

heights = list(map(int, input().split()))

min_cost = sys.maxsize
for i in range(N-T):
    cost = 0
    for idx in range(i, i+T):
        cost += abs(H-heights[idx])
    min_cost = min(min_cost,cost)
print(min_cost)