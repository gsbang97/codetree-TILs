n, m = map(int, input().split())
seq = {}
for n in input().split():
    if n in seq.keys():
        seq[n] += 1
    else:
        seq[n] = 1
for n in input().split():
    if n in seq.keys():
        print(seq[n], end=" ")
    else:
        print(0, end=" ")