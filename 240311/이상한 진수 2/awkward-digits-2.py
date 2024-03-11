a = input()
idx = -1
sum = 0
flag = True
for i, s in enumerate(a):
    if s == '1':
        sum += 2**(len(a)-i-1)
    if s == '0' and flag:
        sum += 2**(len(a)-i-1)
        flag = False

if flag:
    sum -= 1
print(sum)