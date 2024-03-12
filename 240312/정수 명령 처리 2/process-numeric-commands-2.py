from collections import deque

dq = deque()

N = int(input())
for _ in range(N):
    command = list(input().split())
    if command[0] == 'push':
        dq.append(command[1])
    elif command[0] == 'pop':
        print(dq.popleft())
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        print(dq[0])