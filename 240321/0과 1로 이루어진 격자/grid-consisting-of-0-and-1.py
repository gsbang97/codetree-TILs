n = int(input())

numbers = [input() for _ in range(n)]

row_flip = [False for _ in range(10)]
col_flip = [False for _ in range(10)]
push = 0
is_flip = False
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        is_flip = col_flip[j]
        if numbers[i][j] == '0' and is_flip:
            push += 1
            # for x in range(i+1):
            #     row_flip[x] = False if row_flip[x] else True
            for y in range(j+1):
                col_flip[y] = False if col_flip[y] else True
        if numbers[i][j] == '1' and not is_flip:
            push += 1
            # for x in range(i+1):
            #     row_flip[x] = False if row_flip[x] else True
            for y in range(j+1):
                col_flip[y] = False if col_flip[y] else True
print(push)