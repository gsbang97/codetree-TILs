s = None
seq = {}
word = input()
for i in word:
    if i in seq.keys():
        seq[i] += 1
    else: 
        seq[i] = 1
for i in word:
    if seq[i] == 1:
        print(i)
        exit()
print(None)