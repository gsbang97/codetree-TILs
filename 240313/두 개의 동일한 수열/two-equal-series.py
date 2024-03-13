n = int(input())
A = set(input().split())
B = set(input().split())
if len(A-B) == 0:
    print('Yes')
else:
    print('No')