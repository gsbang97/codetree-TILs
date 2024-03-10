N = int(input())
A = list(map(int, input().split()))
result = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if A[i] <= A[j] and A[j] <= A[k]:
                
                result +=1
print(result)