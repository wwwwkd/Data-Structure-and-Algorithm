'''

    双端队列得特性:有两个头部和尾部，可以在双端进行数据得插入和删除，提供了单数据结构中队列得特性。
        Deque():创建一个空的新deque,不需要参数，返回空得deque
        addFront(item):将一个新项添加到deque得首部，需要item参数，不返回内容
        addRear():将一个新项添加到deque得尾部，需要item参数，不返回内容
        removeFront():从deque中删除首项，不需要参数，返回item，deque被篡改
        removeRear():从deque中删除尾部，不需要参数，返回item，deque被篡改
        isEmpty():测试deque是否为空，不需要参数，返回布尔值
        size():返回deque中的项数，不需要参数，返回整数

'''
class Deque():
    def __init__(self):
        self.items = []
    def addFront(self, item): # 队首进，队首出，先进先出
        self.items.insert(0, item)

    def removeFront(self):  # 从队首进1，那么2就要在1得左面
        return self.items.pop()

    def addRear(self, item): # 队尾进，队尾出，先进先出
        self.items.append(item)

    def removeRear(self): # 从队尾进1，那么2就要在1得右面
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

q = Deque()
q.addFront(1)
q.addFront(2)
q.addFront(3)

# 先进先出
print(q.removeFront())
print(q.removeFront())
print(q.removeFront())

q.addFront(1)
q.addFront(2)
q.addFront(3)

# 先进后出
print(q.removeRear())
print(q.removeRear())
print(q.removeRear())

'''
案例：回文检查，回文是一个字符串，读取首尾相同的字符，
例如，radar toot madam。
'''

def isHuiWen(s):
    ex = True
    q = Deque()
    for ch in s:
        q.addFront(ch)
    while q.size() > 1: # 如果为奇数个剩1个输出，如果偶数个剩下0个输出，因此大于1循环
        if q.removeFront() != q.removeRear():
            ex = False
            break
    return ex
print(isHuiWen('heireh'))

