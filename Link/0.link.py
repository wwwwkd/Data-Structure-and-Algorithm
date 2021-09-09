class Node():
    def __init__(self, item):
        self.items = item
        self.next = None

class Link():
    def __init__(self):
        self._head = None

    # 向链表的头部添加元素
    def add(self, item):
        # 创建一个新的节点
        node = Node(item)
        # 让新加入的节点next地址 == _head连接原来的节点地址，使新节点next得到连接
        node.next = self._head
        # node ==> 变量 ==> 内存空间地址
        self._head = node
        # 这一部分一直在改变指向，如果一个引用或者变量表示某一内存空间地址
        # 那么这个引用或变量就指向了内存空间
    def travel(self):
        # _head在列表创建之后一定是不可变的
        cur = self._head
        while cur:
            print(cur.items)
            cur = cur.next

    def isEmpty(self):
        return self._head == None

    def size(self):
        cur = self._head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def append(self, item):
        node = Node(item)
        # 特殊情况：链表为空，则添加到头节点后
        if self._head == None:
            self._head = node
            return
        cur = self._head
        pre = None # 设置第一个节点之前的指针，初始话为None
        while cur:
            pre = cur # 这样，当cur移动到None时，我们就可以获得cur之前，链表最后的一个节点
            cur = cur.next
        pre.next = node # 当cur.next=None时候 不能直接赋给新加入的节点即不能循环结束后cur.next=node应该是前一个

    def search(self, item):
        cur = self._head
        find = False
        while cur:
            if cur.items == item:
                find = True
                break
            cur = cur.next
        return  find

    def insert(self, pos, item):
        node = Node(item)
        cur = self._head
        pre = None
        for i in range(pos):
            pre = cur
            cur = cur.next
        pre.next = node
        node.next = cur

    def remove(self, item):
        cur = self._head
        pre = None
        if cur.items == item:
            self._head = cur.next
            return
        while cur:
            pre = cur
            cur = cur.next
            if cur.items == item:
                pre.next = cur.next
                return
link = Link()
link.add(3)
link.add(9)
link.add(5)
link.append(9)
link.insert(4, 2)
link.remove(9)
link.travel()
print(link.isEmpty())
print(link.size())
print(link.search(1))
