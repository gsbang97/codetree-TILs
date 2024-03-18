n1, n2 = map(int, input().split())

A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))
ans = len(A - B) + len(B - A)
print(ans)