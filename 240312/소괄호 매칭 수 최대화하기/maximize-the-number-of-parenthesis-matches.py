from functools import cmp_to_key

def score(s):
    l = len(s)
    cnt = 0
    lefts = 0
    for i in range(l):
        if s[i] == '(':
            lefts += 1
        else:
            cnt += lefts
    return cnt

def score_2(s):
    left = s.count('(')
    right = s.count(')')
    return (left,right, score(s))
def compare(x,y):
    s1 = x[0]*y[1] + x[2] + y[2]
    s2 = x[1]*y[0] + x[2] + y[2]
    if s1 > s2 :
        return -1
    elif s1 < s2 :
        return 1
    else:
        return 0
n = int(input())
strs = [score_2(input()) for _ in range(n)]
strs.sort(key=cmp_to_key(compare))
scores = strs[0][2]
lefts = strs[0][0]
for i in range(1,n):
    
    rights = strs[i][1]
    scores += lefts*rights + strs[i][2]
    lefts += strs[i][0]
    
print(scores)