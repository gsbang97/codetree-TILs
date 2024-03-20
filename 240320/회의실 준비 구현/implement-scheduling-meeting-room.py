import heapq

n = int(input())
meetings = []

for _ in range(n):
    s,e = map(int, input().split())
    heapq.heappush(meetings, (e,e-s,s))

meeting_cnt = 0
end_time = 0
while meetings:
    e,dist,s = heapq.heappop(meetings)
    if end_time <= s:
        meeting_cnt += 1
        end_time = e

print(meeting_cnt)