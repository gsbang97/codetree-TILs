# 1부터 C까지 번호가 매겨진 빨간 돌 C개
# 1부터 N 까지 번호가 매겨진 검정 돌 N개
c,n = map(int, input().split())

reds = [int(input()) for _ in range(c)]
blacks = [tuple(map(int, input().split())) for _ in range(n)]
reds.sort()
blacks.sort(key=lambda x: (x[1],-x[1]+x[0]))
cnt = 0
red_idx = 0
black_idx = 0
while black_idx < n and red_idx < c:
    t = reds[red_idx]
    A,B = blacks[black_idx]
    if A <= t and t <= B:
        red_idx += 1
        black_idx += 1
        cnt += 1
    elif t < A:
        red_idx += 1
    elif t > B:
        black_idx +=1
print(cnt)