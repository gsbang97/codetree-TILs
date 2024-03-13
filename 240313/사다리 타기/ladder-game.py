# n : 세로줄의 수, m : 가로줄의 수 
n, m = map(int, input().split())
lines = [tuple(map(int, input().split())) for _ in range(m)]
lines.sort(key = lambda x : x[1])

init_result = list(range(n))
for (x,y) in lines:
    x -=1
    init_result[x], init_result[x+1] = init_result[x+1], init_result[x]

min_lines = 15
use_line = []
def check_result():
    init = list(range(n))
    for (x,y) in use_line:
        x -=1
        init[x], init[x+1] = init[x+1], init[x]
    return init == init_result
def choose(cnt):
    global min_lines
    if check_result():
        min_lines = min(len(use_line), min_lines)
        return
    if cnt >= m :
        return
    use_line.append(lines[cnt])
    choose(cnt+1)
    use_line.pop()
    choose(cnt+1)
choose(0)        
print(min_lines)