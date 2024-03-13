N, M = map(int, input().split())

ans = []
def choose(cnt):
    global ans
    if cnt == M:
        print(*ans)
        return 
    if len(ans) == 0:
        j = 1
    else:
        j = ans[-1]+1
    for i in range(j,N+1):
        ans.append(i)
        choose(cnt+1)
        ans.pop()
choose(0)