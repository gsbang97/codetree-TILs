# 크기가 n * n인 2차원 정수 격자
# 각 열별 하나의 정수만 색칠해 가장 합이 큰 값을 구하는 프로그램

n = int(input())

numbers = [list(map(int, input().split())) for _ in range(n)]
max_val = 0
ans = []
selected = [False for _ in range(n)]
def choose(cnt):
    global max_val
    if cnt == n:
        max_val = max(max_val, sum(ans))
    for i in range(n):
        if selected[i]:
            continue
        ans.append(numbers[cnt][i])
        selected[i] = True
        choose(cnt+1)
        ans.pop()
        selected[i] = False
choose(0)
print(max_val)