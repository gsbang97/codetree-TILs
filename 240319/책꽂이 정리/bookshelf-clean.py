def connect(n1,n2):
    if n1:
        n1.next = n2
    if n2:
        n2.prev = n1

class BookShelf:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def insert_tail(self, node):
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            connect(self.tail,node)
            self.tail = node
        self.size += 1
    def insert_tail_all(self, head,tail, size):
        if self.size == 0:
            self.head = head
            self.tail = tail
        else:
            connect(self.tail,head)
            self.tail = tail
        self.size += size
    def insert_head(self, node):
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            connect(node,self.head)
            self.head = node
        self.size += 1
    def insert_head_all(self, head,tail, size):
        if self.size == 0:
            self.head = head
            self.tail = tail
        else:
            connect(tail,self.head)
            self.head = head
        self.size += size
    def pop_tail(self):
        if self.size == 0:
            return None
        tail = self.tail
        self.tail = self.tail.prev
        self.size -= 1
        if not self.tail is None:
            self.tail.next = None
        else:
            self.head = None
            self.size = 0
        tail.prev = None
        # print(self.tail)
        return tail
    def pop_head(self):
        if self.size == 0:
            return None
        head = self.head
        self.head = self.head.next
        self.size -= 1
        if not self.head is None:
            self.head.prev = None
        else:
            self.tail = None
            self.size = 0
        head.next = None
        return head
    def pop_all(self):
        if self.size == 0:
            return None, None, 0
        head = self.head
        tail = self.tail
        size = self.size
        self.head = None
        self.tail = None
        self.size = 0
        return head, tail, size
class Book:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value
    def __str__(self):
        return str(self.value)

n,k = map(int, input().split())
q = int(input())
bookshelves = [BookShelf() for _ in range(k+1)]
for i in range(1,n+1):
    bookshelves[1].insert_tail(Book(i))
# bookshelves[1].tail = node
# bookshelves[1]['tail'] = node
cnt = 0
for _ in range(q):
    cnt += 1
    command, i,j = map(int, input().split())
    if bookshelves[i].size == 0 :
        continue
    if command == 1:
        
        book = bookshelves[i].pop_head()
        # if not book is None:
        bookshelves[j].insert_tail(book)
    elif command == 2:
        # if bookshelves[i].size > 0 :
        book = bookshelves[i].pop_tail()
        # if not book is None:
        bookshelves[j].insert_head(book)
    elif command == 3:
        head, tail,size = bookshelves[i].pop_all()
        # if size > 0:
        bookshelves[j].insert_head_all(head,tail,size)
    elif command == 4:
        head, tail,size = bookshelves[i].pop_all()
        # if size > 0:
        bookshelves[j].insert_tail_all(head,tail,size)
    # if cnt == 1:
    # print(f"{cnt}번째")
    # print(command, i, j)
    # for idx in range(1,k+1):
    #     node = bookshelves[idx].head
    #     # print(bookshelves[idx].size, end = " ")
    #     # print(bookshelves[idx].head, end = " ")
    #     # print(bookshelves[idx].tail)
        
    #     if cnt >= 14:
    #         print(f"size: {bookshelves[idx].size} head: {bookshelves[idx].head} tail: {bookshelves[idx].tail}")
    #     # print(bookshelves[idx].size, end = " ")
    #     # iii = 0 
    #         while node:
    #             # iii += 1
    #             print(node.value, end = " ")
    #             node = node.next
    #         print()
for i in range(1,k+1):
    node = bookshelves[i].head
    print(bookshelves[i].size, end = " ")
    while node != None:
        print(node.value, end = " ")
        node = node.next
    print()