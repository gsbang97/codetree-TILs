node_dict = dict()

class Node:
    def __init__(self,n):
        self.prev = None
        self.next_ = None
        self.value = n
        node_dict[n] = self
    def unconnect(self):
        p = self.prev
        n = self.next_
        if p:
            p.next_ = n
            self.prev = None
        if n:
            n.prev = p
            self.next_ = None
    def insert_next(self, node):
        n = self.next_
        if n:
            n.prev = node
            node.next_ = n
        node.prev = self
        self.next_ = node
    def insert_prev(self, node):
        p = self.prev
        if p:
            p.next_ = node
            node.prev = p
        node.next_ = self
        self.prev = node
    def __str__(self):
        return f"{0 if self.prev is None else self.prev.value} {0 if self.next_ is None else self.next_.value}" 
# n : 노드의 총 개수
n = int(input())
# q : 연산 횟수
q = int(input())
for _  in range(q):
    command = list(map(int, input().split()))
    if command[1] not in node_dict.keys():
        node_dict[command[1]] = Node(command[1])
    i = node_dict[command[1]]

    if command[0] == 1:
        i.unconnect()
    elif command[0] == 2:
        if command[2] not in node_dict.keys():
            node_dict[command[2]] = Node(command[2])
        j = node_dict[command[2]]
        i.insert_prev(j)
    elif command[0] == 3:
        if command[2] not in node_dict.keys():
            node_dict[command[2]] = Node(command[2])
        j = node_dict[command[2]]
        i.insert_next(j)
    elif command[0] == 4:
        print(i)
for i in range(1,n+1):
    if i not in node_dict.keys():
        print(0,end=" ")
    else:
        next_node = node_dict[i].next_
        if next_node is None:
            print(0,end=" ")
        else:
            print(next_node.value,end=" ")