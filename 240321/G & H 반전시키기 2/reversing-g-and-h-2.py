n = int(input())
init_str = input()
goal_str = input()
is_flip = False
push = 0
for idx in range(n-1,-1,-1):
    if init_str[idx] != goal_str[idx]:
        if not is_flip:
            push += 1
            is_flip = not is_flip
    else:
        if is_flip:
            push +=1
            is_flip = not is_flip
print(push)