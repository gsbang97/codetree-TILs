# n : 원소의 개수, k : 두 수의 합이 될 수 
n,k = map(int, input().split())
seq = {}
for i in map(int, input().split()):
    if i in seq.keys():
        seq[i] += 1 
    else:
        seq[i] = 1
cnt = 0
visited = []
for key in seq.keys():
    if k-key == key:
       cnt += seq[key]*(seq[key]-1)
    elif k-key in seq.keys() and k-key not in visited:
        cnt += (seq[key]*seq[k-key])
        visited.append(key)
        
print(cnt)