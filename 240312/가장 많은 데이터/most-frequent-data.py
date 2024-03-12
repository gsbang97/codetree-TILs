seq = {}
n = int(input())
for _ in range(n):
    s = input()
    if s in seq.keys():
        seq[s] += 1
    else:
        seq[s] = 1

print(max(seq.items())[1])