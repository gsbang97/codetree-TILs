n = int(input())


A = input()
B = input()
not_flip = 0
flip = 0
prev_same = False
is_init = True
for a,b in zip(A,B):
    if a == b:
        if not prev_same or is_init:
            is_init = False
            flip += 1
        prev_same = True
    else:
        if prev_same or is_init:
            is_init = False
            not_flip += 1
        prev_same = False
ans = flip
print(ans)