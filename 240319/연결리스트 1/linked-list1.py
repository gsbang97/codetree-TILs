class StringNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next_ = None
    
    def insert_next(self, node):
        u = self.next_
        self.next_ = node
        node.prev = self
        if u != None:
            node.next_ = u
            u.prev = node
    def insert_prev(self, node):
        p = self.prev
        self.prev = node
        node.next_ = self
        if p != None:
            node.prev = p
            p.next_ = node
    
    def __str__(self):
        string = "(Null)" if self.prev is None else self.prev.value 
        string += f" {self.value} "
        string += "(Null)" if self.next_ is None else self.next_.value
        return string
cur = StringNode(input()) # 초기 문자열 노드

n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == '1':
        cur.insert_prev(StringNode(command[1]))
    elif command[0] == '2':
        cur.insert_next(StringNode(command[1]))
    elif command[0] == '3':
        if cur.prev != None:
            cur = cur.prev
    elif command[0] == '4':
        if cur.next_ != None:
            cur = cur.next_
    print(cur)