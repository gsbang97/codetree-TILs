# dfs
# N개의 정점과 M개의 간선으로 이루어진 양방향 그래프
# 1번 정점에서 시작하여 주어진 간선을 따라 이동했을 때 도달 할 수 있는 서로 다른 정점의 수

n,m = map(int, input().split())
grape = [[False for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())

    grape[x][y] = True
    grape[y][x] = True

visited = [False for _ in range(n+1)]
visited[1] = True
cnt = 0
def dfs(current):
    
    global cnt
    for x in range(1,n+1):
        if grape[current][x] and not visited[x]:
            visited[x] = True
            cnt += 1
            dfs(x)

dfs(1)
print(cnt)