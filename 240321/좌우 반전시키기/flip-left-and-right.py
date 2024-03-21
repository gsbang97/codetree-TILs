n = int(input())

numbers = list(map(int, input().split()))
min_push = 101
def choose(cnt, push):
    # print(cnt,push)
    # print(numbers)
    global min_push
    if cnt == n-1:
        if n < 2:
            min_push = -1 if numbers[-1] == 0 else 0
            return
        if numbers[-1] == 1 and numbers[-2] == 1:
            min_push = min(min_push, push)
        elif numbers[-1] == 0 and numbers[-2] == 0:
            min_push = min(min_push, push+1)
        return 
    
    if cnt == 0:
        choose(cnt + 1, push)
    elif cnt < n-1:
        if numbers[cnt-1] == 1:
            choose(cnt + 1, push)
        else:
            numbers[cnt - 1] = 0 if numbers[cnt-1] == 1 else 1
            numbers[cnt] = 0 if numbers[cnt] == 1 else 1
            numbers[cnt+1] = 0 if numbers[cnt+1] == 1 else 1
            
            choose(cnt + 1, push + 1)
            numbers[cnt - 1] = 0 if numbers[cnt-1] == 1 else 1
            numbers[cnt] = 0 if numbers[cnt] == 1 else 1
            numbers[cnt+1] = 0 if numbers[cnt+1] == 1 else 1
choose(0,0)
if min_push == 101:
    min_push = -1
print(min_push)