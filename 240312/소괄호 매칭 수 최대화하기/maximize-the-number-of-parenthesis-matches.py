from functools import cmp_to_key

def score(s):
    l = len(s)
    cnt = 0
    for i in range(l):
        if s[i] == '(':
            for j in range(i+1, l):
                if s[j] == ')':
                    cnt += 1
    return cnt
def compare(x,y):
    s1 = score(x+y)
    s2 = score(y+x)
    if s1 > s2 :
        return -1
    elif s1 < s2 :
        return 1
    else:
        return 0
n = int(input())
# strs = [input() for _ in range(n)]
# strs.sort(key=cmp_to_key(compare))
def score_2(s):
    left = s.count('(')
    right = s.count(')')
    return (left,right, score(s))
def compare2(x,y):
    s1 = x[0]*y[1] + x[2] + y[2]
    s2 = x[1]*y[0] + x[2] + y[2]
    if s1 > s2 :
        return -1
    elif s1 < s2 :
        return 1
    else:
        return 0
strs = [score_2(input()) for _ in range(n)]
# print(strs)
strs.sort(key=cmp_to_key(compare2))
# print(strs)
scores = 0
for i in range(n):
    lefts = strs[i][0]
    rights = 0
    # for j in range(i+1):
    #     lefts += strs[j][0]
    for j in range(i+1,n):
        rights += strs[j][1]
    # print(strs[i][2], lefts, rights)
    scores += strs[i][2] + lefts*rights
print(scores)