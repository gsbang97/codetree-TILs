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
strs = [input() for _ in range(n)]

strs.sort(key=cmp_to_key(compare))
s = ''.join(strs)
print(score(s))