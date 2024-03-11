# N : 사람의 수 , M : 치즈의 수, D: 치즈를 먹은 기록의 수 , S : 아픈 기록의 수 
N,M,D,S = map(int, input().split())
# (p,m,t) 몇 번째 사람(p)이 몇 번째 치즈(m)를 언제 먹었는지(t초)에 대한 정보
d_info = [tuple(map(int, input().split())) for _ in range(D) ]
# (p,t) 하나씩 몇 번째 사람(p)이 언제 확실히 아팠는지(t초)에 대한 기록 (p, t)
s_info = [tuple(map(int, input().split())) for _ in range(S) ]
c = -1
is_True = True
people = []
for i in range(1,M+1):
    cnt = 0
    for p1, t1 in s_info:
        is_True = True
        for p2, m2, t2 in d_info:
            if p1 == p2 and m2 == i:
                cnt +=1
                is_True = is_True and t2 < t1
    if is_True and cnt >= S:
        c = i
        # print(c)
        for p1,m1,t1 in d_info:
            if m1 == c:
                people.append(p1)
        # break
# cnt = 0
# print(c)
# for p1,m1,t1 in d_info:
#     if m1 == c:
#         cnt +=1
# print(people)
print(len(set(people)))