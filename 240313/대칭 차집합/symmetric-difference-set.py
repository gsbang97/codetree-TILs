n,m = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))
result = len(A - B)+ len(B - A)
print(result)