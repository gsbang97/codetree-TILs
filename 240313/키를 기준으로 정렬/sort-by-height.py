n = int(input())
people = [input().split() for _ in range(n)]

people.sort(key = lambda x : int(x[1]))

for n,k,w in people:
    print(n,k,w)