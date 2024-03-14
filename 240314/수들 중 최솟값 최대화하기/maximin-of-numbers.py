# 크기가 n * n인 2차원 격자 내 각 칸에 정수
# n개의 칸에 색칠
# 각 행과 열에 정확히 1개의 색칠된 칸만 오도록 함
# 색칠된 칸에 적힌 수들 중 최솟값이 최대가 되도록

n = int(input())

numbers = [list(map(int, input().split())) for _ in range(n)]

selected = [False for _ in range(n)]
ans = []
max_value = 0
def choose(cnt):
    global max_value
    if cnt == n:
        min_value = min(ans)
        max_value = max(max_value, min_value)
        return
    
    for i in range(n):
        if selected[i]:
            continue
        
        selected[i] = True
        ans.append(numbers[cnt][i])
        choose(cnt+1)
        ans.pop()
        selected[i] = False
    
choose(0)

print(max_value)