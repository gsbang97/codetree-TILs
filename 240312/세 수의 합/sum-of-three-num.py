# n : 정수의 개수 , k : 세 수를 더 했을 때 나와야하는 값
n,k = map(int, input().split())
seq = {}
for i in map(int, input().split()):
    if i in seq.keys():
        seq[i] += 1
    else:
        seq[i] = 1
keys = list(seq.keys())
cnt = 0
visited = set()
for i in range(len(keys)):
    for j in range(i, len(keys)):
        s = keys[i]+keys[j]
        if k - s in keys and k - s not in visited:
            if i == j:
                if keys[j] == (k - s):
                    cnt += (seq[keys[i]]*(seq[keys[i]]-1)*(seq[keys[i]]-2)) // 6
                    visited.add(keys[i])
                else:
                    cnt += (seq[keys[i]]*(seq[keys[i]]-1)//2) * seq[k - s]
                    visited.add(keys[i])
                    visited.add((k-s))
            else:
                if keys[i] == (k - s):
                    visited.add(keys[j])
                    cnt += (seq[keys[i]]*(seq[keys[i]]-1)//2) * seq[keys[j]]
                elif keys[j] == (k - s):
                    visited.add(keys[i])
                    cnt += (seq[keys[j]]*(seq[keys[j]]-1)//2) * seq[keys[i]]
                elif (k-s):
                    cnt += seq[keys[i]]*seq[keys[j]]*seq[k-s]
                    visited.add(keys[i])
                    visited.add(keys[j])
            # print(key[i],key[j],k-s,cnt)
                
print(cnt)