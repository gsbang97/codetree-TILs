from heapq import heappop, heappush

n,m = map(int, input().split())
ans = 0
# 무게, 가치
gems = []
for _ in range(n):
    w,v = map(int, input().split())
    heappush(gems, (-v/w, w, v))

while m > 0 and gems:
    _, w, v = heappop(gems)
    if w <= m:
        ans += v
        m -= w
    else:
        ans += m * v / w
        m = 0
ans = round(ans, 3)
print(f'{ans:.3f}')