class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class Link():
    def __init__(self):
        self.head = None

    def add(self, list):
        self.head = Node(int(list[0]))
        cur = self.head
        for i in list[1:]:
            cur.next = Node(int(i))
            cur = cur.next
        return self.head

    def travel(self, link):
        if link == None: return None
        while link:
            print(link.item, end=' ')
            link = link.next

class solution():
    def merge(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.item < l2.item:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2
    def merge2(self,l1, l2):
        prehead = Node(0)
        pre = prehead
        while l1 and l2:
            if l1.item < l2.item:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        pre.next = l1 if l1 is not None else l2
        return prehead.next
x = input().split()
y = input().split()
L = Link()
l1 = L.add(x)
L.travel(l1)
print('\r')
l2 = L.add(y)
L.travel(l2)
print('\r')
res = solution()
result = res.merge2(l1, l2)
L.travel(result)

