# n : 선분의 개수
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

able = [0 for _ in range(1001)]
line_used = [True for _ in range(n)]
def line_check(x,y):
    for i in range(x,y+1):
        if able[i] == 1:
            return False
    return True
    
max_cnt = 0
def choose(cnt, line_idx):
    can_cnt = 0
    for idx in range(line_idx, n):
        line = lines[idx]
        if line_used[idx]:
            line_used[idx] = False
            x,y = line
            if line_check(x,y):
                for i in range(x,y+1):
                    able[i] = 1
                choose(cnt+1,idx)
                for i in range(x,y+1):
                    able[i] = 0
                can_cnt += 1
            line_used[idx] = True
    if can_cnt == 0:
        global max_cnt
        max_cnt = max(max_cnt, cnt)
choose(0,0)
print(max_cnt)