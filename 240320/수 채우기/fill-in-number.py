import sys

n = int(input())

coins = [sys.maxsize for _ in range(n+1)]
coins[0] = 0
for i in range(2,n+1):
    if coins[i-2] != sys.maxsize:
        coins[i] = min(coins[i], coins[i-2]+1)
    if coins[i-5] != sys.maxsize:
        coins[i] = min(coins[i], coins[i-5]+1)
if coins[n] == sys.maxsize:
    coins[n] = -1
print(coins[n])