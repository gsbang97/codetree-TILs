n = int(input())

numbers = [input() for _ in range(n)]

push = 0
is_flip = False
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        if numbers[i][j] == '0' and is_flip:
            push += 1
            is_flip = False if is_flip else True
        if numbers[i][j] == '1' and not is_flip:
            push += 1
            is_flip = False if is_flip else True
print(push)