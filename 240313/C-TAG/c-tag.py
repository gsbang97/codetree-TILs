# n : 그룹 당 알파벳 줄 수 
# m : 알파벳 당 가지고 있는 원소 수 

n,m = map(int, input().split())
A = [input() for _ in range(n)]
B = [input() for _ in range(n)]
cnt = 0
for i in range(m):
    for j in range(i+1, m):
        for k in range(j+1, m):
            A_set = set([A[idx][i]+A[idx][j]+A[idx][k] for idx in range(n)])
            B_set = set([B[idx][i]+B[idx][j]+B[idx][k] for idx in range(n)])
            flag = True
            for s in A_set:
                if s in B_set:
                    flag = False
                    break
            
            if flag:
                cnt +=1

print(cnt)