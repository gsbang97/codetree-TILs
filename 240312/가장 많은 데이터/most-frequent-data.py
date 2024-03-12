seq = {}
n = int(input())
for _ in range(n):
    s = input()
    if s in seq.keys():
        seq[s] += 1
    else:
        seq[s] = 1
max_item = 0
for k,v in seq.items():
    max_item = max(max_item,v)

print(max_item)