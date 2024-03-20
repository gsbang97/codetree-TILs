from bisect import bisect_left
# 1부터 C까지 번호가 매겨진 빨간 돌 C개
# 1부터 N 까지 번호가 매겨진 검정 돌 N개
c,n = map(int, input().split())

# reds = set([int(input()) for _ in range(c)])
reds = [int(input()) for _ in range(c)]
blacks = [tuple(map(int, input().split())) for _ in range(n)]
reds.sort()
blacks.sort(key=lambda x: (x[1]))
cnt = 0
# red_idx = 0
black_idx = 0
# max_red = 1000000000
for A,B in blacks:
    # for t in range(B,A-1,-1):
    start_idx = bisect_left(reds,A)
    for red_idx in range(start_idx,c):
        t = reds[red_idx]
        if t <= B:
            reds.pop(red_idx)
            cnt += 1
            c -= 1
            break
        elif t  > B :
            break
print(cnt)