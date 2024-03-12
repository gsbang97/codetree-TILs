n = int(input())

seq = {}

for _ in range(n):
    s = list(input())
    s.sort()
    s = ''.join(s)
    if s in seq.keys():
        seq[s] += 1
    else:
        seq[s] = 1
max_items = 0
for _,v in seq.items():
    max_items = max(v,max_items)
print(max_items)