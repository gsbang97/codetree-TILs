# N : 학생 수,  B : 예산
N, B = map(int, input().split())
# (원하는 선물의 가격, 배송비)
ps = [tuple(map(int, input().split())) for _ in range(N)]
max_people = 0
for i in range(N):
    gift = []
    for j, p in enumerate(ps):
        if i == j:
            gift.append(p[0]//2 + p[1])
        else :
            gift.append(p[0] + p[1])
    s = 0
    for i,c in enumerate(sorted(gift)):
        s += c
        if s > B:
            max_people = max(max_people,i)
            break

print(max_people)