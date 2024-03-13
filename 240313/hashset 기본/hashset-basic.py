n = int(input())
hashset = set()
for _ in range(n):
    command = input().split()
    if command[0] == 'add':
        hashset.add(command[1])
    elif command[0] == 'remove':
        hashset.remove(command[1])
    elif command[0] == 'find':
        if command[1] in hashset:
            print('true')
        else:
            print('false')