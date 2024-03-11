N = int(input())
coins = [list(map(int, input().split())) for _ in range(N)]
max_coins = 0
for i in range(N-2):
    for j in range(N-2):
        max_coins = max(max_coins,sum(coins[i][j:j+3]+coins[i+1][j:j+3]+coins[i+2][j:j+3]))
print(max_coins)