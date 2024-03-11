strs = input()
l = len(strs)
cnt = 0
for i in range(l-3):
    if strs[i] == '(' and strs[i+1] == '(':
        for j in range(i+2,l-1):
            if strs[j] == ')' and strs[j+1] == ')':
                cnt +=1
        

print(cnt)