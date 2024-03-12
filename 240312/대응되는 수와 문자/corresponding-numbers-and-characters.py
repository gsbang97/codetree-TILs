# n : 숫자의 개수, m : 조사할 값의 개수
n,m = map(int, input().split())

ntoc = {}
cton = {}

for i in range(1,n+1):
    s = input()
    ntoc[str(i)] = s
    cton[s] = i

for _ in range(m):
    s = input()
    if s in ntoc.keys():
        print(ntoc[s])
    if s in cton.keys():
        print(cton[s])