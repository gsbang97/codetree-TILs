from collections import deque

N = int(input())
dq = deque()
for _ in range(N):
    command = list(input().split())
    if command[0] == 'push_front':
        dq.appendleft(command[1])
    elif command[0] == 'push_back':
        dq.append(command[1])
    elif command[0] == 'pop_front':
        print(dq.popleft())
    elif command[0] == 'pop_back':
        print(dq.pop())
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        print(dq[0])
    elif command[0] == 'back':
        print(dq[-1])