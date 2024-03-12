opens = 0
for i in input():
    if i == '(':
        opens +=1
    else:
        if opens > 0:
            opens -=1
        else:
            print('No')
            exit()
if opens == 0:
    print('Yes')
else:
    print('No')