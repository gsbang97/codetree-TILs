n = int(input())

meetings = [tuple(map(int, input().split())) for  _ in range(n)]

meetings.sort(key = lambda x : (x[1],x[0]))
end_time = 0
cnt = 0
for s,e in meetings:
    if s >= end_time:
        end_time = e
    else:
        cnt += 1
print(cnt)