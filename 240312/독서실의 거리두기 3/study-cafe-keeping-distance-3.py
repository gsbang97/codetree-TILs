# N : 좌석의 개수
N = int(input())
# 좌석 정보 0: 비어있음, 1: 차있음
seat = input()

max_start = 0
min_start = 0 
min_dist = 1000
max_dist = 0
for i in range(N):
    if seat[i] == '1':
        s = i
        e = 0
        for j in range(i+1,N):
            if seat[j] == '1':
                e = j
                break
        if e-s < 0:
            continue
        if max_dist < e-s:
            max_dist = e-s
        if min_dist > e-s:
            min_dist = e-s
        
    if min_dist <= max_dist // 2:
        break
print(min(min_dist, max_dist//2))