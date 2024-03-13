a = list(input())
a.sort()
b = list(input())
b.sort()
if ''.join(a) == ''.join(b):
    print('Yes')
else:
    print('No')