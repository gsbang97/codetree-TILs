class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

def connect(n1:Node, n2:Node):
    if n1:
        n1.next = n2
    if n2:
        n2.prev = n1

n = int(input())
start = Node(None)
node_arr = [start]+[Node(i) for i in range(1,n+1)]
# connect(start, node)
for i in range(n):
    connect(node_arr[i], node_arr[i+1])

q = int(input())
# print(node_arr)
for _ in range(q):
    a,b,c,d = map(int, input().split())
    a_prev = node_arr[a].prev # 1
    b_next = node_arr[b].next # 3
    c_prev = node_arr[c].prev # 2
    d_next = node_arr[d].next # 4
    connect(node_arr[b],d_next)
    connect(a_prev, node_arr[c])
    if b_next == node_arr[c]:
        connect(node_arr[d], node_arr[a])
    else:
        connect(c_prev,node_arr[a])
        connect(node_arr[d],b_next) 
    # node = node_arr[0]
    # for _ in range(n):
    #     node = node.next
    #     print(node.value, end=" ")
    # print()
node = node_arr[0]
for _ in range(n):
    node = node.next
    print(node.value, end=" ")