import heapq

n = int(input())
bombs = []

for _ in range(n):
    point, time = map(int, input().split())
    heapq.heappush(bombs,(time, -point))

current_time = 0
score = 0
while bombs:
     time, point = heapq.heappop(bombs)
     if current_time < time :
        score += -point
        current_time += 1

print(score)