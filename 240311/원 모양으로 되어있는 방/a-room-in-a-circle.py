import sys

N = int(input())

rooms = [int(input()) for _ in range(N)]
min_cost = sys.maxsize
for i in range(N):
    cost = 0
    for j in range(N):
        room_num = i+j
        if room_num >= N:
            room_num -= N
        cost += rooms[room_num] * j
    min_cost = min(min_cost,cost)
print(min_cost)