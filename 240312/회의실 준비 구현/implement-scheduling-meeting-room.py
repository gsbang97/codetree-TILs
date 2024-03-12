from functools import cmp_to_key
# n : 회의 요청 수
n = int(input())
# (시작, 끝)
meeting = [tuple(map(int, input().split())) for _ in range(n)]

def compare(x,y):
    if x[0] < y[0]:
        return -1
    elif x[0] == y[0]:
        x_time = x[1]-x[0]
        y_time = y[1]-y[0]
        if x_time < y_time:
            return -1
        elif x_time == y_time:
            return 0
        else:
            return 1
    else:
        return 1

max_cnt = 0
meeting.sort(key=lambda x : x[0])
cnt = 0
start = 100000
end = 0
for meet in meeting:
    if end <= meet[0] and start:
        end = meet[1]
        cnt +=1
# meeting.sort(key=lambda x : x[1]-x[0])
max_cnt = max(max_cnt, cnt)

meeting.sort(key=lambda x : x[1])
cnt = 0
start = 100000
end = 0
for meet in meeting:
    if end <= meet[0] and start:
        end = meet[1]
        cnt +=1
max_cnt = max(max_cnt, cnt)
# meeting.sort(key=cmp_to_key(compare))
# print(meeting)
# cnt = 0
# end = 0
# for meet in meeting:
#     if end <= meet[0]:
#         end = meet[1]
#         cnt +=1

print(max_cnt)