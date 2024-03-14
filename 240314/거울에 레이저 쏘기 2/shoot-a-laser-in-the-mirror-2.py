n = int(input())

mirrors = [input() for _ in range(n)]

start = int(input()) - 1
i = start % n # 몇 번째 에서 시작하는지
d = start // n # 어느 방향인지
x,y,direction = 0,0,0
dxs,dys = [-1,0,1,0],[0,1,0,-1]
if d == 0:
    x,y,direction = -1, i, 2
elif d == 1 :
    x,y,direction = i, n, 3
elif d == 2 :
    x,y,direction = n, n-i-1, 0
else:
    x,y,direction = n-1-i, n, 1
mirror_dict = {
    "\\": [3,2,1,0],
    "/" : [1,0,3,2]
}
cnt = 0
def in_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < n
while(1):
    cnt +=1
    x,y = x+dxs[direction], y+dxs[direction]
    if not in_range(x,y):
        break
    direction = mirror_dict[mirrors[x][y]][direction]
print(cnt)