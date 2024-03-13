import sys

# S , 1-9 , E
# n : 맵의 크기
n = int(input())
coins = [[-1,-1] for i in range(10)]
coin_map = [list(input()) for _ in range(n)]
min_dist = sys.maxsize
start = None
end = None
coin_cnt = 0
for i in range(n):
    for j in range(n):
        v = coin_map[i][j]
        if v == '.':
            pass
        elif v == 'S':
            start = (i,j)
        elif v == 'E':
            end = (i,j)
        else:
            coins[int(v)] = [i,j]
            coin_cnt += 1


def choose(cnt,x,y,dist,coin):
    global min_dist
    if cnt == 3:
        dist += (abs(end[0]-x) + abs(end[1]-y))
        min_dist = min(min_dist, dist) 
        return
    for i in range(coin+1,10):
        if coins[i][0] != -1:
            adder = (abs(coins[i][0]-x) + abs(coins[i][1]-y))
            choose(cnt+1,coins[i][0],coins[i][1],dist + adder,i)
if start == None or end == None or coin_cnt < 3 :
    print(-1)
else:
    choose(0,start[0],start[1],0,0)
    print(min_dist)