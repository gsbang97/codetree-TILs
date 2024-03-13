n = int(input())
cnt = 0
numbers = [0,0,0,0,0]
def checkNumber():
    for i in range(1,n+1):
        if numbers[i] > 0 and numbers[i] != i:
            return False
    return True
    
def choose(num, idx):
    global cnt
    if idx == 0:
        if checkNumber():
            cnt += 1 
        return 
    if num == -1:
        for i in range(1,min(5,idx+1)):
            numbers[i] += 1
            choose(i,idx-1)
            numbers[i] -= 1
    else:
        if numbers[num] == num:
            numbers[num] = 0
            for i in range(1,min(5,idx+1)):
                numbers[i] += 1
                choose(i,idx-1)
                numbers[i] -= 1
        elif numbers[num] > 0:
            numbers[num] += 1
            choose(num, idx-1)
            numbers[num] -= 1
        else:
            for i in range(1,min(5,idx+1)):
                numbers[i] += 1
                choose(i,idx-1)
                numbers[i] -= 1


choose(-1,n)
print(cnt)