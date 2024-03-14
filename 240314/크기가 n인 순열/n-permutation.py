# 1부터 n까지의 수를 정확히 한 번씩만 사용하여 만들 수 있는 가능한 모든 수열을 구해주는 프로그램
# 사전순으로 가장 앞에 있는 수열부터 먼저 출력

n = int(input())
answer = []
visited = [False for _ in range(n+1)]
def choose(cnt):
    if cnt == n:
        print(*answer)

    for i in range(1,n+1):
        if visited[i]:
            continue
        visited[i] = True
        answer.append(i)
        choose(cnt+1)
        answer.pop()
        visited[i] = False

choose(0)