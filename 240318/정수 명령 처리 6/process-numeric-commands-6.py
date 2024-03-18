import heapq

class PtiotiryQueue:
    def __init__(self):
        self.items = []

    def push(self, value):
        heapq.heappush(self.items, -value)
    def pop(self):
        return -heapq.heappop(self.items)
    def size(self):
        return len(self.items)
    def empty(self):
        return not self.items
    def top(self):
        return -self.items[0]
n = int(input())

que = PtiotiryQueue()
for _ in range(n):
    commands = input().split()
    if commands[0] == "push":
        que.push(int(commands[1]))
    elif commands[0] == "pop":
        print(que.pop())
    elif commands[0] == "size":
        print(que.size())
    elif commands[0] == "empty":
        print(1 if que.empty() else 0)
    elif commands[0] == "top":
        print(que.top())