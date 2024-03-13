n = int(input())
A = set(input())
B = set(input())
if len(A-B) == 0:
    print('Yes')
else:
    print('No')