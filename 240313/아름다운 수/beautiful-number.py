n = int(input())
cnt = 0
number = [0 for i in range(n+1)]
def checkNumber(numbers):
    for i in range(1,n+1):
        if numbers[i] > 0 and numbers[i] != i:
            return False
    return True
    
def choose(num, idx,numbers):
    # print(num, idx, numbers)
    global cnt
    if idx == 0:
        if checkNumber(numbers):
            cnt += 1 
        return 
    if num == -1:
        for i in range(1,min(5,idx+1)):
            numbers[i] += 1
            choose(i,idx-1, numbers)
            numbers[i] -= 1
            if number[i] < 0:
                number[i] = 0
    else:
        if numbers[num] == num:
            numbers[num] = 0
            for i in range(1,min(5,idx+1)):
                numbers[i] += 1
                choose(i,idx-1,numbers)
                numbers[i] -= 1
                if number[i] < 0:
                    number[i] = 0
        elif numbers[num] > 0:
            numbers[num] += 1
            choose(num, idx-1,numbers)
            numbers[num] -= 1
            if number[num] < 0:
                number[num] = 0
        else:
            for i in range(1,min(5,idx+1)):
                numbers[i] += 1
                choose(i,idx-1,numbers)
                numbers[i] -= 1
                if number[i] < 0:
                    number[i] = 0


choose(-1,n,number)
print(cnt)