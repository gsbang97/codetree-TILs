class Stack:
    def __init__(self):
        self.items = []

    def push(self,A):
        self.items.append(A)
    def empty(self):
        return not self.items

    def pop(self):
        if self.empty():
            raise Exception("stack is Empty")
        return self.items.pop()
    
    def size(self):
        return len(self.items)

    def top(self):
        if self.empty():
            raise Exception("stack is Empty")
        return self.items[-1]

stack = Stack()
n = int(input())
for _ in range(n):
    command = list(input().split())
    if command[0] == 'push':
        stack.push(command[1])
    elif command[0] == 'pop':
        print(stack.pop())
    elif command[0] == 'size':
        print(stack.size())
    elif command[0] == 'empty':
        if stack.empty:
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        print(stack.top())