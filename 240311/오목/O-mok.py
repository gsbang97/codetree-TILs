board = [list(map(int, input().split())) for _ in range(19)]
result = 0
for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            if i < 14:
                check = board[i][j] 
                if check == board[i+1][j] and check == board[i+2][j] and check == board[i+3][j] and check == board[i+4][j]:
                    print(check)
                    print(i+3, j+1)
                    exit()
            if j < 14:
                if check == board[i][j+1] and check == board[i][j+2] and check == board[i][j+3] and check == board[i][j+4]:
                    print(check)
                    print(i+1, j+3)
                    exit()
            if i < 14 and j < 14:
                if check == board[i+1][j+1] and check == board[i+2][j+2] and check == board[i+3][j+3] and check == board[i+4][j+4]:
                    print(check)
                    print(i+3, j+3)
                    exit()
            if i > 3 and j < 14:
                if check == board[i-1][j+1] and check == board[i-2][j+2] and check == board[i-3][j+3] and check == board[i-4][j+4]:
                    print(check)
                    print(i-1, j+3)
                    exit()
print(0)