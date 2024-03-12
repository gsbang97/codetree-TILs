# n : 정수의 개수 , k : 세 수를 더 했을 때 나와야하는 값
n,k = map(int, input().split())
seq = {}
seq2 = {}
cnt = 0
for i in map(int, input().split()):
    if k-i in seq2.keys():
        cnt += seq2[k-i]
    for key in seq.keys():
        if key+i in seq2.keys():
            seq2[key + i] += seq[key]
        else:
            seq2[key + i] = seq[key]
    if i in seq.keys():
        seq[i] += 1
    else:
        seq[i] = 1
print(cnt)