n = int(input())

numbers = list(map(int, input().split()))
min_push = 100
def choose(cnt, push):
    global min_push
    if cnt == n-1:
        if numbers[-1] == 1 and numbers[-2] == 1:
            min_push = min(min_push, push)
        elif numbers[-1] == 0 and numbers[-2] == 0:
            min_push = min(min_push, push+1)
        return 
    
    if cnt == 0:
        choose(cnt + 1, push)
        numbers[cnt] = 0 if numbers[cnt] == 1 else 1
        numbers[cnt+1] = 0 if numbers[cnt+1] == 1 else 1
        choose(cnt + 1, push + 1)    
    elif cnt < n-1:
        if numbers[cnt-1] == 1:
            choose(cnt + 1, push)
        else:
            numbers[cnt - 1] = 0 if numbers[cnt] == 1 else 1
            numbers[cnt] = 0 if numbers[cnt] == 1 else 1
            numbers[cnt+1] = 0 if numbers[cnt+1] == 1 else 1
            choose(cnt + 1, push + 1)
            numbers[cnt - 1] = 0 if numbers[cnt] == 1 else 1
            numbers[cnt] = 0 if numbers[cnt] == 1 else 1
            numbers[cnt+1] = 0 if numbers[cnt+1] == 1 else 1
choose(0,0)
print(min_push)