# N 명의 사람들이 모두 제거될때 까지 진행
# 1번 부터 순서대로 k번째 사람을 제거
# 한 사람이 제거되면 남은 사람들로 원을 이루며 1번 연산을 반복

from collections import deque

N, K = map(int, input().split())
# 죽은 사람들
kill_list = deque()
# 생존자들 
numlist = deque(range(1,N+1))
i = 1
while(len(numlist) != 0):
    if i == K :
        # kill_list.append(numlist.popleft())
        print(numlist.popleft(), end=" ")
        i = 1
    else:
        i += 1 
        numlist.append(numlist.popleft())