# 1부터 C까지 번호가 매겨진 빨간 돌 C개
# 1부터 N 까지 번호가 매겨진 검정 돌 N개
c,n = map(int, input().split())

reds = set([int(input()) for _ in range(c)])
blacks = [tuple(map(int, input().split())) for _ in range(n)]
# reds.sort()
blacks.sort(key=lambda x: (x[1]-x[0]))
cnt = 0
# red_idx = 0
black_idx = 0
for A,B in blacks:
    for t in range(A,B+1):
        if t in reds:
            reds.remove(t)
            cnt += 1
            break
print(cnt)