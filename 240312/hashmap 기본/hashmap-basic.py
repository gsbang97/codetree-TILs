n = int(input())

hashmap = dict()
for _ in range(n):
    command = list(input().split())
    if command[0] == 'add':
        hashmap[command[1]] = command[2]
    elif command[0] == 'remove':
        hashmap.pop(command[1])
    elif command[0] == 'find':
        if command[1] in hashmap.keys():
            print(hashmap[command[1]])
        else:
            print('None')