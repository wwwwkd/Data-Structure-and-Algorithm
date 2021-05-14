'''

    栈得特性：先进后出得数据结构
    栈顶、栈尾
    应用：每个web浏览器都有一个返回按钮，当你浏览网页时，这些网页被放置在一个栈种（实际是网页得网址）。你现在看得网页是在顶部，你第一个查看得网页在底部，如果按下返回按钮，及那个相反的顺序浏览刚才得网页。
        Stack()创建一个空的新栈，不需要参数，返回一个空栈
        push(item)将一个新项添加到顶部，需要item作为参数，不返回任何内容
        pop()从栈中删除顶部项，不需要参数，返回item，栈被修改
        peek()从栈返回顶部元素，peek和pop的共同点是都返回栈顶元素。不同点是pop删除栈顶元素，peek不返回栈顶元素。
        isEmpty()测试栈是否为空，不需要参数，并返回布尔值
        size()返回栈中的item数量，不需要参数，并返回一个整数

'''
class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return  len(self.items)
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print('栈顶元素为：', stack.peek())
print("栈是否为空：", stack.isEmpty())
print("元素个数：", stack.size())
print(stack.pop())
print(stack.pop())
print(stack.pop())
