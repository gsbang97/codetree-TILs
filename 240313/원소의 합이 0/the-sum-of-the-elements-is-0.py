n = int(input())
A = {}
for num in map(int, input().split()):
    if num in A.keys():
        A[num] += 1
    else:
        A[num] = 1
B = {}
for num in map(int, input().split()):
    if num in B.keys():
        B[num] += 1
    else:
        B[num] = 1
AB = {}
for key_a in A.keys():
    for key_b in B.keys():
        s = key_a + key_b
        if s in AB.keys():
            AB[s] += A[key_a]*B[key_b]
        else:
            AB[s] = A[key_a]*B[key_b]
C = {}
for num in map(int, input().split()):
    if num in C.keys():
        C[num] += 1
    else:
        C[num] = 1
D = {}
for num in map(int, input().split()):
    if num in D.keys():
        D[num] += 1
    else:
        D[num] = 1
CD = {}
for key_c in C.keys():
    for key_d in D.keys():
        s = key_c + key_d
        if s in CD.keys():
            CD[s] += C[key_c]*D[key_d]
        else:
            CD[s] = C[key_c]*D[key_d]

cnt = 0
for key in AB.keys():
    if -key in CD.keys():
        cnt += AB[key]*CD[-key]
print(cnt)