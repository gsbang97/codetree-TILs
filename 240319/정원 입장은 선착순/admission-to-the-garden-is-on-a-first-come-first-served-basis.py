# 1~N 명의 사람들
# i번 사람은 a_i 시간에 정원 입구에 도착해서 t_i시간동안 정원에 머무르다 간다.
# 정원에는 한 번에 한 명의 사람만이 들어갈 수 있다.
# i번 사람이 정원 입구에 도착했을 때, 이미 누군가가 정원에 있다면 
# 정원 안에 있는 사람이 떠날때 까지 기다렸다가 이후에 정원을 출입할 수 있습니다.
# 기다리는 사람이 여러명이라면 번호표의 숫자가 작은 사람부터 들어갈 수 있습니다. 
# 모든 사람이 정원을 한 번씩 들려서 머물렀다 갈 때, 이들 중 가장 오래 기다려야 하는 사람이 기다리는 시간을 구하는 프로그램을 작성해보세요.

import heapq

n = int(input())
# 도착시간, 머무르는 시간
people = [[i]+list(map(int, input().split())) for i in range(1,n+1)]

people.sort(key=lambda x : x[1])
# print(people)
waiting = []
wait_time = []
able_time = 0

for number, arrive, time in people:
    # print(able_time, "able")
    if arrive < able_time:
        heapq.heappush(waiting,(number,arrive,time))
    else:
        while arrive > able_time and waiting:
            # print(waiting)
            next_number, next_arrive, next_time = heapq.heappop(waiting)
            # print(next_number, able_time, next_arrive)
            heapq.heappush(wait_time, (-(able_time - next_arrive), next_number))
            able_time += next_time
        if able_time < arrive:
            if able_time == 0:
                able_time = arrive
            heapq.heappush(wait_time, (0, number))
            able_time += time
        else:
            heapq.heappush(waiting,(number,arrive,time))
while waiting:
    next_number, next_arrive, next_time = heapq.heappop(waiting)
    heapq.heappush(wait_time, (-(able_time - next_arrive), next_number))
    able_time += next_time
# print(wait_time)
print(-heapq.heappop(wait_time)[0])