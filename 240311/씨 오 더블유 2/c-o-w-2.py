n = int(input())
strs = input()
cnt = 0
for i in range(n-2):
    if strs[i] == 'C':
        for j in range(i+1, n-1):
            if strs[j] == 'O':
                for k in range(j+1,n):
                    if strs[k] == 'W':
                        cnt +=1

print(cnt)