score = [0,0]
rank = 3
next_rank = 3
n = int(input())
cnt = 0
for _ in range(n):
    w,s = input().split()
    if w == 'A':
        score[0] += int(s)
    else:
        score[1] += int(s)
    if score[0] > score[1]:
        next_rank = 1
    elif score[1] > score[0]:
        next_rank = 2
    else:
        next_rank = 3
    if next_rank != rank :
        cnt +=1 
        rank = next_rank
print(cnt)