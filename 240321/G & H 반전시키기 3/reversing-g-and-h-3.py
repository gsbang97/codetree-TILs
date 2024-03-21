n = int(input())
init_str = input()
goal_str = input()
answer = 0
cnt = 0
for i in range(n):
    if init_str[i] != goal_str[i]:
        if cnt == 0:
            answer += 1
        cnt += 1
        if cnt == 4:
            cnt = 0
    else:
        cnt = 0
print(answer)