# 사전순으로 가장 뒤에 있는 수열부터 먼저 출력
n = int(input())

ans = []
visited = [False for _ in range(n+1)]
def choose(cnt):
    if cnt == n:
        print(*ans)
    for i in range(n,0,-1):
        if visited[i]:
            continue
        visited[i] = True
        ans.append(i)
        choose(cnt+1)
        ans.pop()
        visited[i] = False
    
choose(0)