# n개의 회의 요청
# 취소하는 회의 개수를 최소화하여 원활하게 진행할 수 있는 회의의 수

n = int(input())
# (시작시간, 끝 시간)
meetings = [tuple(map(int, input().split())) for _ in range(n)]

min_cnt = 100000

meetings.sort(key = lambda x : x[0])
cnt = 0
end = 0
for s,e in meetings:
    if end <= s:
        end = e
    else:
        cnt +=1
min_cnt = min(min_cnt, cnt)

meetings.sort(key = lambda x : x[1])
cnt = 0
end = 0
for s,e in meetings:
    if end <= s:
        end = e
    else:
        cnt +=1
min_cnt = min(min_cnt, cnt)

print(min_cnt)