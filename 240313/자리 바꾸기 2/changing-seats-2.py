# 1부터 N까지 번호표를 든 N명의 사람이 1부터 N까지 번호가 매겨진 자리에 번호 순서대로 앉아있습니다. 
# K분 동안 K번 자리 바꾸기가 진행 된 후에 K+1 … 2*K 분 동안은 똑같은 방식으로 K번의 자리 바꿈이 반복
# 2*K+1 … 3*K 분 동안 또 같은 방식으로 K번의 자리 바꿈이 반복
# n: 사람수 (번호 수) # k : 자리바꿈 경우의수
n,k = map(int, input().split())

seat_set = [set([i]) for i in range(n)]
seat_list = [i for i in range(n)]
change_list = [tuple(map(int, input().split())) for i in range(k) ]
for i in range(3):
    for a,b in change_list:
        a -=1
        b -=1
        seat_set[seat_list[a]].add(b)
        seat_set[seat_list[b]].add(a)
        seat_list[a], seat_list[b] = seat_list[b], seat_list[a]
for i in range(n):
    print(len(seat_set[i]))