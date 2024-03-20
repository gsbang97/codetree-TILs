# import sys
n = int(input())

max_gain = 0
min_cost = -1
for cost in map(int, input().split()):
    if min_cost == -1:
        min_cost = cost
        continue
    min_cost = min(min_cost, cost)
    max_gain = max(max_gain, cost - min_cost)
print(max_gain)