n,t = map(int, input().split())

r,c,d = input().split()
r = int(r)
c = int(c)

dxs,dys = [1,0,0,-1], [0,1,-1,0]
if d == 'U':
    d = 3
elif d == 'D':
    d = 0
elif d == 'R':
    d = 1
else:
    d = 2

def in_range(x,y,d):
    return (d == 0 and x == n) or (d == 1 and y == n) or (d == 2 and y == 1) or (d == 3 and x == 1)
        
for i in range(t):
    if in_range(r,c,d):
        d = 3-d
        continue
    r += dxs[d]
    c += dys[d]
    

print(r,c)