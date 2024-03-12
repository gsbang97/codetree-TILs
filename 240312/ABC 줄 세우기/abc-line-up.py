alphabet_dict = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
    'D' : 4,
    'E' : 5,
    'F' : 6,
    'G' : 7,
    'H' : 8,
    'I' : 9,
    'J' : 10,
    'K' : 11,
    'L' : 12,
    'M' : 13,
    'N' : 14,
    'O' : 15,
    'P' : 16,
    'Q' : 17,
    'R' : 18,
    'S' : 19,
    'T' : 20,
    'U' : 21,
    'V' : 22,
    'W' : 23,
    'X' : 24,
    'Y' : 25,
    'Z' : 26,
}
n = int(input())
alpha = input().split()
# print( )
def score(strs):
    sc = 0
    for i, s in enumerate(strs):
        sc += abs(i + 1 - alphabet_dict[s])
        # s += abs(i+1 - alphabet_dict[s])
    return sc
# print(score(alpha))
# score(alpha)
scores = score(alpha)
cnt = 0
while scores != 0:
    best_score = [0,-2]
    for i in range(n-1):
        s = 0
        if i > alphabet_dict[alpha[i]] -1 :
            s -= 1
        else:
            s += 1
        if i + 1 < alphabet_dict[alpha[i+1]] -1 :
            s -= 1
        else:
            s += 1
        if s == 2 :
            tmp = alpha[i]
            alpha[i] = alpha[i+1]
            alpha[i+1] = tmp
            cnt += 1
            best_score = [i,s]
            break
        if best_score[1] < s:
            best_score = [i,s]
    if best_score[1] != 2:
        i = best_score[0]
        tmp = alpha[i]
        alpha[i] = alpha[i+1]
        alpha[i+1] = tmp
        cnt += 1
    scores = score(alpha)
print(cnt)