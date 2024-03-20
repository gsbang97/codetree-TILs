import heapq

n = int(input())
bombs = []

for _ in range(n):
    point, time = map(int, input().split())
    heapq.heappush(bombs,(-point, time))

can_time = [True for _ in range(10001)]
score = 0
while bombs:
     point,time = heapq.heappop(bombs)
     for t in range(time-1, -1, -1):
        if can_time[t]:
            can_time[t] = False
            score += -point
            break

print(score)