a = input()
idx = -1
sum = 0
flag = True
for i, s in enumerate(a):
    sum += 2**(len(a)-i-1)
    if s == '0' and flag:
        flag = False

if flag == False:
    sum -= 1
print(sum)