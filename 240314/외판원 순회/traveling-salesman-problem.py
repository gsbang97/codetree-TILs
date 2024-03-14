# 외판원 문제
# 1번 지점에서 출발하여 모든 지점을 정확히 딱 한 번씩만 방문하고 다시 1번 지점으로 돌아옴
# i번 지점에서 j번 지점으로 이동하는데 드는 비용 정보 A가 주어졌을 때
# 모든 정점을 겹치지 않게 방문하고 되돌아오는데 필요한 최소 비용의 합을 구하는 프로그램

# n : 지점의 수
n = int(input())
# A : 비용정보 (i,j) : i에서 j로 이동하는데 드는 비용 정보
A = [list(map(int, input().split())) for _ in range(n)]

min_value = 10000*n
visited = [False for _ in range(n)]
def choose(cnt, current, dist):
    global min_value
    if cnt == n-1:
        if A[current][0] == 0:
            return
        min_value = min(min_value, dist+A[current][0])
        return
    
    for i in range(n):
        if visited[i] or A[current][i] == 0:
            continue
        visited[i] = True
        choose(cnt+1, i, dist + A[current][i])
        visited[i] = False
visited[0] = True
choose(0,0,0)

print(min_value)