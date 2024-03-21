from functools import cmp_to_key

def compare(x,y):
    x_left, x_right, x_score = x
    y_left, y_right, y_score = y
    xy = x_left*y_right
    yx = y_left*x_right
    if xy > yx:
        return -1
    elif xy == yx:
        return 0
    else:
        return 1
n = int(input())
strings = []
for _ in range(n):
    string = input()
    left = 0
    right = 0
    score = 0
    for char in string:
        if char == "(":
            left += 1
        if char == ")":
            right += 1
            score += left
    strings.append((left,right,score))
strings.sort(key=cmp_to_key(compare))
lefts = 0
ans = 0
for i in range(n):
    left, right, score = strings[i]
    if right > 0:
        ans += lefts * right
    lefts += left
    ans += score
print(ans)