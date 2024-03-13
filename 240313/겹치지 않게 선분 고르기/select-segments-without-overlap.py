# n : 선분의 개수
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

able = [0 for _ in range(1001)]

def line_check(x,y):
    for i in range(x,y+1):
        if able[i] == 1:
            return False
    return True
    
max_cnt = 0
def choose(cnt):
    can_cnt = 0
    for line in lines:
        x,y = line
        if line_check(x,y):
            for i in range(x,y+1):
                able[i] = 1
            choose(cnt+1)
            for i in range(x,y+1):
                able[i] = 0
            can_cnt += 1
    if can_cnt == 0:
        global max_cnt
        max_cnt = max(max_cnt, cnt)
choose(0)
print(max_cnt)