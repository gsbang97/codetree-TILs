n, k = map(int, input().split())

seq = {}
for num in map(int, input().split()):
    if num in seq.keys():
        seq[num] += 1
    else:
        seq[num] = 1
item = list(seq.items())
item.sort(key = lambda x : (-x[1],-x[0]))
for i in range(k):
    print(item[i][0], end = " ")
# print(.sort)