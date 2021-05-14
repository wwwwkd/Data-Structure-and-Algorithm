'''

    队列得特性：先进先出
    队首，队尾
    应用：我们的计算机实验室有30太计算器与一台打印机联网，当想打印时，他们的打印任务与其他正在等待打印的任务一致，第一个进入的任务是先完成的，如果你是最后一个，那你必须等待前面所有的打印任务先完成。
        Queue():创建一个新队列，不要参数，返回空队列
        enqueue(item):将一个新项添加到队尾，要item参数，不返回
        dequeue():从队首移除项，不需要参数，返回item，队列被修改
        isEmpty():查看队列是否为空，不需要参数，返回布尔值
        size():返回队列中得项个数，不需要参数，返回整数

'''
class Queue():
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("队列是否为空：", queue.isEmpty())
print("元素个数：", queue.size())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

'''
    
    6个人围成一个圈，排列顺序孩子们自己指定，第一个孩子手里有一个山芋，计时器计时1s后
    传给下一个孩子，以此类推，计时器每计时七秒淘汰一人，直至最后一人取得最终胜利。使用
    队列实现该游戏策率。

'''
# 根据上述准则我们可以这样想，第1s时A手里有山芋，第2s时候B手里有山芋，那么我们可以让A出队列，然后再进队列，这样就可以使拿到山芋得B位于队首。
kids = ['A', 'B', 'C', 'D', 'E', 'F']
for kid in kids:
    queue.enqueue(kid) # A位于队首，F位于队尾
while queue.size() > 1:
    for i in range(6): # 每循环一次，山芋产第一次，手里有山芋得人在队首
        kid = queue.dequeue()
        queue.enqueue(kid)

    queue.dequeue() # 第七秒位于队首得项移除
print('获胜的选手是:', queue.dequeue())
