n = int(input())
ABCD = [dict() for _ in range(4)]
for i in range(4):
    for n in list(map(int, input().split())):
        if n in ABCD[i].keys():
            ABCD[i][n] += 1 
        else:
            ABCD[i][n] = 1
AB_CD = [dict(), dict()]
for i in [0,1]:
    A_idx = i*2
    B_idx = i*2+1
    for A in ABCD[A_idx].keys():
        for B in ABCD[B_idx].keys():
            if A+B in AB_CD[i].keys():
                AB_CD[i][A+B] += ABCD[A_idx][A] * ABCD[B_idx][B]
            else:
                AB_CD[i][A+B] = ABCD[A_idx][A] * ABCD[B_idx][B]
answer = 0
for A in AB_CD[0].keys():
    B = -1 * A
    if B in AB_CD[1].keys():
        answer += AB_CD[0][A] * AB_CD[1][B]
print(answer)